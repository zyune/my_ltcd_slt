def bestSumTable(targetSum, numbers):
    table = [None]*(targetSum+1)
    table[0] = []
    for i in range(0, targetSum):
        if table[i] != None:
            for num in numbers:
                if (i + num) <= targetSum:

                    if table[i+num] == None:
                        table[i+num] = table[i]+[num]
                    else:
                        currentsum = table[i]+[num]
                        if len(currentsum) < len(table[i+num]):
                            table[i+num] = currentsum

    return table[targetSum]


print(bestSumTable(8, [2, 3, 5]))
print(bestSumTable(8, [1, 4, 5]))
print(bestSumTable(7, [2, 3]))
print(bestSumTable(7, [5, 3, 4, 7]))
print(bestSumTable(7, [2, 4]))
print(bestSumTable(300, [7, 14]))
print(bestSumTable(100, [1, 2, 5, 25]))
