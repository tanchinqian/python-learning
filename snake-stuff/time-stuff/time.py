import datetime
today = datetime.date.today()
now = datetime.datetime.now()

target_datetime = datetime.datetime(2010 , 1 , 2, 12, 30 , 1)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
  print("We are in the future")
else:
  print("target date has not passed")