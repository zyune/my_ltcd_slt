def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
            # remainderCombination.append(num)
            combination = remainderCombination
            combination.append(num)
            # combination=remainderCombination.append(num)
            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    # print("current num is ", print(
    #     "currentshortest combination is ", num))
    # print("currentshortest combination is ", shortestCombination)
    memo[targetSum] = shortestCombination

    return memo[targetSum]
    #print("memo is",memo[targetSum])
    # print(shortestCombination)


# print(bestSum(0, []))
print(bestSum(10, [2, 3, 5]))


# print(bestSum(100, [10, 2, 5, 25]))
