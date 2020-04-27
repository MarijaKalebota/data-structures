from unittest import TestCase

from src.my_stack import MyStack


class TestStack(TestCase):
    def setUp(self):
        self.my_stack = MyStack()

    # integration test
    def test_stack(self):
        assert self.my_stack.stack == []
        self.my_stack.push("Element")
        assert self.my_stack.stack == ["Element"]
        assert self.my_stack.peek() == "Element"
        assert self.my_stack.stack == ["Element"]
        popped_element = self.my_stack.pop()
        assert popped_element == "Element"
        assert self.my_stack.stack == []
