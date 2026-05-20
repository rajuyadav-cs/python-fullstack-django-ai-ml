from datetime import (
    datetime,
    timedelta
)


# current datetime
now = datetime.now()

print(now)


# individual parts
print(now.year)

print(now.month)

print(now.day)

print(now.hour)

print(now.minute)

print(now.second)


# current date
print(now.date())


# current time
print(now.time())


# custom datetime
custom = datetime(
    2026,
    5,
    20,
    10,
    30
)

print(custom)


# formatting datetime
formatted = now.strftime(
    "%d-%m-%Y %H:%M:%S"
)

print(formatted)


# parsing string to datetime
date_string = "25-12-2026"

parsed = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(parsed)


# add time
future = now + timedelta(days=5)

print(future)


# subtract time
past = now - timedelta(days=2)

print(past)


# difference between dates
d1 = datetime(2026, 1, 1)

d2 = datetime(2026, 1, 10)

difference = d2 - d1

print(difference)

print(difference.days)


# timestamp
timestamp = now.timestamp()

print(timestamp)


# timestamp -> datetime
converted = datetime.fromtimestamp(
    timestamp
)

print(converted)


# comparisons
print(d1 < d2)

print(d1 > d2)


print("done")