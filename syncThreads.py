import threading
import time


x = 8192

def double():
    global x
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum")

def half():
    global x
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)


t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()
