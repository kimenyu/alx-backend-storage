#!/usr/bin/env python3
"""redis basics"""



import redis
import uuid
from typing import Union

class Cache:
    """class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()

        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)
        return random_key
