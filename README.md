# Hobio - Hobby Recommendation and Community App

Hobio, kullanıcıların hobilerini keşfetmesini, hobileriyle ilgili topluluklara katılmasını ve ilgi alanlarına göre diğer kullanıcılarla bağlantı kurmasını sağlayan bir platformdur. Bu uygulama hem bireysel olarak hobiler üzerine yoğunlaşmak isteyen hem de benzer ilgi alanlarına sahip arkadaşlar edinmek isteyenlere hitap eder.

## Özellikler

- Kullanıcı Kaydı ve Kimlik Doğrulama (JWT tabanlı).
- Kullanıcıların hobilerini seçmesi ve yönetmesi.
- Hobi öneri sistemi.
- Hobilere özel lobiler ve mesajlaşma sistemi.
- Kullanıcı rollerine göre farklı erişim seviyeleri (Admin, User, Moderator).
- Admin paneli ile kullanıcı ve içerik yönetimi.

---

## Kurulum

### 1. Gereksinimler

- Python 3.9+
- PostgreSQL
- Redis
- FastAPI
- Docker (opsiyonel)

### 2. Ortam Değişkenleri

Proje için gerekli olan `ENV` değişkenlerini yapılandırın. Ana dizinde bir `.env` dosyası oluşturun ve aşağıdaki bilgileri ekleyin:

```env
AUTHJWT_SECRET_KEY=your_secret_key
AUTHJWT_ACCESS_TOKEN_EXPIRES=30
DATABASE_URL=postgresql://user:password@localhost/hobio_db
