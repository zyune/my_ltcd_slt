class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=int(len(nums)/2)
        dict={}
        for i in nums:
            if i in dict:
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        for i in dict:
            if dict[i] > n:
                return i
            else:
                continue