class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,num in enumerate(nums):
            '''
            i是下标，num是数值
            '''
            j = target - num
            if j in a:
                return[a[j],i]
            a[num] = i