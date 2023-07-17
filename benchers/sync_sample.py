import pathlib
import sys
import time

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from requesters import sync_req

s = time.perf_counter()
sync_req.run_sync(20_000)
e = time.perf_counter()
print(f'(Sync) elapsed: {e - s:f}')
