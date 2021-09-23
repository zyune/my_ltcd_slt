def grid_travel(a, b):
    table = [[0]*(a+1) for _ in range(b+1)]
    table[1][1] = 1

    for i in range(0, a+1):
        for j in range(0, b+1):
            current = table[i][j]
            if i+1 <= a:
                table[i+1][j] += current
            if j+1 <= b:
                table[i][j+1] += current
            print(table)


grid_travel(3, 3)
#grid_travel(3, 2)
# for num in range(5):
#     print(num)
