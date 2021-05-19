# Binary Heap:
# Properties of Binary heap
# 1.It should be complete binary tree

# There are 2 type of Heap tree

# 2. For Min heap---Root node of every subtree & tree should be min of it
# 3. For Max heap---Root node of every subtree & tree should be max of it


# from heapq import heappush, heappop, heapify, heappushpop
# Implement Binary Heap using heapq module in python

import heapq
nodes = [30, 20, 7, 8, 50, 9, 100, 40, 35]

heapq.heapify(nodes)  # Build Heap Tree
print(nodes)
print(heapq.heappop(nodes))  # Pop min of heap
print(heapq.nlargest(2, nodes))  # Return n largest Element
print(heapq.heappushpop(nodes, 10))  # Insert node and pop min
print(nodes)
print(heapq.heapreplace(nodes, 200))  # Pop min and insert node
print(nodes)
