def cansum(targetsum, numbers):
    minnum = min(numbers)
    if targetsum == 0:
        return True
    if targetsum < minnum:
        return False
    for num in numbers:
        remainder = targetsum - num
        if cansum(remainder, numbers) == True:
            return True
    return False


def cansumfindfalse(targetsum, numbers, falseremainders={}):
    # print(falseremainders)
    minnum = min(numbers)
    if targetsum in falseremainders:  # when adding a memo use the parameter within the arguement
        return falseremainders[targetsum]
    if targetsum == 0:
        return True
    if targetsum < minnum:
        return False

    for num in numbers:
        remainder = targetsum - num
        if cansumfindfalse(remainder, numbers, falseremainders) == True:
            return True
        if targetsum not in falseremainders:
            falseremainders[targetsum] = False
    return False

# this function has problem just use the cansumfindfalse function.
# to be honest I don't think there's any necessary to cache true


def cansumfindtrue(targetsum, numbers, memo={}):
    minnum = min(numbers)
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return True
    if targetsum < minnum:
        return False
    for num in numbers:
        remainder = targetsum - num
        if cansumfindtrue(remainder, numbers, memo) == True:
            memo[targetsum] = True
            return True
    memo[targetsum] = False
    return False


print(cansumfindfalse(7, [2, 3]))
print(cansumfindfalse(7, [5, 4, 3, 7]))
print(cansumfindfalse(7, [2, 4]))
print(cansumfindfalse(8, [2, 3, 5]))
print(cansumfindfalse(300, [7, 14]))

# print(cansumfindtrue(7, [2, 3]))
# print(cansumfindtrue(7, [5, 4, 3, 7]))
# print(cansumfindtrue(7, [2, 4]))
# print(cansumfindtrue(8, [2, 3, 5]))
# print(cansumfindtrue(300, [7, 14]))
