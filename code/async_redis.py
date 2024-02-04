import asyncio
from redis.asyncio.client import Redis


async def main():
    redis = await Redis(host='localhost', port=6379)
    keys = ['Americas', 'Africa', 'Europe', 'Asia']
    async for value in one_at_a_time(redis, keys):
        print(value)


async def one_at_a_time(redis, keys):
    for k in keys:
        value = await redis.get(k)
        yield value


asyncio.run(main())
