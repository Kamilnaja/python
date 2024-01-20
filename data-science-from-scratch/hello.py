import random
from typing import Callable, Dict, List, Optional

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


def double(x):
    return x * 2


def apply_to_one(f):
    return f(1)


y = apply_to_one(lambda x: x + 4)


def another_double(x):
    return 2 * x


def my_print(message="my default message"):
    print(message)


def full_name(first="Whats your name", last="Something"):
    return first + " " + last


first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name
full_name2 = "{0} {1}".format(first_name, last_name)
full_name3 = f"{first_name} {last_name}"

# try:
#     print(0 / 0)
# except ZeroDivisionError:
#     print("cannot divide by zero")

x = [0, 1, 2, 3, 4, 6, 7]


def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


# for i in generate_range(10):
#     print(f"i: {i}")

names = ["Alice", "Bob", "Charlie", "Debbie"]

# for i in range(len(names)):
#     print(f"name {i} is {names[i]}")

# for i, name in enumerate(names):
#     print(f"name {i} is {names[i]}")


my_best_friend = random.choice(names)
# print(my_best_friend)
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

zipped = [pair for pair in zip(list1, list2)]

letters, numbers = zip(*zipped)


def doubler(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g


def f1(x) -> int:
    return x + 1


g = doubler(f1)
assert g(3) == 8


def magic(*args, **kwargs):
    print("unnamed args", args)
    print("keyword args:", kwargs)


magic(1, 2, key="word", key2="word2")


def add(a: int, b: int) -> int:
    return a + b


print(add(10, 5))


def total(xs: List[float]) -> float:
    return sum(xs)


values: List[int] = []
best_so_far: Optional[float] = None

counts: Dict[str, int] = {'data': 1, 'science': 2}


def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)


def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)
