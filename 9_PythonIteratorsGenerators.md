# Python Iterators and Generators

```python
import string
from functools import reduce

players = ["frank thomas", "barry bonds", "cal ripken"]
iterator = iter(players)

print(iterator)
print(next(iterator))   # frank thomas
print(next(iterator))   # barry bonds
print(next(iterator))   # cal ripken
# print(next(iterator))   # StopIteration error


def counter(start, end):
    print("inside counter function")
    while start <= end:
        yield start
        start += 1


# when you call the function, the code you have written inside the function
# body does NOT actually run
print(counter(5, 10))
print('---')

for i in counter(5, 10):
    print(i)

print(type(counter(1, 10)))   # <class 'generator'>


def letter_generator():
    for l in string.ascii_uppercase:
        yield l


for l in letter_generator():
    print(l)


# Generator Expressions
n = sum(x*x for x in range(10))
print(n)    # 285

# can also use a list to get same result
# generators use less memory and resources
n = sum([x*x for x in range(10)])
print(n)    # 285


def double_it(n):
    return n * 2


# MAP function
numbers = [1, 2, 3, 4]
doubles = list(map(double_it, numbers))
print(doubles)  # [2, 4, 6, 8]
doubles = list(map(lambda x: x*2, numbers))
print(doubles)  # [2, 4, 6, 8]


def get_slugging_pct(total_bases, at_bats):
    return round(total_bases / at_bats, 3)


def map_player(player_tuple):
    print("map_player: {}".format(player_tuple))
    player_dict = player_tuple[1]

    player_dict['slg'] = get_slugging_pct(player_dict['total_bases'],
                                          player_dict['at_bats'])
    return player_tuple


players = {
    'Giancarlo Stanton': {
        'position': 'right_field',
        'team': 'marlins',
        'ave': .281,
        'home_runs': 59,
        'rbi': 132,
        'hits': 168,
        'at_bats': 597,
        'total_bases': 377
    },
    'Jose Altuve': {
        'position': 'second_base',
        'team': 'astros',
        'ave': .346,
        'home_runs': 24,
        'rbi': 81,
        'hits': 204,
        'at_bats': 590,
        'total_bases': 323
    },
    'Nelson Cruz': {
        'position': 'right_field',
        'team': 'mariners',
        'ave': .288,
        'home_runs': 39,
        'rbi': 119,
        'hits': 160,
        'at_bats': 556,
        'total_bases': 305
    }
}

players = dict(map(map_player, players.items()))
print(players)


# Filter
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce
# returns a single result
result = reduce(lambda x, y: x + y, numbers)  # 1 + 2 + 3 + 4
print(result)  # 10

result = reduce(lambda x, y: x * y, numbers)  # 1 * 2 * 3 * 4
print(result)  # 24

players = ["frank thomas", "barry bonds", "cal ripken"]
longest_string = reduce(lambda x, y: x if len(x) >= len(y) else y, players)
print(longest_string)  # frank thomas

```
