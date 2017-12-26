# Python Dictionaries

```python
# multiple ways to initialize a dictionary
d = {'a': 1, 'b', 2, 'c': 3}
d = dict(a=1, b=2, c=3)
print(d) # {'a': 1, 'b': 2, 'c': 3} always prints using brackets
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
d = dict([('a', 1), ('b', 2), ('c', 3)])

print(d['a']) # 1

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

print(players['Jose Altuve']) # {'position': 'second_base', 'team': 'astros', 'ave': 0.346, 'home_runs': 24, 'rbi': 81}
print(players['Jose Altuve']['position']) # second_base

# print(players['jose altuve']) # KeyError (keys are case-sensitive)

players['Mike Trout'] = {
  'position': 'center_field',
  'team': 'angels',
  'ave': .306,
  'home_runs': 33,
  'rbi': 72
}

print(players) # dictionary of all players
print('---') # create some separation
print(players['Mike Trout']) # {'position': 'center_field', 'team': 'angels', 'ave': 0.306, 'home_runs': 33, 'rbi': 72}
print('---')

players_list = [p for p in players.items()]
print(players_list)
print('---')
print(players_list[0]) # ('Giancarlo Stanton', {'position': 'right_field', 'team': 'marlins', 'ave': 0.281, 'home_runs': 59, 'rbi': 132})
print(type(players_list[0])) # tuple
# name
print(players_list[0][0]) # Giancarlo Stanton
# nested dictionary info
print(players_list[0][1]) # {'position': 'right_field', 'team': 'marlins', 'ave': 0.281, 'home_runs': 59, 'rbi': 132}

names_list = [p for p in players.keys()]
print(names_list) # ['Giancarlo Stanton', 'Jose Altuve', 'Nelson Cruz', 'Mike Trout']

del players['Jose Altuve']
names_list = [p for p in players.keys()]
print(names_list) # ['Giancarlo Stanton', 'Nelson Cruz', 'Mike Trout']

print('Jose Altuve' in players) # False
print('Nelson Cruz' in players) # True

# update
default_payer = {
  'position': None,
  'team': None,
  'ave': None,
  'home_runs': None,
  'rbi': None
}

rookie = {
  'position': 'shortstop',
  'team': 'yankees'
}

joe_rookie = default_payer
joe_rookie.update(rookie)
print(joe_rookie)
```
