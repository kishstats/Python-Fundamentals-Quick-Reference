# Python Error Handling

```python
def do_division(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        # print('ZeroDivisionError')
        return 0
    except TypeError:
        # print('TypeError')
        return 0
    finally:
        # print('excecuting finally clause')
        pass

result = do_division(10, 2)
print('result: {}'.format(result))  # result: 5

# ZeroDivisionError
result = do_division(10, 0)
print('result: {}'.format(result))  # result: 0

# TypeError
result = do_division('ten', 1)
print('result: {}'.format(result))  # result: 0

# still TypeError since TypeError triggers first
result = do_division('ten', 0)
print('result: {}'.format(result))  # result: 0        
```

## Examples with Logging
```python
import logging
from datetime import datetime

FORMAT_JSON = "{\"datetime\": \"%(asctime)s\", \"level\": \"%(levelname)s\", \"messsage\": \"%(message)s\"}"


# from logging tutorial
# for use in re-raising exceptions
def get_app_logger(name):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = name + '_' + date_str
    logging.basicConfig(level=logging.DEBUG,
                        format=FORMAT_JSON,
                        datefmt='%m/%d/%Y %H:%M:%S',
                        filename='./log/{}.log'.format(filename),
                        filemode='a')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    return logger


logger = get_app_logger('error_handling')

# NOTE: for demonstration only
# using a context manager (with) is recommended approach
# --- with open('./files/myfile.txt', 'w') as f:
# will handle closing the file automatically
try:
    f = open('./files/myfile.txt', 'w')
    f.write('testing')
except FileNotFoundError:
    print('file not found')
except Exception as e:
    logger.error('unknown exception: {}'.format(e.message))
    raise
finally:
    print('finally clause - closing file')
    try:
        f.close()
    except NameError as e:
        logger.error('name error: {}'.format(e))
        # re-raise error after logging
        raise
    except:
        print('unknown exception in finally clause')
```
