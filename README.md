GeoLookup
GeoLookup uygulaması, adresleri coğrafi koordinatlara dönüştürmek için geliştirilmiş bir Python tabanlı web uygulamasıdır. Kullanıcılar, il, ilçe, mahalle, sokak ve isteğe bağlı olarak kapı numarası bilgileri girerek, bu adreslere ait enlem (latitude) ve boylam (longitude) bilgilerini alabilirler.

Özellikler
Adreslerden Koordinat Bulma: Uygulama, OpenStreetMap API (Nominatim) kullanarak adreslerden enlem ve boylam bilgisi alır.
Excel Yükleme ve Koordinat Ekleme: Excel dosyasındaki adresleri yükleyerek her adres için koordinat bilgisi alabilir ve bu verileri yeni bir Excel dosyasına kaydedebilirsiniz.
Çevrimdışı Çalışma: Uygulama, çevrimdışı çalışma modu kapalı olarak çalışır ve çevrimiçi veritabanlarından doğru verileri alır.
Kullanım
Uygulamayı Başlatın:

Python ve gerekli bağımlılıkların kurulu olduğundan emin olun.
app.py dosyasını çalıştırarak web uygulamasını başlatın.
python app.py
Adres Bilgilerini Girin:

Web tarayıcınızda localhost:5000 adresini ziyaret ederek uygulamayı açın.
Adres bilgilerini (il, ilçe, mahalle, sokak, kapı numarası) girerek koordinat bilgilerini alın.
Excel Dosyası Yükleyin:

Adreslerinizin bulunduğu bir Excel dosyasını yükleyin.
Uygulama, her adres için enlem ve boylam bilgilerini hesaplayarak yeni bir Excel dosyasına dönüştürür.
Teknolojiler
Python: Uygulama Python 3 ile geliştirilmiştir.
Flask: Web uygulaması framework'ü olarak Flask kullanılmıştır.
Pandas: Excel dosyalarını işlemek için Pandas kütüphanesi kullanılmaktadır.
Requests: OpenStreetMap API'ye istek göndermek için Requests kütüphanesi kullanılır.
API
OpenStreetMap Nominatim API: Adreslerden enlem ve boylam bilgisi almak için OpenStreetMap'in Nominatim API'si kullanılır.
Kurulum
Bağımlılıkları Yükleyin:

Aşağıdaki komutla gerekli Python paketlerini yükleyin:
pip install -r requirements.txt
Uygulamayı Başlatın:

Uygulamayı başlatmak için şu komutu çalıştırın:
python app.py
Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
