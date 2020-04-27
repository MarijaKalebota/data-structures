class MyStack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        popped_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return popped_element
