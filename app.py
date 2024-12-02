from flask import Flask, render_template, request, send_file
import pandas as pd
import requests
from io import BytesIO
import time

app = Flask(__name__)

# OpenCage API ile koordinat bulma fonksiyonu
def get_coordinates(address):
    try:
        url = "https://api.opencagedata.com/geocode/v1/json"
        params = {
            "q": address,
            "key": "85af1d8affb3414488fb467a1d1861e5",  # OpenCage API anahtarınız
            "language": "tr",  # Türkçe dil desteği
            "no_annotations": 1  # Gereksiz açıklamaları engeller
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                lat = data['results'][0]['geometry']['lat']
                lon = data['results'][0]['geometry']['lng']
                return lat, lon
        return None, None
    except Exception as e:
        print(f"API hatası: {e}")
        return None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-coordinates', methods=['POST'])
def get_coordinates_route():
    # Kullanıcıdan form ile gelen bilgileri alıyoruz
    sokak = request.form['sokak']
    kapı_numarası = request.form.get('kapı_numarası', '')  # Kapı numarasını opsiyonel olarak alıyoruz
    mahalle = request.form['mahalle']
    ilce = request.form['ilce']
    il = request.form['il']

    # Adresi oluşturuyoruz
    address_parts = [sokak]
    
    # Kapı numarasını ekliyoruz (varsa)
    if kapı_numarası:
        address_parts.append(f"No:{kapı_numarası}")
    
    address_parts += [mahalle, ilce, il]
    address = ', '.join(address_parts) + ", Türkiye"
    
    # Koordinatları alıyoruz
    lat, lon = get_coordinates(address)

    return render_template('result.html', address=address, lat=lat, lon=lon)

@app.route('/upload-excel', methods=['POST'])
def upload_excel():
    file = request.files['file']
    df = pd.read_excel(file)

    # Sütun adlarını temizliyoruz (boşlukları kaldırıyoruz)
    df.columns = df.columns.str.strip()

    # Sonuçları tutmak için liste
    results = []
    failed_addresses = []  # Koordinat bulunamayan adresler için

    for index, row in df.iterrows():
        # Excel'deki sütunlardan verileri alıyoruz
        sokak = row['Sokak']
        kapı_numarası = row.get('Kapı Numarası', '')  # Kapı numarasını opsiyonel alıyoruz
        mahalle = row['Mahalle']
        ilce = row['İlçe']
        il = row['İl']
        
        # Adresi oluşturuyoruz
        address_parts = [sokak]
        
        # Kapı numarasını ekliyoruz (varsa)
        if kapı_numarası:
            address_parts.append(f"No:{kapı_numarası}")
        
        address_parts += [mahalle, ilce, il]
        address = ', '.join(address_parts) + ", Türkiye"
        
        # Koordinatları alıyoruz
        lat, lon = get_coordinates(address)

        # Koordinatları kontrol ediyoruz
        if lat is None or lon is None:
            failed_addresses.append(address)
        
        results.append({
            "address": address,
            "latitude": lat if lat else "Koordinat bulunamadı",
            "longitude": lon if lon else "Koordinat bulunamadı"
        })

        # API sınırlarını aşmamak için bekleme ekliyoruz
        time.sleep(1)

    # Hatalı adresleri konsola yazdırıyoruz
    if failed_addresses:
        print("Koordinat bulunamayan adresler:")
        for addr in failed_addresses:
            print(addr)

    # Yeni bir DataFrame oluşturuyoruz
    result_df = pd.DataFrame(results)

    # Sonuçları Excel dosyasına dönüştürüyoruz
    output = BytesIO()
    result_df.to_excel(output, index=False)
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="coordinates.xlsx")

if __name__ == '__main__':
    app.run(debug=True)
