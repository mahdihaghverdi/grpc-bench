import csv
import pathlib

import matplotlib.pyplot as plt
from benchers import number_of_reqs

sync_stats = pathlib.Path(__file__).parent / "stats/sync_data.csv"

sync_elapses = []
with open(sync_stats) as f:
    reader = csv.DictReader(f)
    for row in reader:
        sync_elapses.append(row["elapsed_time"])


plt.figure(figsize=(10, 6))
plt.plot(number_of_reqs, sync_elapses, "-")
plt.xlabel("number of requests")
plt.ylabel("elapsed time")
plt.savefig("sync_stats.png")
