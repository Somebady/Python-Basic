from queue import PriorityQueue, Queue
q = PriorityQueue()
q.put(25)
q.put(18)
q.put(20)
print(q.get())

qq = Queue()
qq.put((4, 2))
qq.put(2, 33)
qq.put(5, 11)
qq.put(3, 12)
print(qq.get())
