def cansum(targetsum, numbers):
    minnum = min(numbers)
    if targetsum == 0:
        return True
    if targetsum < minnum:
        return False
    for num in numbers:
        remainder = targetsum-num
        if cansum(remainder, numbers) == 0:
            return True

    return False


print(cansum(8, [2, 3, 5]))
