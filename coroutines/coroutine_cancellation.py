"""Ex 3.9. Coroutine cancellation with CancelledError."""

import asyncio


async def f():
    try:
        while True:
            print('executing')
            await asyncio.sleep(0)

    except asyncio.CancelledError:
        print('Cancelled')

    else:
        return 111


coro = f()
coro.send(None)
coro.send(None)
coro.throw(asyncio.CancelledError)              # internally used in asyncio for task cancellation