# Python File System

```python
import os
import random
import shutil

current = os.getcwd()
print(current)

# change directories
os.chdir('/Users/brettkishkis/Documents')
current = os.getcwd()
print(current)

# list files and folders
print(os.listdir())

# make new directory
# os.mkdir('new')

os.listdir()

os.rename('new', 'all_years')
os.chdir('./all_years')
print("switeched to: {}".format(os.getcwd()))

# add file
open('myfile.txt', 'w').close()

# remove file
os.remove('file.txt')

# remove directory
# os.rmdir('newbie')


def create_directories():
    for i in range(1900, 2017):
        os.mkdir(str(i))

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]


def create_sentence():
    return random.choice(s_nouns) + ' ' + random.choice(s_verbs) + ' ' + random.choice(s_nouns).lower() or random.choice(p_nouns).lower() + ' ' + random.choice(infinitives)


def get_filename():
    return str(random.getrandbits(128)) + '.txt'


def create_random_files(_dir):
    for subdir, dirs, files in os.walk(_dir):
        for i in range(random.randint(1, 10)):
            new_file = get_filename()
            print(new_file)
            with open(subdir + '/' + new_file, 'w') as f:
                f.write(create_sentence())


def list_files(_dir):
    r = []
    for subdir, dirs, files in os.walk(_dir):
        for name in files:
            r.append(os.path.join(subdir, name))
    return r


def search(term, _dir):
    matches = []
    files = list_files(_dir)
    for f in files:
        with open(f, 'r') as ff:
            contents = ff.read()
            if term in contents:
                matches.append(contents)
    return matches


def remove_all(_dir):
    shutil.rmtree(_dir)  # Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory)


create_directories()
create_random_files(os.getcwd())

file_list = list_files(os.getcwd())
for f in file_list:
   print(f)

matches = search('king', os.getcwd())
for m in matches:
    print(m)

remove_all(os.getcwd())
```
