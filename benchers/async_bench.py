import asyncio
import csv
import functools
import logging
import pathlib
import time

from benchers import number_of_reqs
from requesters import async_req

stat_file = pathlib.Path(__file__).parent.parent / "stats/async_data.csv"


def async_timer(coro):
    @functools.wraps(coro)
    async def inner(*args, **kwargs):
        s = time.perf_counter()
        await coro(*args, **kwargs)
        e = time.perf_counter()
        return float(f"{e - s:f}")

    return inner


logger = logging.getLogger(__file__)
logger.info("Starting the benchmark for async version")

elapsed_times = []
run_async = async_timer(async_req.run_async)
for num_of_req in number_of_reqs:
    logger.info(f"Benchmarking with '{num_of_req}' number of requests!")
    elapsed_times.append(took := asyncio.run(run_async(num_of_req)))
    logger.info(f"Took: {took} seconds.")

logger.info(f"Writing the statistics to '{stat_file}'")

with open(stat_file, "w") as f:
    fieldnames = ["number_of_reqs", "elapsed_time"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    data = []
    for num, e_time in zip(number_of_reqs, elapsed_times):
        data.append({"number_of_reqs": num, "elapsed_time": e_time})
    writer.writerows(data)
