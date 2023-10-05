"""Ex 3.29. Destroyer of pending tasks"""

import asyncio


async def f(delay):
    await asyncio.sleep(delay)


loop = asyncio.get_event_loop()
t1 = loop.create_task(f(1))
t2 = loop.create_task(f(2))
loop.run_until_complete(t1)

# will give "Task was destroyed but it is pending!"
# since we closed the loop while t2 wasnt completed
loop.close()
