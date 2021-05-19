from queue import PriorityQueue, Queue
# Normal Queue
q = Queue()
q.put(25)
q.put(18)
q.put(20)
print(q.get())

qq = Queue()
qq.put((4, 20))
qq.put(2, 33)
qq.put(5, 11)
qq.put(3, 12)
print(qq.get())

# Priority Queue
q1 = PriorityQueue()
q1.put(25)
q1.put(18)
q1.put(20)
print(q1.get())

qq1 = PriorityQueue()
qq1.put(4, 20)  # Priority And values
qq1.put(6, 10)
qq1.put(5, 11)
qq1.put(3, 12)
print(qq1.get())
