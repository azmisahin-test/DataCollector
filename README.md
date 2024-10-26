# Proje Teknolojileri ve Servisleri

Bu belgede, projemizde kullandığımız teknolojiler ve bunların sunduğu hizmetler hakkında bilgiler yer almaktadır.

## 1. Mesaj Brokerleri

### Kafka
- **Açıklama**: Yüksek hacimli veri akışlarını işlemek için kullanılan dağıtık bir mesajlaşma sistemidir. Üreticilerden tüketicilere veri iletimini sağlar.
- **Kullanım Alanları**: Gerçek zamanlı veri akışı, olay tabanlı mimariler.

### RabbitMQ
- **Açıklama**: Açık kaynak kodlu bir mesaj kuyruğu yazılımıdır. Mesajları güvenli bir şekilde yönlendirir ve dağıtır.
- **Kullanım Alanları**: Mesaj iletimi, arka planda çalışan mikroservisler arasında veri paylaşımı.

## 2. Veri Tabanları

### MySQL
- **Açıklama**: İlişkisel bir veritabanı yönetim sistemidir. Yapılandırılmış verilerin depolanması için idealdir.
- **Kullanım Alanları**: Kullanıcı bilgileri, uygulama verileri.

### MongoDB
- **Açıklama**: NoSQL veritabanıdır ve belge tabanlı bir yapıya sahiptir. JSON formatında veri depolar.
- **Kullanım Alanları**: Esnek veri yapısı gerektiren uygulamalar, büyük veri uygulamaları.

### PostgreSQL
- **Açıklama**: İleri düzey özelliklere sahip bir ilişkisel veritabanı sistemidir. Verilerin karmaşık sorgularla işlenmesini sağlar.
- **Kullanım Alanları**: Analitik uygulamalar, coğrafi bilgi sistemleri.

### Cassandra
- **Açıklama**: Dağıtık bir NoSQL veritabanıdır. Yüksek yazma ve okuma hızı ile bilinir.
- **Kullanım Alanları**: Büyük veri uygulamaları, yüksek ölçeklenebilirlik gerektiren projeler.

### ClickHouse
- **Açıklama**: Analitik veritabanı yönetim sistemidir. Gerçek zamanlı veri analizi için optimize edilmiştir.
- **Kullanım Alanları**: Veri analitiği, büyük veri raporlama.

### Redis
- **Açıklama**: Anahtar-değer veritabanı olarak çalışan bir bellek içi veri deposudur. Hızlı veri erişimi sağlar.
- **Kullanım Alanları**: Önbellekleme, hızlı veri erişimi gerektiren uygulamalar.

### InfluxDB
- **Açıklama**: Zaman serisi verilerini depolamak ve sorgulamak için tasarlanmış bir veritabanıdır.
- **Kullanım Alanları**: Gerçek zamanlı veri izleme, IoT uygulamaları.

### Neo4j
- **Açıklama**: Graf tabanlı bir veritabanı yönetim sistemidir. Veriler arasındaki ilişkileri görselleştirir.
- **Kullanım Alanları**: Sosyal ağlar, ilişkisel veri analizleri.

### CouchDB
- **Açıklama**: NoSQL veritabanıdır ve verileri JSON belgeleri olarak depolar. Dağıtık bir yapıdadır.
- **Kullanım Alanları**: Verilerin esnek yapıda saklanması gereken uygulamalar.

## 3. İzleme ve Yönetim Araçları

### Prometheus
- **Açıklama**: Zaman serisi verilerini toplamak ve izlemek için kullanılan bir sistemdir. Kendi sorgulama dili (PromQL) ile veri analizine olanak tanır.
- **Kullanım Alanları**: Uygulama ve sistem izleme, uyarı sistemleri.

### Grafana
- **Açıklama**: Veri görselleştirme aracı olarak kullanılan bir platformdur. Farklı veri kaynaklarından gelen verileri grafiklerle sunar.
- **Kullanım Alanları**: İzleme panoları, analitik raporlar.

## 4. Web Servisleri

### Nginx
- **Açıklama**: Yük dengelemesi ve ters proxy işlevselliği sunan bir web sunucusudur. Performans ve ölçeklenebilirlik için idealdir.
- **Kullanım Alanları**: Statik içerik sunumu, API yönlendirmesi.

## 5. Elasticsearch ve Kibana

### Elasticsearch
- **Açıklama**: Tam metin arama ve analitik veritabanı olarak çalışan bir sistemdir. Veri sorgulama ve analiz için güçlü bir arayüz sunar.
- **Kullanım Alanları**: Veri arama, analitik raporlama.

### Kibana
- **Açıklama**: Elasticsearch ile entegre çalışan bir veri görselleştirme ve analiz aracıdır.
- **Kullanım Alanları**: Elasticsearch verilerinin görselleştirilmesi, panoların oluşturulması.

## Sonuç
Bu teknolojiler, projenin verimliliğini artırmak, veri akışını yönetmek ve izlemek için kritik öneme sahiptir. Her bir bileşen, projenin ihtiyaçlarına yönelik olarak seçilmiş ve optimize edilmiştir.
