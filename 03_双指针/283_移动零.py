class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        i负责寻找非零位置；j负责记录零位置
        '''
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                '''
                交换数组元素
                '''
                j += 1