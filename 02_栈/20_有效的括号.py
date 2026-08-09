class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[','}':'{'}
        for i in s:
            if i in dic.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                if dic[i] == stack[-1]:
                    stack.pop()
        return not stack