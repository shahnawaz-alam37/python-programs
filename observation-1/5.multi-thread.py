import threading
import time

def worker1():
    for i in range(5):
        print("\nWorker 1: Performing task %d" % i)
        time.sleep(1)
def worker2():
    for i in range(5):
        print("\nWorker 2: Performing task %d" % i)
        time.sleep(1)

t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both workers have finished.")