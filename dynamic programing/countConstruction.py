def countConstruction(target, wordbank):
    if target == '':
        return 1
    totalcount = 0
    for word in wordbank:
        if word in target:
            remainder = target.lstrip(word)
            if remainder == target:
                continue
            numwaysfortherest = countConstruction(remainder, wordbank)
            totalcount += numwaysfortherest
    return totalcount


# I have problem with the first case
print(countConstruction('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruction('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruction('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruction('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))

print(countConstruction('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
      'e', 'eeee', 'eeeeeeee', 'eeeee', 'eeeeeee', 'eeee', '']))
