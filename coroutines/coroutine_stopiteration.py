"""Ex 3.6. Coroutine internals: using send() and StopIteration"""

async def f():
    return 123

coro = f()
try:
    coro.send(None)
except StopIteration as e:              # when coroutine returns, StopIteration is raised
    print('answer is ', e.value)

