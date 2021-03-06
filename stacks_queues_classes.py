class Stack(object):
    """stack implemented using a list"""

    def __init__(self):
        self._stack = []

    def push(self, item):
        """add item to the top"""

        self._stack.append(item)

    def pop(self):
        """remove top item"""

        return self._stack.pop()

    def peek(self):
        """return, but don't remove, top item"""

        return self._stack[-1]

    def is_empty(self):
        """is the stack empty?"""

        return not self._stack


class Queue(object):
    """queue implemented using a list"""

    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        """add item to the end"""
        self._queue.append(item)

    def dequeue(self, item):
        """remove from the front"""

        del self._queue[0]

    def peek(self):
        """return, but don't remove, beginning item"""

        return self._queue[0]

    def is_empty(self):
        """is the queue empty?"""

        return not self._queue


class Node(object):
    """Node in a Linked List"""

    def __init__(self, data):
        self.data = data
        self.next = None












