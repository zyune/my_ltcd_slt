class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        left = 0
        right = len(nums)-1
        mid = left+(right-left)//2
        while left < right:
            if nums[mid] == target:
                return [mid, right]
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return [-1, -1]
