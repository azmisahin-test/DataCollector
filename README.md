# Proje Yapısı

Bu proje, çeşitli veri hizmetlerini ve izleme (monitoring) servislerini bir araya getirir. Aşağıda her bir servisin tanımı ve kullanım alanları bulunmaktadır.

## 1. Mesajlaşma Servisleri

### Kafka ve Kafdrop
- **Kafka**: Dağıtık bir mesajlaşma sistemi; veri akışını yönetir.
- **Kafdrop**: Kafka'nın kullanıcı dostu bir arayüzü; veri akışını görsel olarak izlemeye yarar.

## 2. Veri Tabanları

### İlişkisel Veritabanları
- **MySQL**: Yapılandırılmış veri için ideal bir ilişkisel veritabanıdır.
- **phpMyAdmin**: MySQL için web tabanlı yönetim arayüzü.
- **PostgreSQL**: Gelişmiş özelliklere sahip bir ilişkisel veritabanıdır.
- **PgAdmin**: PostgreSQL için web tabanlı bir yönetim arayüzü.

### NoSQL Veritabanları
- **MongoDB**: Esnek veri yapıları için uygun bir NoSQL veritabanıdır.
- **Mongo Express**: MongoDB'yi görsel olarak yönetmek için bir arayüz.
- **Cassandra**: Yüksek ölçeklenebilirlik sunan dağıtık bir NoSQL veritabanıdır.
- **CouchDB**: HTTP üzerinden erişilebilen belge tabanlı bir veritabanıdır.

### Analitik Veritabanları
- **ClickHouse**: Hızlı analitik sorgular için tasarlanmış bir veritabanıdır.

### Diğer
- **Redis**: Anahtar-değer veritabanı; veri önbellekleme için idealdir.
- **InfluxDB**: Zaman serisi veritabanı; zamanla değişen verileri yönetir.
- **Chronograf**: Zaman serisi verilerini görselleştirmek için kullanılan bir araç.
- **Elasticsearch**: Arama ve analiz motorudur.
- **Kibana**: Elasticsearch ile toplanan verileri görselleştirir.
- **Neo4j**: Graf veritabanı; ilişkisel verileri grafiksel olarak yönetir.

## 3. İzleme Servisleri

- **Prometheus**: Zaman serisi veri toplama ve izleme aracı.
- **Grafana**: Zaman serisi verilerini görselleştirmek için kullanılır.
