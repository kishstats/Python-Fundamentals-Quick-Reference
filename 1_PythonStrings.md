# Python Strings

```python
statement = "take me out to the ballgame"
print(statement)

fname = "frank"
lname = "thomas"
print(fname)

fullname = fname + " " + lname
print(fullname)  # frank thomas

words = statement.split(" ")
print(words)  # ['take', 'me', 'out', 'to', 'the', 'ballgame']
for word in words:
  print(word)

slug = "-".join(statement.split(" "))
print(slug)  # take-me-out-to-the-ballgame

slug = "-".join(words)
print(slug)  # take-me-out-to-the-ballgame
```

## String Interpolation

Mulitple ways to format strings
  - %-formatting
  - str.format
  - string template

Continuing from example above:
```python
position = "first base"
print(type(position))  # <class 'str'>

sentence = f"{fname} {lname} played {position}"
print(sentence)  # frank thomas played first base

print("{} {} played {}".format(fname, lname, position))  # frank thomas played first base
print("%s %s played %s" % (fname, lname, position))  # frank thomas played first base
```

## Most Common String Methods

Continuing from previous example:
```python
### String Replace ###
# change position from first base to third base
sentence = sentence.replace("first", "third")
print(sentence)  # frank thomas played third base

# replaces all instances of
sentence = "the quick brown fox jumped over the lazy dog"
sentence = sentence.replace("lazy", "quick")
print(sentence)  # the quick brown fox jumped over the quick dog

# replaces all instances of quick by default
sentence = sentence.replace("quick", "slow")
print(sentence)  # the slow brown fox jumped over the slow dog

# replaces only first instance of quick
sentence = sentence.replace("quick", "slow", 1)
print(sentence)  # the slow brown fox jumped over the slow dog

length = len(sentence)
print(length)  # 43

career_home_runs = 521
print(type(career_home_runs))  # int

string_val = str(career_home_runs)
print(string_val)  # 521
print(type(string_val))  # str

# index method
sentence = "the quick brown fox jumped over the lazy dog"
idx = sentence.index('fox')
print(idx)  # 16

# slice
sliced = sentence[0:16]  # sliced = sentence[:16] will also work
print(sliced)  # the quick brown
length = len('fox')
sliced = sentence[0:idx+length]  # sliced = sentence[:idx+length] will also work
print(sliced)  # the quick brown fox

# upper and lower case
fname = fname[0].upper() + fname[1:].lower()
print(fname)  # Frank

all_upper = "ABCDEF"
all_lower = all_upper[:].lower()
print(all_lower)  # abcdef

backup_statement = statement
print(statement)
# will attempt to strip both left and right
stripped = statement.strip('me')  # take me out to the ballga
print(stripped)

# restore statement
statement = backup_statement
print(statement)
# left only
stripped = statement.lstrip('take me')  # out to the ballgame
print(stripped)

statement = backup_statement
print(statement.startswith('take me'))  # True
print(statement.endswith('take me'))  # False
print(statement.endswith('ballgame'))  # True

# Find method
print(statement.find('out'))  # 8
```
