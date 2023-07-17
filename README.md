# `gRPC` Python Benchmark

In this benchmark I tested sync and async servers

## Benchers
There are 4 files in the benchers package
- async_bench.py
- sync_bench.py

These two are the main benchmark files. They send requests to their appropriate server.
The number of requests they send is in the `__init__.py` file of this package.
Also they log everything happens in the benchmark.

- async_sample.py
- sync_sample.py

- These two files are just really small requesters for small and command line results.
You can see their results with 
```bash
python sync_sample.py
```

There are 3 pictures in the repo.
- [plot_whole.png](https://github.com/mahdihaghverdi/grpc-bench/blob/main/whole_stats.png)
- [async_plot.png](https://github.com/mahdihaghverdi/grpc-bench/blob/main/async_stats.png)
- [sync_plot.png](https://github.com/mahdihaghverdi/grpc-bench/blob/main/sync_stats.png)

### plot_whole.png
![](https://github.com/mahdihaghverdi/grpc-bench/blob/main/whole_stats.png)

In this image, I plotted the results of both async (orange) and sync (blue) requesters.
There is no doubt that the sync version takes really longer than the async version.

In these two pictures you can see the actual times against the number of requests which are done by that requester.
#### async
![](https://github.com/mahdihaghverdi/grpc-bench/blob/main/async_stats.png)

#### sync 
![](https://github.com/mahdihaghverdi/grpc-bench/blob/main/sync_stats.png)
