# ID: 20
# Title: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses
# Difficulty: Easy
# Tags: Stack


def isValid(s: str) -> bool:
    """
    Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    """
    stack = []
    mapping = {"}": "{", ")": "(", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)
    return not stack
