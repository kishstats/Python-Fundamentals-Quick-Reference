# Python Logging

*Basic Logging*
```python
import logging

FORMAT = '%(asctime)s %(levelname)-8s %(name)s %(message)s'
FORMAT_JSON = "{\"datetime\": \"%(asctime)s\", \"level\": \"%(levelname)s\", \"messsage\": \"%(message)s\"}"


logging.basicConfig(level=logging.DEBUG,
                    format=FORMAT_JSON,
                    datefmt='%m/%d/%Y %H:%M:%S',
                    filename='./log/myapp.log',
                    filemode='a')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.debug('this is a debug message')
logger.info('this is a debug message')
logger.warn("this is a warning message")
logger.error("this is an error message")

players = {
  'Giancarlo Stanton': {
    'position': 'right_field',
    'team': 'marlins',
    'ave': .281,
    'home_runs': 59,
    'rbi': 132
  },
  'Jose Altuve': {
    'position': 'second_base',
    'team': 'astros',
    'ave': .346,
    'home_runs': 24,
    'rbi': 81
  },
  'Nelson Cruz': {
    'position': 'right_field',
    'team': 'mariners',
    'ave': .288,
    'home_runs': 39,
    'rbi': 119
  }
}

logger.info("players: {}".format(players))
```

*Uses Custom Logger*
- creates log file for each date by name
```python
import logging
from datetime import datetime

FORMAT_JSON = "{\"datetime\": \"%(asctime)s\", \"level\": \"%(levelname)s\", \"messsage\": \"%(message)s\"}"


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


logger = get_app_logger('players')

logger.debug('this is a debug message')
logger.info('this is a debug message')
logger.warn("this is a warning message")
logger.error("this is an error message")

players = {
  'Giancarlo Stanton': {
    'position': 'right_field',
    'team': 'marlins',
    'ave': .281,
    'home_runs': 59,
    'rbi': 132
  },
  'Jose Altuve': {
    'position': 'second_base',
    'team': 'astros',
    'ave': .346,
    'home_runs': 24,
    'rbi': 81
  },
  'Nelson Cruz': {
    'position': 'right_field',
    'team': 'mariners',
    'ave': .288,
    'home_runs': 39,
    'rbi': 119
  }
}

logger.info("players: {}".format(players))
```
