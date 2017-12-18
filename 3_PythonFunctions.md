# Python Functions

```python
def get_full_name(first, last):
    name = first + " " + last
    return name


fname = "frank"
lname = "thomas"

fullname = get_full_name(fname, lname)
print(fullname)     # "frank thomas"


def get_words_from_statement(sentence_string):
    return sentence_string.split(' ')


statement = "take me out to the ballgame"
words = get_words_from_statement(statement)
print(words)


def capitalize(s):
    if len(s) == 0:
        return ""
    else:
        return s[0].upper() + s[1:].lower()


def ucwords(w):
    lyst = w.split(' ')
    return " ".join(capitalize(w) for w in lyst if w != '')


# passing in a default parameter
def player_position(_fullname, position=None):
    if position:
        return "{} plays {}".format(ucwords(_fullname), position)
    else:
        return "Not sure what position {} plays.".format(ucwords(_fullname))


pos = player_position(fullname)
print(pos) # Not sure what position Frank Thomas plays.

pos = player_position(fullname, "first base")
print(pos) # Frank Thomas plays first base


def get_batting_ave(hits, at_bats):
  return round(hits / at_bats, 3)

batting_ave = get_batting_ave(174, 549)
print("batting ave: {}".format(batting_ave)) # 0.317


# variable-length argument list
def create_sentence(delim, *_words):
  print(type(_words)) # tuple
  return delim.join(_words)

print(words)    
s = create_sentence(" ", 'take', 'me', 'out', 'to', 'the', 'ballgame')
print(s) # take me out to the ballgame

slug = create_sentence("-", 'take', 'me', 'out', 'to', 'the', 'ballgame')
print(slug) # take-me-out-to-the-ballgame

def _create_sentence(delim, **_words):
  print(_words) # {'word1': 'take', 'word2': 'me'}
  print(type(_words)) # dictionary  
  lyst = [_words[key] for i, key in enumerate(_words.keys())]
  print(lyst) # ['take', 'me']
  return delim.join(lyst)


s = _create_sentence(" ", word1='take', word2='me')
print(s) # take me

slug = _create_sentence("-", word1='take', word2='me')
print(slug) # take-me

```

## Other Functions

```python
# nested functions
def incrementer(n):
  def actually_increment(x, n=n):
    return x + n
  return actually_increment

add_another = incrementer(1)
print(type(add_another)) # function
print(add_another(2)) # 3

add_even = incrementer(2)
print(add_even(2)) # 4

# lambda expressions
def _incrementer(n):
  return lambda x: x + n

add_one = _incrementer(1)
print(add_one(2)) # 3

add_even = _incrementer(2)
print(add_even(2)) # 4

another_full_name = lambda x, y: capitalize(x) + " " + capitalize(y)
print(type(another_full_name)) # function
name = another_full_name(fname, lname)
print(name) # Frank Thomas

```
