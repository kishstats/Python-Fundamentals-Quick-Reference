import random
from functools import reduce

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

check_accuracy = reduce((lambda x, y: x + y), outcomes.values())
print(check_accuracy) # should match the SIMULATIONS constant

# sort by outcome counts (dictionary values)
sorted_outcomes = dict(sorted(outcomes.items(), key=lambda x: x[1], reverse=True))

for item in sorted_outcomes.items():
    print(item)
    print('pct {}%'.format(round(item[1] / SIMULATIONS * 100, 1)))
    print('---')
