import numpy as np
import math


def matrix_multiply(A, B):  # this function returns  matrix A*B
    a, b, c, d = A
    x, y, z, w = B

    return (
        a*x + b*z,
        a*y + b*w,
        c*x + d*z,
        c*y + d*w,
    )


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
            B = matrix_multiply(B, B)
            global global_N
            global_N += 1
            i = i*2
        # add on the remainder
        R = matrix_power(F1, n-i//2)
        return matrix_multiply(B, R)


F1 = [1, 1, 1, 0]


def matrix_fib(n):
    return matrix_power(F1, n)[1]


if __name__ == "__main__":
    global_N = 0
    print(matrix_fib(8))

    print("O(logn)", global_N)

print("np.floor(math.log(8, 2))的结果是", np.floor(math.log(9, 2)))
