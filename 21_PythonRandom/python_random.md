# Python Random Module

The Python random module has a variety of uses. You can do many different things that include simulations, getting a random number, picking an item from a list, generating data for unit tests, and generating data for load tests. Pretty much everyone will run into a use for random data at some points.

## Random Method

The random module has a built-in `random` method that will return a value between 0 and 1. Alternatively, you can call the `uniform` method to get a float value between two values of you're choosing:

```python
import random

# returns a float value between 0 and 1
print(random.random())

# returns a float value between 100 and 200
print(random.uniform(100, 200))
```

## Random Ranges for Integers

The random `randrange` method allows you to set boundaries so you can limit what range a value will fall into. When a single parameter is passed in, it will return any value between 0 and the parameter value.

Alternatively, you can pass in 2 parameters for a lower bound and upper bound limit. An optional third parameter for a step value is available. Passing in a step value of 2 will only return even numbers. A step of 5, on the other hand, will return only value ending in 5 or 0.

```python
import random

# randrange with an upper limit
random.randrange(1000)

# randrange with a lower and upper limit
random.randrange(100, 200)

# any random int between 2 values
# equivalent to randrange(a, b+1)
random.randint(100, 200)

# randrange with a lower and upper limit with a step value
# will only return even numbers
random.randrange(100, 200, 2)

# a step of 5
# any result will end in either 5 or 0
random.randrange(100, 200, 5)
```

## Random Functions for Sequences

In this section, the `choice` method can be used with any data that consists of a sequence. This can be a list, tuple, or even a string. Within a string, each character will count for a single item in the sequence.

```python
import random

number_list = [1, 2, 3, 4, 5]
number_tuple = (1, 2, 3, 4, 5)
number_string = 'abcdef'

print(random.choice(number_list)) # returns any item in the list
print(random.choice(number_tuple)) # returns any item in the tuple
print(random.choice(number_string)) # returns any character in the string
```

### Random Shuffling and Sampling

Randomly rearranging the order of a sequence is very easy. The `shuffle` method will handle this for you. The `shuffle` method happens in place, meaning that there a new sequence will not be returned. Our original variable will be mutated.

If we want to return a new sequence and leave the original variable alone, there are a couple of options: the `sample` method, generating a sample that's the same size as the original variable. Or, the built-in `sorted` method using the `random` method as the sorting function.

Sampling is relatively straightforward. The `sample` method can be used by taking the sequence as the first parameter with the sample size being the second parameter.

```python
import random

number_list = [1, 2, 3, 4, 5]
number_tuple = (1, 2, 3, 4, 5)
number_string = 'abcdef'


random.shuffle(number_list) # shuffling happens in place, method will return None
# now, we can print our new value
print(number_list)

# resetting our values
number_list = [1, 2, 3, 4, 5]
# create new shuffled list
# all values will be shuffled because the length matches the length of the list
shuffled = random.sample(number_list, len(number_list))


number_list = [1, 2, 3, 4, 5]
# sorted method provides another alternative
shuffled = sorted(number_list, key=lambda x: random.random())

number_list = [1, 2, 3, 4, 5]
# get a sample of any 3 values
sample = random.sample(number_list, 3)
```

## Random Strings

Generating random strings can be done with the help of the `string` module. This allows us to import character sets where we can select random data from. In this first example, we'll set a default of 32 characters. The characters in which we will be selecting random choices from are going to include any upper or lower case character, along with any number between 0 and 9. Similar to the sequence examples described earlier, the `choice` method can be used with a `range` to concatenate a string of random characters.

```python
import random
import string

def random_string(length=32):
    # string.ascii_letters same as string.ascii_uppercase + string.ascii_lowercase
    character_set = string.ascii_letters + string.digits
    return ''.join(random.choice(character_set) for i in range(length))

my_random = random_string()  # oyKR3MwyzcWpVT42wFUJTYYlYxbZRC09
```

To make our `random_string` function more flexible, we can allow parameters to choose whether we want uppercase, lowercase, and numbers to be included. We will use keyword parameters so we can have defaults that will include everything. We simply start with an empty string and add any characters pass the boolean parameter values.

```python
import random
import string


def random_string(length=32, uppercase=True, lowercase=True, numbers=True):
    character_set = ''

    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits

    return ''.join(random.choice(character_set) for i in range(length))

my_random = random_string(length=25, uppercase=False, lowercase=False)  # 8210504801539685297626160
```

Above: if we don't pass in any additional parameters, the result would be the same as before. However, if we wanted to generate a random sequence of numbers, we can set uppercase and lowercase to false.

