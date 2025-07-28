class FixedBoundedQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
        self.enqueued_count = 0  # counts total enqueues

    def enqueue(self, item):
        if self.enqueued_count < self.max_size:
            self.queue.append(item)
            self.enqueued_count += 1
        else:
            print("Queue is full!")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty!")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:", self.queue)

# Example:
q = FixedBoundedQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)  # Queue is full!
q.display()
q.dequeue()
q.display()
q.enqueue(4)  # Queue is full! (still)
