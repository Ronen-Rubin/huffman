class Stack:  # Stack will be a list of Nodes
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    def top(self):  # returns top Node by refrence
        if self.is_empty():
            raise ValueError("why you be like this?")
        return self.lst[-1]

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        if self.is_empty():
            raise ValueError("why you be like this?")
        return self.lst.pop()
