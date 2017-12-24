# Python Sets

A set contains an unordered collection of unique objects.

```python
set1 = set([1, 2, 3])
set2 = {4, 5, 6}

# no duplicates
set3 = {1, 2, 3, 3}
print(set3) # {1, 2, 3}

# membership
print(3 in set1) # True
print(3 in set2) # False

string_set = set('abcdef')
print(string_set) # {'a', 'c', 'f', 'd', 'b', 'e'}

combined = set1.union(set2)
print(combined) # {1, 2, 3, 4, 5, 6}

set1.update(set2)
print(set1) # {1, 2, 3, 4, 5, 6}

print(set1 == combined) # True

set1.add(7)
set1.remove(5)
print(set1) # {1, 2, 3, 4, 6, 7}

frozen = frozenset([1, 2])
# frozen.add(3) # throws AttributeError

```

## Set Operators

```python  
# operators  
a = set('abracadabra')
b = set('alacazam')

# difference: letters in a but not in b
print(a - b)
print(a.difference(b))
# {'r', 'd', 'b'}

# union: letters in a or b or both
print(a | b)
print(a.union(b))
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# intersection: letters in both a and b
print(a & b)
print(a.intersection(b))
# {'a', 'c'}

# xor: letters in a or b but not both
print(a ^ b)
print(a.symmetric_difference(b))
# {'r', 'd', 'b', 'm', 'z', 'l'}


c = set('dabra')
print(c.issubset(a)) # True  
print(c.issubset(b)) # False

print(a.issuperset(c)) # True
```
