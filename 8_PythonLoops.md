# Python Loops

```python
i = 1
while i < 10:
    print(i)
    i += 1

i = 1
while i <= 10:
    print(i)
    i += 1

players = ["frank thomas", "barry bonds", "cal ripken"]
for player in players:
    print(player)
# frank thomas
# barry bonds
# cal ripken


for player in sorted(players):
    print(player)
# barry bonds
# cal ripken
# frank thomas

# get index position while looping through list
for i, v in enumerate(players):
    print(i, v)
# 0 frank thomas
# 1 barry bonds
# 2 cal ripken

set1 = set([1, 2, 3])
for s in set1:
    print(s)

string = "my interesting string"
# will loop through every character
for s in string:
    print(s)

players = {
  'Giancarlo Stanton': {
    'position': 'right_field',
    'team': 'marlins',
    'ave': .281,
    'home_runs': 59,
    'rbi': 132
  },
  'Jose Altuve': {
    'position': 'second_base',
    'team': 'astros',
    'ave': .346,
    'home_runs': 24,
    'rbi': 81
  },
  'Nelson Cruz': {
    'position': 'right_field',
    'team': 'mariners',
    'ave': .288,
    'home_runs': 39,
    'rbi': 119
  }
}
for player in players:
    print(player)

for k, v in players.items():
    print(k, v)
    # loop through nested dictionary containing stats
    for key, val in v.items():
        print(key, val)
```
