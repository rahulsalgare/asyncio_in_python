"""Ex 3.18. A closer look at what ensure_future() is doing."""

import asyncio

async def f():
    pass

coro = f()
loop = asyncio.get_event_loop()

task = loop.create_task(coro)
print(isinstance(task, asyncio.Task), isinstance(task, asyncio.Future))

# we pass coroutine object, gets back Task instance
new_task = asyncio.ensure_future(coro)
print(isinstance(task, asyncio.Task),  isinstance(task, asyncio.Future))

# when we pass task/future instance, we get back future instance
mystery = asyncio.ensure_future(task)
print(mystery is task)

fut = asyncio.Future()
myster2 = asyncio.ensure_future(fut)
print(myster2 is fut)

# what happens if we pass task to create task
# suspense = loop.create_task(mystery)              # cannot do this, create_task only takes coroutine object
# print(suspense)