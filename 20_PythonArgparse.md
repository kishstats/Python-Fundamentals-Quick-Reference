# Argparse

Parser for command-line options

**Start and End Dates example**
- start_date is required field
- end_date has a default (current date) if no end date gets passed in
```python
import argparse
from datetime import datetime


current_date = datetime.now()

parser = argparse.ArgumentParser(description='Get start and end dates')
parser.add_argument('-s', '--start_date', help='Start Date', required=True)
parser.add_argument('-e', '--end_date', help='End Date', default=current_date.strftime('%Y-%m-%d'))

# Example Usage
# python3 argparse_examples.py --start_date 2000-1-1 --end_date 2001-2-2
args = parser.parse_args()
print(args)  # Namespace(end_date='2001-2-2', start_date='2000-1-1')
print(args.start_date)  # 2001-2-2
print(args.end_date)  # 2000-1-1
```
---

**Add Example**
- nargs
  - number of arguments
  - can be a fixed number or use `+` operator (to gather into a list)
- dest (--sum argument)
  - accumulate
  - accumulate attribute will be either the sum() function, if --sum was specified at the command line, or the max() function
- action (--sum argument)
    - `store` is default
    - `store_const`
- type
  - require `int`
- metavar
  - compare with --help output
  - replaces argument name (integers)  
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print("args: {}".format(args))  # args: Namespace(accumulate=<built-in function sum>, integers=[2, 3, 1])
print(args.accumulate(args.integers))

# python argparse_add.py 1 2 3 4
# returns 4

# python argparse_add.py 1 2 3 4 --sum
# returns 10
```
---

**Add or Multiply example**
- uses mutually exclusive group (add or multiply)
```python
import argparse
from functools import reduce


def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)


parser = argparse.ArgumentParser(description='Process some integers.')
group = parser.add_mutually_exclusive_group()
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
group.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')
group.add_argument('--mult', dest='accumulate', action='store_const',
                   const=multiply, default=max,
                   help='multiply the integers (default: find the max)')


args = parser.parse_args()
print("args: {}".format(args))  # args: Namespace(accumulate=<built-in function sum>, integers=[2, 3, 1])
print(args.accumulate(args.integers))
```
