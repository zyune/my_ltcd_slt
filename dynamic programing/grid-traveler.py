def grid_travel(a,b,memo=dict()):
    if(a==1 and b==1): return 2
    if(a==0 or b ==0): return 1
    return grid_travel(a-1, b) + grid_travel(a, b-1)
def grid_travel_memo(a,b,memo=dict()):
    # are the args in the memo
    key= str(a)+','+str(b)
    print(key)
    if key in memo:
        return memo[key]
    if(a==1 and b==1): return 2; #base case 
    if(a==0 or b ==0): return 1; #base case 
    memo[key]= grid_travel_memo(a-1, b,memo) + grid_travel_memo(a, b-1,memo) #memorization
    return memo[key]


#don't write any pre emptive logic where you check key , like this if((m-1+','+n) in memo){}
    
print(grid_travel(2,3))
print(grid_travel_memo(4,5))

## memorization recipe
#stick to high level solutions 
# stay methodical to the following step and follow these

#1. make it work  // this step is the hard part
#   visualize the problem as a tree 
#   implement the tree using recursion
#       base case
#       (memorization) not necessary in this step
#
#   test it
# 
# 2. make it efficient // this step is much easy 
#   add a memo object
#   add a base case to return memo value
#   store return value into the memo object
#
#
#
#
