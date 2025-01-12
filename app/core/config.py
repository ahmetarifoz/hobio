from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

class Settings(BaseSettings):
    authjwt_secret_key: str = os.getenv("AUTHJWT_SECRET_KEY")
    authjwt_access_token_expires: int = int(os.getenv("AUTHJWT_ACCESS_TOKEN_EXPIRES", 3600))
    database_url: str = os.getenv("DATABASE_URL")
    redis_host: str = os.getenv("REDIS_HOST", "localhost")
    redis_port: int = int(os.getenv("REDIS_PORT", 6379))
    redis_db: int = int(os.getenv("REDIS_DB", 0))

settings = Settings()
