# Python pytz and Arrow

## pytz

```python
from datetime import datetime
import pytz
from pprint import pprint


timezones = pytz.country_timezones.get('US')  # can also use all_timezones, common_timezones
pprint(timezones)
# ['America/New_York',
#  'America/Detroit',
#  'America/Kentucky/Louisville',
#  'America/Kentucky/Monticello',
#  'America/Indiana/Indianapolis',
#  ...
#  'Pacific/Honolulu']

pacific = pytz.timezone('America/Los_Angeles')
print(type(pacific), pacific)  # <class 'pytz.tzfile.America/Los_Angeles'> America/Los_Angeles

# localize a naive datetime
# safe for timezones without daylight saving transitions though, such as UTC:
local_date = pacific.localize(datetime.now())
print(type(local_date), local_date)  # <class 'datetime.datetime'> 2017-12-25 12:16:50.407873-08:00
print(local_date.tzinfo)  # America/Los_Angeles

local_date_no_tz = datetime.now()
print(local_date_no_tz, local_date_no_tz.tzinfo)  # 2017-12-25 12:17:45.625949 None

# NOTE: The preferred way of dealing with times is to always work in UTC, converting to localtime only when generating output to be read by humans. (http://pytz.sourceforge.net/#introduction)

utc_date = local_date.astimezone(pytz.utc)
print(utc_date, utc_date.tzinfo)  # 2017-12-25 20:30:16.775555+00:00 UTC
```

## Arrow

```python
import arrow

utc = arrow.utcnow()
print(type(utc), utc)  # 2017-12-25T20:39:06.184291+00:00

local = utc.to('US/Pacific')
print(local)  # 2017-12-25T12:46:15.199570-08:00
print(local.format())  # 2017-12-25 12:46:15-08:00
print(local.naive)   # 2017-12-25 12:46:15.199570
print(local.tzinfo)  # tzfile('/usr/share/zoneinfo/US/Pacific') ## Path to binary file

dt = arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
print(type(dt))  # <class 'arrow.arrow.Arrow'>
# convert to python datetime
dt_obj = arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss').datetime
print(type(dt_obj))  # <class 'datetime.datetime'>

isodate = "2011-11-12T03:01:05"
print(arrow.get(isodate))  # 2011-11-12T03:01:05+00:00

print(local.timestamp)  # 1514234702
print(local.date())  # 2017-12-25
print(local.time())  # 12:48:20.752394
# see Arrow formatting codes: http://arrow.readthedocs.io/en/latest/#tokens
print(local.format('MM/DD/YYYY HH:mm:ss'))  # 12/25/2017 12:50:05
print(local.humanize())  # just now

print(local.floor('hour'))  # 2017-12-25T12:00:00-08:00
print(local.ceil('hour'))  # 2017-12-25T12:59:59.999999-08:00

# add and subtract using shift method
later_on = local.shift(hours=3)  # 2017-12-25T15:59:22.577283-08:00
print(later_on)

# iterating through a range
start = arrow.Arrow(2013, 5, 5, 12, 30)
end = arrow.Arrow(2013, 5, 5, 17, 15)
for hourly in arrow.Arrow.span_range('hour', start, end):
    print(hourly)
```
