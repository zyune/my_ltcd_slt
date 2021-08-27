class Solution:
   
#有必要自己去看一下range的用法
#python的长度是len（）
#you时候 两个东西一个前移动 一个不移动 移动的那个for函数就已经帮实现了 不用在else里面写
#核心 快慢指针
   
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow=0
            for fast in range(1,len(nums)): 
                if nums[fast]!=nums[slow]: 
                    slow=slow+1
                    nums[slow]=nums[fast]
            return slow+1
                    
        else:
            return 0