
F1 = [0, 1, 1, 1]


def matrix_fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        result = matrix_power(F1, n)
        return result[1]


def matrix_power(F1, n):
    if n == 0:
        return [1, 0, 0, 1]
    elif n == 1:
        return F1
    else:
        B = F1
        i = 2
        while i <= n:
            # repeated square B until n = 2^q > m
            B = matrix_multiply_f2(B, B)
            global global_N
            global_N += 1
            i = i*2
        # add on the remainder
        R = matrix_power(F1, n-i//2)
        return matrix_multiply_f2(B, R)


def matrix_multiply_f1(F1, B):
    a, b, c, d = F1
    x, y = B
    return (a*x+b*y, c*x+d*y)


def matrix_multiply_f2(A, B):  # this function returns  matrix A*B
    a, b, c, d = A
    x, y, z, w = B
    global add_time
    global multi_time
    add_time += 4
    multi_time += 8
    return (
        a*x + b*z,
        a*y + b*w,
        c*x + d*z,
        c*y + d*w,
    )


# 1,1,2,3,5,8,13,21,34,55
global_N = 0
add_time = 0
multi_time = 0
n = 8
print("the ", n, "th fib number is ", matrix_fib(n))
print("The is O(logn)", global_N)
print("the number of addition is performed is", add_time)
print("the number of multiplication is performed is", multi_time)
