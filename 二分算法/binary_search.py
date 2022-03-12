class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            pivot = left+(right-left)//2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot-1
            else:
                left = pivot+1
        return -1

    def search_recursion(self, left, right, nums, target):
        if(left > right):
            return -1
        # pivot = (left+right)//2
        pivot = left+(right-left)//2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            return self.search_recursion(pivot+1, right, nums, target)
        else:
            return self.search_recursion(left, pivot-1, nums, target)


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    right = len(nums)
    solution = Solution()
    print(solution.search_recursion(0, right, nums, target))
    # solution.search(nums, target)
