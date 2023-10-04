import asyncio


async def f():
    await asyncio.sleep(0)
    return 111

loop = asyncio.get_event_loop()
coro = f()

# this internally calls .send(None) method calls, it detects completion by handling StopIteration which also contains value
print(loop.run_until_complete(coro))
