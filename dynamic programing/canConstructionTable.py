def canConstructTable(str, wordbank):
    table = [False]*(len(str)+1)
    table[0] = True
    # print(table)
    for i in range(len(str)):
        # print(i)
        if table[i] == True:
            for word in wordbank:
                if str[i:i+len(word)] and word == str[i:i+len(word)]:
                    table[i+len(word)] = True

    print(table[len(str)])
    return table[len(str)]


canConstructTable("abcdef", ["ab", "abc", "cd", "def", "abcd"])
canConstructTable("skateboard", ["bo", "rd", "ate", "t", "ska", 'sk', "boar"])
canConstructTable("enterapotentpot", [
                  "a", "p", "ent", "enter", "ot", 'o', "t"])
canConstructTable("eeeeeeeeeeeeeef", ["e"])
