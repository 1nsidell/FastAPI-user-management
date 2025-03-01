import json
from typing import Dict, Any, Optional, Self
from datetime import timedelta

import redis.asyncio as redis
from src.app.repositories import CacheRepositoryProtocol
from src.app.repositories import handle_redis_exceptions
from src.settings import settings


class RedisUsersCacheImpl(CacheRepositoryProtocol):
    def __init__(self: Self, redis_pool: redis.ConnectionPool) -> None:
        self.redis = redis.Redis(
            connection_pool=redis_pool,
            decode_responses=True,
        )

    @handle_redis_exceptions
    async def add(self: Self, key: Any, data: Dict[Any, Any]) -> None:
        expiration = int(
            timedelta(
                minutes=settings.redis.USERS_CACHE_LIFETIME
            ).total_seconds()
        )
        json_data = json.dumps(data)
        await self.redis.set(key, json_data, ex=expiration)

    @handle_redis_exceptions
    async def get(self: Self, key: Any) -> Optional[Dict[Any, Any]]:
        value = await self.redis.get(key)
        return json.loads(value) if value else None

    @handle_redis_exceptions
    async def delete(self: Self, key: Any) -> bool:
        deleted = await self.redis.delete(key)
        return deleted > 0

    @handle_redis_exceptions
    async def close(self: Self) -> None:
        await self.redis.close()
