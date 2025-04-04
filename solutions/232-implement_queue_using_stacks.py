# ID: 232
# Title: Implement Queue using Stacks
# Link: https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: Easy
# Tags: Stack, Design, Queue

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if not self.s2:
            self.s2.append(x)
            while self.s1:
                self.s2.append(self.sl.pop())
        else:
            self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        result = self.s2.pop()
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return result

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        return not (self.s1 or self.s2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
