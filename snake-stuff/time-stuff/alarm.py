import time
import datetime
import pygame
class AlarmTimeInThePastError(Exception):
  pass


def set_alarmtime(alarm_time):
  is_running = True
  try:
    current_check = datetime.datetime.now().strftime("%H:%M:%S")
    if current_check > alarm_time :
      raise AlarmTimeInThePastError("You cannot set an alarm in the past brochacho")
    
    print(f'Alarm time set for {alarm_time}')
    
    
    
    while is_running:
      current = datetime.datetime.now().strftime("%H:%M:%S")
      
      time.sleep(1)
      
      if current == alarm_time:
        print("WAKE UP!")
        is_running = False
      print(current)
      
  except AlarmTimeInThePastError as e: 
    print(f'{e}')


if __name__ == "__main__":
  alarm_time = input("Enter Your Alarm Target in (HH:MM:SS) : ")
  set_alarmtime(alarm_time)