import datetime

today = datetime.datetime.now()
end = today - datetime.timedelta(weeks=1)
start_of_week = end - datetime.timedelta(days=end.weekday())
start = today.strftime('%Y-%m-%d')
end = end.strftime('%Y-%m-%d')

print(start)
print(end)