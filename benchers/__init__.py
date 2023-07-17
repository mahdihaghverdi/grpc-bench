import logging
from itertools import chain

data = [
    [1 * mul, 2 * mul if mul < 100_000 else 0, 5 * mul if mul < 100_000 else 0]
    for mul in (1, 10, 100, 1000, 10_000, 100_000)
]

number_of_reqs = list(filter(bool, list(chain.from_iterable(data))))

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    datefmt="%d-%b-%Y %I:%M:%S",
    handlers=[logging.StreamHandler()],
)
