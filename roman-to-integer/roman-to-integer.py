class Solution(object):
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
        



        

    
        

 
    





