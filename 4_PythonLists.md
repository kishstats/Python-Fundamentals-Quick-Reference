# Python Lists

```python
players = ["frank thomas", "barry bonds", "cal ripken"]

# 0 index
print(players[0]) # frank thomas

count = len(players)
print("count: {}".format(count))

# last
print(players[len(players) - 1])
print(players[-1]) # negative index values count from the right

# loop through players
for player in players:
  print(player)

# add another
players.append("alex rodriguez")
print(players) # ['frank thomas', 'barry bonds', 'cal ripken', 'alex rodriguez']

# remove last item
players.pop()
print(players) # ['frank thomas', 'barry bonds', 'cal ripken']

players.reverse()
print(players) # ['cal ripken', 'barry bonds', 'frank thomas']

players.remove('cal ripken')
print(players) # ['barry bonds', 'frank thomas']

# delete by index value
del players[1]
print(players) # ['barry bonds']

players.extend(["cal ripken"])
print(players)

pitchers = ["greg maddux", "roger clemens"]

# for p in pitchers:
#   players.append(p)

# extend is more concise than the for loop
players.extend(pitchers)
print(players) # ['barry bonds', 'cal ripken', 'greg maddux', 'roger clemens']

# add a duplicate
players.append('roger clemens')
print(players)

count_roger = players.count('roger clemens')
print("roger clemens appears {} times".format(count_roger))

# remove method will one remove 1 instance
players.remove('roger clemens')

# reverse again
players.reverse()
print(players)

players.sort()
print(players) # ['barry bonds', 'cal ripken', 'greg maddux', 'roger clemens']

copy = players.copy()
print(copy) # ['barry bonds', 'cal ripken', 'greg maddux', 'roger clemens']

players.pop()
print(players) # ['barry bonds', 'cal ripken', 'greg maddux']
print(copy) # ['barry bonds', 'cal ripken', 'greg maddux', 'roger clemens']

# remove all
players.clear()
print(players) # []

# restore from copy
players = copy.copy()

print(players[0:2]) # ['barry bonds', 'cal ripken']
print(players[:2]) # ['barry bonds', 'cal ripken']

print(players[2:4]) # ['greg maddux', 'roger clemens']
print(players[2:]) # ['greg maddux', 'roger clemens']

numbers = [8, 6, 7, 5, 3, 0, 9]
numbers.sort()
print(numbers) # [0, 3, 5, 6, 7, 8, 9]

# a single list can contain multiple data types
complete_list = []
complete_list.extend(players)
complete_list.extend(numbers)
print(complete_list) # ['barry bonds', 'cal ripken', 'greg maddux', 'roger clemens', 0, 3, 5, 6, 7, 8, 9]

for item in complete_list:
  print(type(item))

# unable to sort when mixing strings and integers   
complete_list.sort()  # TypeError
```
