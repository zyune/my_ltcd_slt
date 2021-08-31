class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)

#动态规划，memorize这一步 在nums[i] = max(nums[i - 1] + nums[i], nums[i]) 实现了