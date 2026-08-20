# 20 有效的括号 | 简单 | 考点：栈
# 核心思路：遍历字符串，左括号入栈；遇到右括号时与栈顶配对：
#   栈空（右括号多了）或不匹配 → False；遍历结束后栈非空（左括号多了）→ False
# 时间复杂度：O(n)，每个字符最多入栈/出栈一次
# 空间复杂度：O(n)，最坏情况全部是左括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')' : '(' , ']' : '[' , '}' : '{'}
        for w in s:
            if w in dic.values():
                stack.append(w)
            else:
                if not stack: #若栈为空
                    return False
                if dic[w] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack