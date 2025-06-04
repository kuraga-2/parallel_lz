import asyncio

async def some_func():
  print("Start sleeping")
  await asyncio.sleep(1)
  print("Done sleeping")

async def main():
    try:
        await asyncio.wait_for(some_func(), timeout=2.0)
    except asyncio.TimeoutError:
        print('timeout!')