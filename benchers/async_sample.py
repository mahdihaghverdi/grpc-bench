import asyncio
import pathlib
import sys
import time

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from requesters import async_req

s = time.perf_counter()
asyncio.run(async_req.run_async(20_000))
e = time.perf_counter()
print(f'(Async) elapsed: {e - s:f}')
