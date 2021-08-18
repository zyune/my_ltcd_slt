class Solution:
    #https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/easy/20.valid-parentheses
    # 关于这道题的思路，邓俊辉讲的非常好，没有看过的同学可以看一下，视频地址。
    # 使用栈，遍历输入字符串
    # 如果当前字符为左半边括号时，则将其压入栈中
    # 如果遇到右半边括号时，分类讨论：
    # 1）如栈不为空且为对应的左半边括号，则取出栈顶元素，继续循环
    # 2）若此时栈为空，则直接返回 false
    # 3）若不为对应的左半边括号，反之返回 false
    def isValid(self,s):
      stack = []
      map = {
        "{":"}",
        "[":"]",
        "(":")"
      }
      for x in s:
        if x in map:
          stack.append(map[x]) #what really enter in the stack is the counterpart of },],) ,
                            # because when make a comparision we need to },],)  使用括号的右半部分来做相等比较
    # 如果遇到右半边括号时，分类讨论：
    # 1）如栈不为空且为对应的左半边括号，则取出栈顶元素，继续循环
    # 2）若此时栈为空，则直接返回 false
    # 3）若不为对应的左半边括号，反之返回 false
        else:
          if len(stack)!=0:
            top_element = stack.pop()
            if x != top_element:
              return False # 3）若不为对应的左半边括号，反之返回 false
            else:
              continue
          else:      # 2）若此时栈为空，则直接返回 false
            return False
      return len(stack) == 0