def fibTable(n):
    table = [0]
    table = [0]*(n+2)
    table[1] = 1
    for i in range(1, n):
        print(i)
        table[i+1] += table[i]
        table[i+2] += table[i]

    return table[n]


print(fibTable(6))
# print(fibTable(7))
# print(fibTable(8))
# print(fibTable(50))
print(range(6))
