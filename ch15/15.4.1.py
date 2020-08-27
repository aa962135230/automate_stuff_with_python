import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta)
print(delta.total_seconds())
print(str(delta))

dt = datetime.datetime.now()
print(dt)
thousand_days =  datetime.timedelta(days=1000)
print(dt + thousand_days)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
about_thirty_years = datetime.timedelta(days=365 * 30)

print(oct21st)
print(oct21st - about_thirty_years)
print(oct21st - (2*about_thirty_years))