def cansum(targetsum, numbers):
    # minnum = min(numbers)
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    for num in numbers:
        remainder = targetsum - num
        remainderresult = cansum(remainder, numbers)
        if remainderresult != None:
            remainderresult.append(num)
            return remainderresult
    return None


# test case for brute
# print(cansum(7, [2, 3]))
# print(cansum(7, [5, 4, 3, 7]))
# print(cansum(7, [2, 4]))
# print(cansum(8, [2, 3, 5]))
# print(cansum(300, [7, 14]))


def cansumfindfalse(targetsum, numbers, memo={}):
    # minnum = min(numbers)
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    for num in numbers:
        remainder = targetsum - num
        remainderresult = cansumfindfalse(remainder, numbers, memo)
        if remainderresult != None:
            remainderresult.append(num)
            return remainderresult
    memo[targetsum] = None
    return None


print(cansumfindfalse(8, [2, 3, 5]))
print(cansumfindfalse(7, [2, 3]))
print(cansumfindfalse(7, [5, 4, 3, 7]))
print(cansumfindfalse(7, [2, 4]))
print(cansumfindfalse(300, [7, 14]))
