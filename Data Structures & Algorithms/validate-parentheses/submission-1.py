class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for i in s:
            if i in pair:
                stack.append(i)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if i != pair[prev]:
                    return False
        return len(stack) == 0
        