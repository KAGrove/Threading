import threading

def function1():
    for x in range(10):
        print("ONE")

def function2():
    for x in range(10):
        print("TWO")


t1 = threading.Thread(target=function1)

t2 = threading.Thread(target=function2)

t1.start()
t2.start()

t1.join()	# Den under venter på at t1 er ferdig (ikke t2)
		# Hm, t2 gjør seg også ferdig før teksten under
print("Another text")
