def canSumTable(targetSum, numbers):
    table = [False]*(targetSum+1)
    table[0] = True

    for i in range(0, targetSum):
        if(table[i] == True):
            for num in numbers:
                if (i + num) <= targetSum:
                    table[i + num] = True

    return table[targetSum]


print(canSumTable(7, [2, 3]))
print(canSumTable(7, [5, 3, 4]))
print(canSumTable(7, [2, 4]))
print(canSumTable(8, [2, 3, 5]))
print(canSumTable(300, [7, 14]))
