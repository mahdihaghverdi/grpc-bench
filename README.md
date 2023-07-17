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

These two files are just really small requesters for small and command line results.
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


## Produce yourself
To produce the results yourself you have to do the following:

**clone the repo**
```bash
git clone https://github.com/mahdihaghverdi/grpc-bench
```

**go inside**
```bash
cd grpc-bench
```

**create a virtual environment**
```bash
python -m venv .venv
```

**install the requirements**
```bash
pip install -r requirements.txt
```

**activate the venv (linux)**
```bash
source .venv/bin/activate
```

- ### async test

run the server
```bash
python servers/async_server.py
```
in another terminal, run the bencher
```bash
python benchers/async_bench.py
```

- ### sync test
```bash
python servers/sync_server.py
```
```bash
python benchers/sync_bench.py
```

**to plot the results**
- whole
```bash
python plot_whole.py
```
- async
```bash
python async_plot.py
```
- sync
```bash
python sync_plot.py
```

**to see and try the sample benchmarks**
- async
```bash
python benchers/async_sample.py 
```
- sync
```bash
python benchers/sync_sample.py 
```

## Os and Python versions of this benchmack
```
>>> import os
>>> os.uname()
posix.uname_result(sysname='Linux', nodename='mahdi', release='5.19.0-46-generic', version='#47~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Jun 21 15:35:31 UTC 2', machine='x86_64')
>>>
```

```
>>> import platform
>>> platform.python_version()
'3.10.6'
>>> platform.python_build()
('main', 'May 29 2023 11:10:38')
>>> platform.python_compiler()
'GCC 11.3.0'
>>> platform.python_implementation()
'CPython'
>>>
```
