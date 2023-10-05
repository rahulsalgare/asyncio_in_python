import asyncio
from signal import SIGINT, SIGTERM


async def main():
    try:
        while True:
            print('app is running')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        for i in range(3):
            print('app shutting down')
            await asyncio.sleep(1)


def handler(sig):
    loop = asyncio.get_event_loop()
    loop.stop()
    print(f'Got signal: {sig!s}, shutting down')
    loop.remove_signal_handler(SIGTERM)

    # if we remove SIGINT, KeyboardInterrupt will again become handler for SIGINT
    # if we set an empy lambda function as handler, SIGINT has no effect.
    loop.add_signal_handler(SIGINT, lambda: None)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for sig in (SIGINT, SIGTERM):
        loop.add_signal_handler(sig, handler, sig)  # this prints SIGINT
        # loop.add_signal_handler(sig, lambda: handler(sig))          # and this prints SIGTERM, strange

    loop.create_task(main())
    loop.run_forever()
    tasks = asyncio.all_tasks(loop=loop)
    print(tasks)
    for t in tasks:
        t.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    print(group)
    loop.run_until_complete(group)
    loop.close()
