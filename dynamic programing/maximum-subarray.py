class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)

# 这没有自己调用自己 不是memorization
# 动态规划，tabulation这一步 在nums[i] = max(nums[i - 1] + nums[i], nums[i]) 实现了
