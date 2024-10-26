# Veri Servisleri Projesi

Bu proje, çeşitli veri servislerinin kullanımı ve yönetimi için bir dizi örnek uygulama ve Docker yapılandırması içermektedir. Aşağıda, her bir servisin tanımı ve işlevi bulunmaktadır.

## Servisler

### 1. Kafka
**Tanım:** Mesaj kuyruğu servisi; veri akışını yönetir. Dağıtık sistemler arasında asenkron iletişim sağlar.  
**Kullanım:** Gerçek zamanlı veri akışları için idealdir. Örneğin, kullanıcı etkinliklerini takip etmek veya uygulama bileşenleri arasında mesaj iletmek için kullanılabilir.

### 2. Kafdrop
**Tanım:** Kafka'nın kullanıcı dostu bir arayüzüdür; konular ve mesajları görüntülemeye yarar.  
**Kullanım:** Kafka ortamınızı görsel olarak yönetmek ve mesajları takip etmek için kullanılır.

### 3. MySQL
**Tanım:** İlişkisel veritabanı yönetim sistemi; veri depolamak için kullanılır.  
**Kullanım:** Yapılandırılmış verilerin saklanması ve yönetilmesi için idealdir. Örneğin, web uygulamalarında kullanıcı bilgilerini saklamak için kullanılabilir.

### 4. phpMyAdmin
**Tanım:** MySQL için bir web arayüzüdür; veritabanlarını yönetmek için kullanılır.  
**Kullanım:** MySQL veritabanlarınızı kolayca yönetmek ve sorgulamak için grafiksel bir arayüz sağlar.

### 5. MongoDB
**Tanım:** NoSQL veritabanı; esnek veri yapıları için idealdir.  
**Kullanım:** Dinamik ve değişken veri yapılarının depolanması için kullanılır. Örneğin, JSON formatında veri saklamak için tercih edilir.

### 6. Mongo Express
**Tanım:** MongoDB için web tabanlı bir yönetim arayüzüdür.  
**Kullanım:** MongoDB veritabanlarınızı görsel olarak yönetmek ve sorgulamak için kullanılır.

### 7. PostgreSQL
**Tanım:** Diğer bir ilişkisel veritabanıdır; daha karmaşık veri yapıları için uygundur.  
**Kullanım:** Gelişmiş veri analizi ve yönetimi için tercih edilir; özellikle karmaşık ilişkileri olan veri setleri için idealdir.

### 8. Cassandra
**Tanım:** Dağıtık NoSQL veritabanıdır; yüksek veri ölçeklenebilirliği sağlar.  
**Kullanım:** Büyük ölçekli veri uygulamaları için kullanılabilir; yüksek yazma ve okuma performansı gerektiren senaryolarda idealdir.

### 9. ClickHouse
**Tanım:** Analitik veritabanıdır; hızlı sorgulama ve veri analizi için kullanılır.  
**Kullanım:** Büyük veri setleri üzerinde hızlı analiz yapmak için ideal bir çözümdür.

### 10. Redis
**Tanım:** Anahtar-değer veritabanıdır; veri önbellekleme ve hızlı veri erişimi için kullanılır.  
**Kullanım:** Performansı artırmak için sıkça kullanılan bir önbellekleme mekanizmasıdır.

### 11. InfluxDB
**Tanım:** Zaman serisi veritabanıdır; özellikle zamanla değişen verileri depolamak için idealdir.  
**Kullanım:** IoT, uygulama performansı ve diğer zaman serisi verilerini izlemek için kullanılır.

### 12. Chronograf
**Tanım:** InfluxDB ile birlikte çalışır; zaman serisi verileri görselleştirmeye yarar.  
**Kullanım:** Zaman serisi verilerinizi grafiklerle analiz etmek için kullanılır.

### 13. Elasticsearch
**Tanım:** Arama ve analiz motorudur; büyük veri setlerinde hızlı arama sağlar.  
**Kullanım:** Log analizi, veri keşfi ve metin arama uygulamaları için yaygın olarak kullanılır.

### 14. Kibana
**Tanım:** Elasticsearch verilerini görselleştirmek için kullanılır.  
**Kullanım:** Elasticsearch ile toplanan verilerin grafik ve görsellerle sunulmasını sağlar.

### 15. Neo4j
**Tanım:** Graf veritabanıdır; ilişkisel verileri grafiksel olarak yönetmek için kullanılır.  
**Kullanım:** Karmaşık ilişkileri olan veri setlerinde veri modellemesi ve analizi için idealdir.

### 16. CouchDB
**Tanım:** NoSQL veritabanıdır; HTTP üzerinden erişilebilir veri depolama sağlar.  
**Kullanım:** Belge tabanlı verilerin saklanması için kullanılır.

### 17. Data Collection Servisleri
**Tanım:** Python ve Node.js ile veri toplamak için yazılmış uygulamalardır.  
**Kullanım:** Farklı veri kaynaklarından veri toplamak ve işlemek için kullanılır.
