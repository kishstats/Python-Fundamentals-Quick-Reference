# Python Files

Reading, writing, and appending to files.

```python
# write 2 lines
with open('./files/myfile.txt', 'w') as f:
    f.write('this is the first line\n')
    f.write('this is the second line\n')

# read entire file
with open('./files/myfile.txt', 'r') as f:
    contents = f.read()
    print(contents)

# read single lines
with open('./files/myfile.txt', 'r') as f:
    line = f.readline()
    print("line: {}".format(line))
    line = f.readline()
    print("line: {}".format(line))

with open('./files/myfile.txt', 'r') as f:
    for line in f:
        # line = line.rstrip('\n')
        # rstrip() removes \f ,  \n , \r , \t , \v , \x and blank space
        # without having to pass in char as param
        line = line.rstrip()
        # print(line, end='\n') # error is rstrip removes line break
        print(line)

# ignore line breaks on output without stripping
with open('./files/myfile.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line)

# append to file
with open('./files/myfile.txt', 'a') as f:
    f.write('appending a 3rd line')
```
