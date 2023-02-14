#Her kan vi endre på innholdet i text.txt, 
#og utskriften i daemon.py vil endres fortløpende (etter 3 sek)

import threading
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)


def printloop():
    for x in range(30): # Printer 30 ganger
        print(text)
        time.sleep(1) # Skrives ut hvert sekund

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
