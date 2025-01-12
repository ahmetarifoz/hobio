import redis
from app.core.config import settings

def get_redis_client():
    redis_client = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        db=settings.redis_db,
        decode_responses=True
    )
    return redis_client
