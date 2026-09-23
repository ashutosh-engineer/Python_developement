# import threading
# from threading import Thread
# import time

# def threadfunc():
#     print("Hello")
#     time.sleep(5)
#     print("Completed")

# thrd= Thread(target= threadfunc)
# thrd.start()
# thrd.join()

# print(threading.active_count())  
#To print active counts;

# This is about thread---------------------------
# GIL ROLE (Global Interpretor lock)
#Global interpreter locks says that you can create
# Multiple threds But you can execute only one at once
# NOt more than that;


# def print_name():
#     print("Ashutosh")

# kill_thread=False
# def createThreads():
#     time.sleep(5)
#     print("Nashutosh 1")
#     while kill_thread == True:
#         return

# thread1=Thread(target =print_name)
# thread2=Thread(target= createThreads)
# thread1.start()
# thread2.start() 


# print(threading.active_count())
# It is also an thread;
'''
Here after executing the thread 1 python 
executes thread2 but when 5 sleep clicks insteead 
of wait8ing it executes the Print statement and then 
Ends the second thread;

-It also proves that - in Cpython only Youcannot execute two thread paralley
Because of Global Interpretor locks
'''


# Startting with th emultiprocesssing in the python
import multiprocessing as mp
from multiprocessing import Process

'''
While creating multiple Processes there will be no GIL
in Between
'''

# Multiprocessing is that where multiple process can run simultaneously
def creat_pro():
    print("This is new Process")
    print("The process name is :", mp.current_process())


p1=Process(target=creat_pro)
