import asyncio


async def f():
    loop = asyncio.get_event_loop()
    for i in range(10):
        loop.create_task(NotImplemented)
