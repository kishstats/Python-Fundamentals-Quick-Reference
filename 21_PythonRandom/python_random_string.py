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

my_random = random_string(length=25, uppercase=False, lowercase=False)
print(my_random)
