# Python Numbers

```python
my_num = 5
print(my_num)
print(type(my_num))

print(5+5) # 10
print(5-5) # 0
print(5*5)  # 25
print(5/5)  # 1.0
print(5**5) # 3125

div = 5/5
print(type(div)) # float in Python 3

div = int(5/5)
print(type(div)) # int

div = 5//5
print(div)  # 1
print(type(div)) # int  

num = 1.1
f = math.floor(num)
print("f: {}".format(f)) # 1
```

## Order of Operations

**PEMDAS**
- https://en.wikipedia.org/wiki/Order_of_operations
- (P)arentheses
- (E)xponent
- (M)ultiplication
- (D)ivision
- (A)ddition
- (S)ubtraction

```python
n = 1 + 4 * 4
print(n) # 17

n = (1 + 4) * 4
print(n) # 20

n = 1 + 4 * 4 ** 4
print(n) # 1025

n = (1 + 4 * 4) ** 4
print(n) # 83521
```

## Numeric Data Types

Floating Point Arithmetic
- What Every Computer Scientist Should Know About Floating-Point Arithmetic
  - http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
- http://floating-point-gui.de/basic/

Floating point numbers are an approximation.

Decimal: more accurate value than Float.

```python
from decimal import Decimal, getcontext

i = 5
print(type(i)) # int

f = 5.0  
print(type(f)) # float

print("float val: {}".format(float(i))) # float val: 5.0

f = 1/7
print(f) # 0.14285714285714285
print(type(f)) # float

getcontext().prec = 28
d = Decimal(f) # 0.142857142857142849212692681248881854116916656494140625
print(d)
print(type(d)) # <class 'decimal.Decimal'>

res = 0.1 + 0.1 + 0.1 - 0.3
print("res: {}".format(res)) # 5.551115123125783e-17
res = Decimal(0.1 + 0.1 + 0.1 - 0.3)
print("res: {}".format(res)) # 5.5511151231257827021181583404541015625E-17

```
