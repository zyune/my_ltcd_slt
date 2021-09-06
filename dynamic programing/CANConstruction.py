

# def CanConstruct(str, wordbank=[]):
#     if str == "":
#         return True
#     for word in wordbank:
#         if str.index(word) == 0:
#             remainder = str.slice(len(word))
#             if CanConstruct(remainder, wordbank) == True and remainder != str:
#                 return True
#     return False


def myCanConstruct(str, wordbank):
    if str == "":
        return True
    for word in wordbank:
        if word in str:
            remainder = str.lstrip(word)
            if remainder == str:
                continue
            if myCanConstruct(remainder, wordbank) == True and remainder != str:
                return True
    return False


def myCanConstructMemo(str, wordbank, memo={}):
    if str == "":
        return True
    if str in memo:
        return memo[str]
    for word in wordbank:
        if word in str:
            remainder = str.lstrip(word)
            if remainder == str:  # This tipically important in my function
                continue
            if myCanConstructMemo(remainder, wordbank, memo) == True and remainder != str:
                memo[str] = True
                return memo[str]
    memo[str] = False
    return memo[str]


print(myCanConstructMemo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(myCanConstructMemo('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(myCanConstructMemo('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(myCanConstructMemo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
      'e', 'eeee', 'eeeeeeee', 'eeeee', 'eeeeeee', 'eeee', '']))
# a = 'skateboard'
# b = 'ska'
# a.lstrip(b)
# print(a.lstrip(b))
