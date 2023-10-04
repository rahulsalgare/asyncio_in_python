"""Ex 3.17. Calling set_result() on a Task"""

import asyncio
from contextlib import suppress


async def main(f: asyncio.Future):
    print('main')
    await asyncio.sleep(1)
    try:
        # not allowed will raise RuntimeError. Task represents a running coroutine,
        # so the result should always come only from that
        f.set_result('I am finished')
    except RuntimeError as e:
        print('Not allowed')
        f.cancel()


loop = asyncio.get_event_loop()
fut = asyncio.Task(asyncio.sleep(1_000_000))    #????
print(fut)
task2 = loop.create_task(main(fut))
print(task2)

with suppress(asyncio.CancelledError):
    loop.run_until_complete(fut)

print(fut.done())
print(fut.cancelled())
