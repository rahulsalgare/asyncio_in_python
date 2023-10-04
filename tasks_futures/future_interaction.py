"""Ex 3.16. Interaction with a Future instance"""
import asyncio

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result('I am finished')

loop = asyncio.get_event_loop()
fut = asyncio.Future()
print(fut)
print(fut.done())

task = loop.create_task(main(fut))
print(task)

loop.run_until_complete(fut)
print(fut.done())
print(fut.result())