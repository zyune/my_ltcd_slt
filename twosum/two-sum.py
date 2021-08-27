class Solution:
    
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
    def bruteForcetwoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): 
                # DOn't have to worry about the duplicate here,  
                #becasue range(i+1,len(nums)) is always one further than range(len(nums))
                if nums[i] + nums[j] == target:
                    return[i,j]
    
    
    def cccc(self, nums, target):
        c=dict()                        # c is a dictionary,in this dictionary 
                                        #{'complement1': <index of list>, 'complement2': <index of list>}
        for i in range(len(nums)):
            complement=target - nums[i]
            if nums[i]in c:
                return [nums.index(complement),i]
            else:
                c[complement]=i
                
a = Solution()
a.cccc([2,7,11,15], 26)



