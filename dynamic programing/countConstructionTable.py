def countConstructionTable(str, wordbank):
    table = [0]*(len(str)+1)
    table[0] = 1
    for i in range(len(str)):
        if table[i] != 0:
            for word in wordbank:
                if str[i:i+len(word)] and word == str[i:i+len(word)]:
                    # 这一步就比较绝妙了 一定是+table[i] 而不是简单地加1，因为之前的几种加起来的方式也得算在里面
                    table[i+len(word)] += table[i]
    return table[len(str)]


print(countConstructionTable("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstructionTable("yinzheng", ["yin", "zheng", "yinz", "heng"]))
print(countConstructionTable("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))

print(countConstructionTable(
    "eeeeeeeeeeeeeef", ["e", "ee", "eeeee", "eeeeee"]))
