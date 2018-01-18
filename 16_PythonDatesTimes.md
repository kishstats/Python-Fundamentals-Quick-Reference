# Python Dates and Times

```python
from datetime import date, datetime, timedelta, timezone

current = datetime.now()
current_date = date.today()

print(current)
print(current_date)

specific_datetime = datetime(2011, 11, 12)
print(specific_datetime)  # 2011-11-12 00:00:00

specific_datetime = datetime(2011, 11, 12, 3, 1, 5)
print(specific_datetime)  # 2011-11-12 09:01:05

specific_date = date(2009, 1, 1)
print(specific_date)  # 2009-01-01

next_year = current_date + timedelta(days=365)
print(next_year)


# datetime from string
datetime_obj_from_str = datetime.strptime('1/1/2001', '%m/%d/%Y')
print(datetime_obj_from_str)  # 2001-01-01 00:00:00

datetime_obj_from_str = datetime.strptime('2005-05-09 12:00:00', '%Y-%m-%d %H:%M:%S')
print(datetime_obj_from_str)  # 2001-01-01 00:00:00


# get date and time objects from a datetime
s_date = specific_datetime.date()
print(type(s_date), s_date)  # <class 'datetime.date'> 2011-11-12
s_time = specific_datetime.time()
print(type(s_time), s_time)  # <class 'datetime.time'> 03:01:05

### instance methods ###
print("instance methods")
# format date to string
print(specific_datetime.strftime('%m/%d/%Y %H:%M:%S'))  # 11/12/2011 03:01:05
print("isoformat: {}".format(specific_datetime.isoformat()))  # isoformat: 2011-11-12T03:01:05

# zero-based where Monday is 0 and Sunday is 6
print(specific_datetime.weekday())  # 5
# 1-based where Monday is 1 and Sunday is 7
print(specific_datetime.isoweekday())  # 6
# 3-tuple, (ISO year, ISO week number, ISO weekday)
print(specific_datetime.isocalendar())  # (2011, 45, 6)

### Timedelta
year = timedelta(days=365)
print(year.total_seconds())  # 31536000.0

diff = next_year - current_date
print(type(diff), diff)  # <class 'datetime.timedelta'> 365 days, 0:00:00

# Time Zones
print("current tzinfo: {}".format(current.tzinfo))  # current tzinfo: None
current = current.replace(tzinfo=timezone.utc)
print("current tzinfo: {}".format(current.tzinfo))  # current tzinfo: UTC

# use replace method to modify date
specific_datetime = specific_datetime.replace(month=12, minute=15)
print(specific_datetime)  # 2011-12-12 03:15:05
```
