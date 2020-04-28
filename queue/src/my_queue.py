class MyQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        dequeued = self.queue[0]
        self.queue = self.queue[1:]
        return dequeued

    def peek(self):
        return self.queue[0]
