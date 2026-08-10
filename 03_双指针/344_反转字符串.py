class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        for j in range(len(s)):
            '''
            改用while可以在两指针碰头时就停止循环
            1. 对撞指针模板:while left < right: 交换; left+=1; right-=1
            2. Python 切片反转:s[::-1](超常用,字符串也能用:"hello"[::-1] → "olleh")
            '''
            if i > j:
                s[i],s[j] = s[j],s[i]
                i -= 1