"""Ex 3.35. Signal handling when using asyncio.run()."""
import asyncio
from signal import SIGINT, SIGTERM


async def main():
    loop = asyncio.get_event_loop()
    for sig in (SIGINT, SIGTERM):
        loop.add_signal_handler(sig, handler, sig)

    try:
        while True:
            print('app running')
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        for i in range(3):
            print('app shutting down')
            await asyncio.sleep(1)


def handler(sig):
    loop = asyncio.get_event_loop()
    for task in asyncio.all_tasks(loop=loop):
        task.cancel()
    print(f'Got signal: {sig!s}, shutting down')
    loop.remove_signal_handler(SIGTERM)
    loop.add_signal_handler(SIGINT, lambda: None)


if __name__ == '__main__':
    asyncio.run(main())
