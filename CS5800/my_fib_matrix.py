def fib_matrix(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        F1 = [0, 1, 1, 1]
        return naive_matrix_power(F1, n)[0]


def naive_matrix_power(F1, n):

    B = [1, 1]
    for _ in range(n-1):
        B = matrix_multiply(F1, B)
        global number_of_matrix_muliply
        number_of_matrix_muliply += 1
        # print(B)
    return B


def matrix_multiply(F1, B):
    a, b, c, d = F1
    x, y = B
    global add_time
    global multi_time
    add_time += 2
    multi_time += 4
    return (a*x+b*y, c*x+d*y)


number_of_matrix_muliply = 0
add_time = 0
multi_time = 0
n = 8  # input your nth fibonacci number here
print("the", n, "number of fibonacci number is", fib_matrix(n))
print("the number of matrix muliply is", number_of_matrix_muliply)
print("the number of addition is performed is", add_time)
print("the number of multiplication is performed is", multi_time)
