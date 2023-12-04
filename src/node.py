from stack import Stack


class Node:  # (object):
    # count = 0 #property of class not object
    def __init__(
        self, src_symbol, freq, left=None, right=None
    ):  # __magic method__ because all object have this method, we are overriding.
        self.src_symbol = src_symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.enc_symbol = ""
        # Node.count += 1
        # e.g: self.sum = self.left + self.right

    # def __str__(self):
    #     return f'({self.src_symbol} , {self.freq})' #'('self.src_symbol + ',' + str(self.freq) ')'
    def __repr__(self):
        return f"({self.src_symbol} , {self.freq}, {self.enc_symbol})"  #'('self.src_symbol + ',' + str(self.freq) ')'

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return (
            isinstance(other, Node) and self.freq == other.freq
        )  # order matters with the and

    def is_leaf(self):
        return (self.left == None) and (self.right == None)

    def dfs_encode(self):
        stack = Stack()
        leaves = []
        stack.push(self)

        while not stack.is_empty():
            popped_node = stack.pop()  # popped_node will be what was the top Node

            if popped_node.is_leaf():
                leaves.append(popped_node)

            if popped_node.right:
                popped_node.right.enc_symbol = popped_node.enc_symbol + "1"
                stack.push(popped_node.right)

            if popped_node.left:
                popped_node.left.enc_symbol = popped_node.enc_symbol + "0"
                stack.push(popped_node.left)

        return leaves

    # @staticmethod #decorator is a function that takes a function and modifies it.
    # def get_count():
    #     return Node.count
