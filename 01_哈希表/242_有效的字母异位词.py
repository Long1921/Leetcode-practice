# 242 有效的字母异位词 | 简单 | 考点：哈希表
# 核心思路：长度不同直接 False；用 dict 统计 s 中每个字符出现次数，
#   遍历 t 逐个抵消（遇到陌生字符或次数对不上 → False），最后次数全部归零 → True
# 时间复杂度：O(n)，两次遍历字符串
# 空间复杂度：O(1)，字符最多 26 种，字典最多 26 个键
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1   # dic.get(i, 0)：键不存在时默认取 0
        for j in t:
            if j not in dic:
                return False
            dic[j] -= 1
        return all(v == 0 for v in dic.values())
