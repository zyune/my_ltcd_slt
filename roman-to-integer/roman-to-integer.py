class Solution(object):
    #题懂了就非常简单。首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，如果当前字符代表的值不小于其右边，就加上该值；否则就减去该值。以此类推到最左边的数，最终得到的结果即是答案
    def romanToInt(self, s):
        ss = list(s)
        dict = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        number=0
        for i in range(len(ss)):
            print(ss[i])
            if i+1 < len(ss):
                if dict[ss[i]] < dict[ss[i+1]]:
                    number = number - dict[ss[i]]
                else:
                    number = number + dict[ss[i]]
            else:
                number = number + dict[ss[i]]
        print(number)
        return number
    
# s="CMXCIX"
# ss = list(s)
# #print(ss.pop())
# dict = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
# number=0
# for i in range(len(ss)):
#     #print(ss[i])
#     if i+1 < len(ss):
#         if dict[ss[i]] < dict[ss[i+1]]:
#             number = number - dict[ss[i]]
#         else:
#             number = number + dict[ss[i]]
#     else:
#         number = number + dict[ss[i]]
# #print(number)
        
for item in range:
     print(item)


        

    
        

 
    






