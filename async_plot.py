import csv
import pathlib

import matplotlib.pyplot as plt
from benchers import number_of_reqs

async_stats = pathlib.Path(__file__).parent / "stats/async_data.csv"

async_elapses = []
with open(async_stats) as f:
    reader = csv.DictReader(f)
    for row in reader:
        async_elapses.append(row["elapsed_time"])

plt.figure(figsize=(10, 6))

plt.plot(number_of_reqs, async_elapses)
plt.xlabel("number of requests")
plt.ylabel("elapsed time")
plt.savefig("async_stats.png")
