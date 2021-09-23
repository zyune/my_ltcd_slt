def howSumTable(targetSum, numbers):
    table = [None]*(targetSum+1)
    table[0] = []
    for i in range(0, targetSum):
        if table[i] != None:
            for num in numbers:
                if (i + num) <= targetSum:
                    table[i+num] = table[i]+[num]

    return table[targetSum]


print(howSumTable(7, [2, 3]))
print(howSumTable(7, [5, 3, 4, 7]))
print(howSumTable(7, [2, 4]))
print(howSumTable(300, [7, 14]))
