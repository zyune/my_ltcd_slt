# my_ltcd_slt
my leetcode solution
2021 Aug 27th
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
#有必要自己去看一下range的用法
#python的长度是len（）
#you时候 两个东西一个前移动 一个不移动 移动的那个for函数就已经帮实现了 不用在else里面写
#核心方法是使用快慢指针
https://leetcode-cn.com/problems/roman-to-integer/
<img width="707" alt="Screen Shot 2021-08-28 at 12 42 16 AM" src="https://user-images.githubusercontent.com/66234261/131160845-44d8f836-f89e-475c-8a9c-ef03d2dac1db.png">

2021 Aug 31th
so the key thing about memorization in dynamic programming is that we need to follow the following steps 
1. make it work  // this step is the hard part
   visualize the problem as a tree 
   implement the tree using recursion
       base case
       (memorization) not necessary in this step

   test it
 
 2. make it efficient // this step is much easy 
   add a memo object
   add a base case to return memo value
   store return value into the memo object

2021 September 22th
  Tabulation recipe
  
    visualize the problem as a table
    
    size the table based on the input
    
    initiate the table with default value
    
    seed the trival answer into the table
    
    iterate through the table
    
    fill further positions based on the current position
    
#### binary search类型问题的 边界选择问题。强推 这篇 https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/

> 二分查找重点概括
写成 while(left < right) ，退出循环的时候有 left == right 成立，好处是：不用判断应该返回 left 还是 right；
区间 [left..right] 划分只有以下两种情况：
分成 [left..mid] 和 [mid + 1..right]，分别对应 right = mid 和 left = mid + 1；
分成 [left..mid - 1] 和 [mid..right]，分别对应 right = mid - 1 和 left = mid，这种情况下。需要将 int mid = (left + right) / 2 改成 int mid = (left + right + 1) / 2，否则会出现死循环，这一点不用记，出现死循环的时候，把 left 和 right 的值打印出来看一下就很清楚了；
退出循环 left == right，如果可以确定区间 [left..right] 一定有解，直接返回 left 就可以，否则还需要对 left 这个位置单独做一次判断；
始终保持不变的是：在区间 [left..right] 里查找目标元素。

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

### hahaha