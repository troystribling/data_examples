import asyncio

async def print_every_second():
    for i in range(60):
        print(f"{i}s")
        await asyncio.sleep(1)

async def print_every_minute():
    for i in range(1, 2):
        await asyncio.sleep(60)
        print(f"{i} minutes")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(print_every_second(), print_every_minute()))
loop.close()
