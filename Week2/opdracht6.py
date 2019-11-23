import heapq

class priorityQueue:

    def __init__(self):
        self.q = []

    def queue(self, v, p):
        heapq.heappush(self.q, (p, v))

    def dequeue(self):
        return heapq.heappop(self.q)

    def contains(self, v):
        for x in self.q:
            if x[1] == v:
                return True
        return False

    def remove(self, e):
        for i in range(0, len(self.q)-1):
            if e in self.q[i]:
                self.q.pop(i)


que = priorityQueue()
que.queue(9, 3)
que.queue(8, 2)
que.queue(5, 1)
que.queue(4, 8)
que.dequeue()
print(que.contains(8))
que.remove(8)
print(que.contains(8))
