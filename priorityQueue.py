import queue

q = queue.PriorityQueue()

q.put((2, "Hello world!"))  #Dobbel parentes lager tuple
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get()[1])       #Get den som er på indeks 1
