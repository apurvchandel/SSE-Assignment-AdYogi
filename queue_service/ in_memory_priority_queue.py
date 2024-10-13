import heapq

class InMemoryPriorityQueue:
    def __init__(self):
        self.queue = []
        self.count = 0 

    def enqueue(self, request, priority):
        heapq.heappush(self.queue, (-priority, self.count, request))
        self.count += 1

    def dequeue(self):
        if not self.queue:
            return None
        return heapq.heappop(self.queue)[2]  
