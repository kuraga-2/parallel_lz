import asyncio

async def some_func():
  print("Start sleeping")
  await asyncio.sleep(1)
  print("Done sleeping")