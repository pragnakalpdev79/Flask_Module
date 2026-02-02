import threading
import os
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
import sys

busy = threading.Lock() 
laod = True


def test(test):
    print("hello checking the lock",test)
    animation = "|/-\\"
    i = 0
    while busy.locked() == True:
        #print(f"waiting for task{test} to complete")
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        if i == len(animation)-1 :
            i = 0
        i += 1

    with busy:
        #reading data or writing data
        print(f"Doing Task {test}")
        print(test)
        time.sleep(20)
        #print(busy.locked())
        print("Task finished,db updated")


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(test,1)
    executor.submit(test,2)

print("end")