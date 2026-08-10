class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for chars in zip(*strs):    # zip(*strs) 把字符串按"列"打包
            if len(set(chars)) == 1:
                #set(chars):把这一列变成集合,如果全相同,集合只有1个元素
                res += chars[0]
            else:
                break
        return res

''' 
   strs = ["flower", "flow", "flight"]
   zip(*strs) 会把每个字符串"按位置"拆开打包:
   第0列: ('f', 'f', 'f')   ← 三个字符串的第0个字符
   第1列: ('l', 'l', 'l')   ← 第1个字符
   第2列: ('o', 'o', 'i')   ← 第2个字符
   ...
 '''