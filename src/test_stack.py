from .stack import Stack


def test_filo():
    stack = Stack()
    assert stack.is_empty()

    stack.push(1)
    assert stack.top() == 1

    stack.push(2)
    assert stack.top() == 2

    stack.pop()
    assert stack.top() == 1
