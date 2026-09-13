import threading
import time

def task1( *args, **kwargs):
    time.sleep(4)
    print(f"Task 1 Finish {args[0]} {args[1]} {kwargs["joe"]}")
  
def task2():
    time.sleep(5)
    print("Task 2 Finish")

def task3():
    time.sleep(7)
    print("Task 3 Finish")

  
chore1 = threading.Thread(target=task1 , args=("joe","mama") , kwargs={"joe":"mama"} )
chore2 = threading.Thread(target=task2)
chore3 = threading.Thread(target=task3)


chore3.start()
chore2.start()
chore1.start()


chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")