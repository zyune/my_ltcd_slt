class Solution(object):
    def findPeakElement_iteration(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low < high:   # 这个地方一定不能用<=  这样的话循环不出来
            midindex = int((low+high)/2)
            current = nums[midindex]
            if current > nums[midindex+1]:
                high = midindex
            else:
                low = midindex+1
        return low


def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def search(nums, low, high):
        print("low is ", low)
        print("high is", high)
        if low == high:
            print("now low==high low is", low)
            return low
        midindex = (low+high)//2
        if nums[midindex] > nums[midindex+1]:
            return search(nums, low, midindex)
        else:
            return search(nums, midindex+1, high)
    search(nums, 0, len(nums)-1)


list = [1, 2, 3, 1]
print(findPeakElement(list))
