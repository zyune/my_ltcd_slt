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
