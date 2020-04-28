from unittest import TestCase

from src.my_queue import MyQueue


class TestQueue(TestCase):
    def setUp(self):
        self.my_queue = MyQueue()

    def test_queue(self):
        assert self.my_queue.queue == []
        self.my_queue.enqueue("One")
        assert self.my_queue.queue == ["One"]
        self.my_queue.enqueue("Two")
        assert self.my_queue.queue == ["One", "Two"]
        self.my_queue.enqueue("Three")
        assert self.my_queue.peek() == "One"
        assert self.my_queue.queue == ["One", "Two", "Three"]
        dequeued = self.my_queue.dequeue()
        assert dequeued == "One"
        assert self.my_queue.queue == ["Two", "Three"]