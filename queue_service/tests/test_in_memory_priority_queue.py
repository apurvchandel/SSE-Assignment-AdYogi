import unittest

import heapq

class InMemoryPriorityQueue:
    def __init__(self):
        self.queue = []
        self.count = 0  # To maintain order for FCFS

    def enqueue(self, request, priority):
        heapq.heappush(self.queue, (-priority, self.count, request))
        self.count += 1

    def dequeue(self):
        if not self.queue:
            return None
        return heapq.heappop(self.queue)[2]  # Return the request part of the tuple
    
class TestInMemoryPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = InMemoryPriorityQueue()

    def test_enqueue_dequeue(self):
        self.queue.enqueue("task1", 1)
        self.queue.enqueue("task2", 2)
        self.assertEqual(self.queue.dequeue(), "task2")  # Highest priority first
        self.assertEqual(self.queue.dequeue(), "task1")  # Next task

    def test_same_priority_fcfs(self):
        self.queue.enqueue("task1", 1)
        self.queue.enqueue("task2", 1)
        self.assertEqual(self.queue.dequeue(), "task1")  # FCFS order

if __name__ == '__main__':
    unittest.main()