One of the more important uses for generating random values is simulations. Simulations themselves have a variety of uses. You may need to do a load test in terms of how much traffic your website can handle. You also may want to speed up the cause and effect of a tedious task. For example, let's imagine you need to better understand how dropping grains of sand on a pile will trigger an avalanche (see [Abelian Sandpile Model](https://en.wikipedia.org/wiki/Abelian_sandpile_model)). It would be an extremely long and boring task to actually go out and do this. Instead, you can use a computer simulation dropping one grain of sand on top of another. And, repeat it as many times as you wish.

For now, we're going to try tackling a simpler task. In the next section, we will create a simulation for rolling dice.

## Dice Simulation

In this section, we will use random values to simulate throwing a set of dice. Since two dice get thrown at once, the smallest possible outcome is "snake eyes", or 2. This is simply because each die ranges from 1 to 6. This is also reflected in the fact that the maximum possible outcome is 12.

With that in mind, we can go ahead and setup our simulation. We will create a constant for the number of simulations that we will do.

```python
SIMULATIONS = 1000

possible_values = list(range(2, 13))
```

In the example above, we've also setup a list of possible values. Since 2 is the minimum value, we passed that into the built-in `range` function. We also passed in 13 as our stop value. The reason for using 13 is because the range index values are 0-based and the stop value is not inclusive.

In our simulation, it will be necessary to keep track of each outcome as we iterate through each simulation. Setting up a dictionary can handle that.

```python
SIMULATIONS = 1000

possible_values = list(range(2, 13))

# create a dictionary of the outcomes
# start each possible outcome with an initial value of 0
outcomes = {i: 0 for i in possible_values}
```

Our outcomes dictionary sets up each possible outcome with an initial value of 0:

```python
{2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
```

The next step will be to setup another range to actually do our simulations. We will setup 2 variables: 1 for each die. Calculating an individual outcome will simply require adding the the values of the dice. The final step will consist of incrementing the outcome value to our `outcomes` dictionary.

```python
import random

SIMULATIONS = 1000

possible_values = list(range(2, 13))

# create a dictionary of the outcomes
# start each possible outcome with an initial value of 0
outcomes = {i: 0 for i in possible_values}

for i in range(SIMULATIONS):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    outcome = d1 + d2
    outcomes[outcome] += 1

print(outcomes)
```

Running the script will return a distribution like the following:

```python
{2: 28, 3: 50, 4: 92, 5: 120, 6: 141, 7: 156, 8: 154, 9: 106, 10: 74, 11: 58, 12: 21}
```

On the surface, this appears normal. For example, outcomes of 6 and 7 should happen more often than 2 or 12. This is due to the simple fact that there are multiple combinations that would result in a 6 or a 7. And, only one way to roll a 2 or a 12.

If we want to verify that we have 1,000 simulations, we can use the `reduce` function to get a count of all the values for each outcome.

We will need to import `reduce` from `functools`, which is a module that's available from the Python standard library.

```python
import random
from functools import reduce

...

check_accuracy = reduce((lambda x, y: x + y), outcomes.values())
print(check_accuracy) # should match the SIMULATIONS constant
```

Above: inside the `reduce` function, we pass in a lambda function as the first argument. The second argument entails the sequence we will be iterating through. Which, in this case, are the outcomes from our results dictionary. As it iterates, it will add the next value `y` to the accumulated value `x`. When calling `reduce`, the result will be a single value.

One final thing we can do is sort the outcomes based on the totals. The built-in `sorted` method can help us accomplish the task:

```python
...

# sort by outcome counts (dictionary values)
sorted_outcomes = dict(sorted(outcomes.items(), key=lambda x: x[1], reverse=True))

for item in sorted_outcomes.items():
    print(item)
    print('pct {}%'.format(round(item[1] / SIMULATIONS * 100, 1)))
    print('---')
```

Above: `outcome.items()` returns a type of `dict_items`, thus resulting in the need to convert the sorted outcomes back to a dictionary. By default, sorting will sort from the lowest values to the highest. In our situation we want to sort from highest to lowest (the outcomes with the highest frequencies to be at the top). Setting the `reverse` parameter to `True` will accomplish that.

Finally, the very last thing we did was iterate through the sorted outcomes and printed out a percentage of the total for each outcome.

Here is an example of the final results. Obviously, each result will vary slightly. However, 5 through 9 should consistently appear at the top of the list.

Random Outcome:
```
(7, 179)
pct 17.9%
---
(8, 157)
pct 15.7%
---
(6, 122)
pct 12.2%
---
(9, 119)
pct 11.9%
---
(5, 105)
pct 10.5%

```

Dice simulation source code: https://github.com/kishstats/Python-Fundamentals-Quick-Reference/blob/master/21_PythonRandom/python_random_dice.py
