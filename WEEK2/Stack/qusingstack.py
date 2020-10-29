class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.queue == []:
            self.queue.append(x)
        else:
            self.queue.insert(0, x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0