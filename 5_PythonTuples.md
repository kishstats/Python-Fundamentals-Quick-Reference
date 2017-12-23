# Python Tuples

```python
players = ('sammy sosa', 'frank thomas', 'barry bonds')

print(players[0]) # sammy sosa

# parentheses are optional
numbers = (1, 2, 3)
more = 4, 5, 6

combined = numbers, more
print(combined) # ((1, 2, 3), (4, 5, 6))

concat = numbers + more  
print(concat) # (1, 2, 3, 4, 5, 6)

# comparison
print(combined[0]) # (1, 2, 3)
print(type(combined[0])) # tuple
print(concat[0]) # 1
print(type(concat[0])) # int  

# Tuples are immutable and have fixed length
# players[0] = "cal ripken" # throws TypeError

empty_tuple = ()  
print(type(empty_tuple)) # <class 'tuple'>
print(empty_tuple) # ()

one_item = ('hello',)
print(one_item) # ('hello',)

# returns tuple
def get_stats(hits, at_bats, total_bases):
  ave = hits / at_bats
  slg = total_bases / at_bats
  return round(ave, 3), round(slg, 3)

stats = get_stats(174, 549, 333) # (0.317, 0.607)
print(stats)

ave, slg = get_stats(174, 549, 333)
print(ave) # 0.317
print(type(ave)) # <class 'float'>

# convert list to tuple
num_list = [7, 8, 9]
converted = tuple(num_list)
print(converted) # (7, 8, 9)

# unpack  
seven, eight, nine = converted
print(seven) # 7
```
