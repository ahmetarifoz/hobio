# Hobio - Hobby Recommendation and Community App

Hobio, kullanıcıların hobilerini keşfetmesini, hobileriyle ilgili topluluklara katılmasını ve ilgi alanlarına göre diğer kullanıcılarla bağlantı kurmasını sağlayan bir platformdur. Bu uygulama, bireysel hobiler üzerine yoğunlaşmak isteyenler ve benzer ilgi alanlarına sahip arkadaşlar edinmek isteyenler için tasarlanmıştır.

## Özellikler

- Kullanıcı kaydı ve kimlik doğrulama (JWT tabanlı).
- Kullanıcıların hobilerini seçip yönetmesi.
- Hobi öneri sistemi.
- Hobilere özel lobiler ve mesajlaşma.
- Rol tabanlı erişim kontrolü (Admin, User, Moderator).
- Admin paneli ile kullanıcı ve içerik yönetimi.

---

## Kurulum

### Gereksinimler

- Python 3.9+
- PostgreSQL
- Redis
- FastAPI
- Docker (opsiyonel)

### Adımlar

1. **Depoyu Klonlayın**
   ```bash
   git clone https://github.com/username/hobio.git
   cd hobio
   ```

2. **Sanal Ortamı Kurun**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

4. **.env Dosyasını Ayarlayın**

   Proje kök dizininde `.env` dosyası oluşturun ve aşağıdaki bilgileri ekleyin:

   ```env
   AUTHJWT_SECRET_KEY=your_secret_key
   AUTHJWT_ACCESS_TOKEN_EXPIRES=30
   DATABASE_URL=postgresql://username:password@localhost/hobio_db
   ```

5. **Veritabanını Ayarlayın**
   Alembic ile veritabanı tablolarını oluşturun:
   ```bash
   alembic upgrade head
   ```

6. **Uygulamayı Çalıştırın**
   ```bash
   uvicorn main:app --reload
   ```

7. **API Dokümantasyonu**
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Kullanım

### Kullanıcı Kaydı
- **Endpoint**: `/auth/register`
- **Yöntem**: `POST`
- **Örnek İstek**:
  ```json
  {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "password": "securepassword",
    "role": "user"
  }
  ```

### Token Alma
- **Endpoint**: `/auth/token`
- **Yöntem**: `POST`
- **Örnek İstek**:
  ```json
  {
    "username": "john_doe",
    "password": "securepassword"
  }
  ```

---

## Proje Hakkında

Hobio, kullanıcıların hobilerini keşfetmesini ve hobileri aracılığıyla bağlantılar kurmasını sağlayan bir platformdur. Hem bireysel hem de topluluk odaklı bir deneyim sunar.

---

## Katkıda Bulunma

Katkıda bulunmak isterseniz şu adımları takip edebilirsiniz:

1. Depoyu fork edin.
2. Yeni bir dal oluşturun:
   ```bash
   git checkout -b my-new-feature
   ```
3. Değişikliklerinizi commit edin:
   ```bash
   git commit -m "Add my feature"
   ```
4. Değişikliklerinizi push edin:
   ```bash
   git push origin my-new-feature
   ```
5. Pull Request gönderin.

---

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
