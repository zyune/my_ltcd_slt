

def matrix_multiply(A, B):  # this function returns  matrix A*B
    a, b, c, d = A
    # print(a,b,c,d)
    x, y, z, w = B
    print("A is ", A)
    print("B is", B)
    global time_add
    time_add += 4
    global time_multi
    time_multi += 8
    return (
        a*x + b*z,
        a*y + b*w,
        c*x + d*z,
        c*y + d*w,

    )


def naive_matrix_power(A, m):
    if m == 1:
        return [1, 0, 0, 1]
    B = A
    for _ in range(m-1):
        B = matrix_multiply(B, A)
        global X_N
        X_N += 1
    return B


def naive_matrix_fib(n):
    F1 = [0, 1, 1, 1]
    return naive_matrix_power(F1, n)[2]


if __name__ == "__main__":

    time_add = 0
    time_multi = 0
    X_N = 0
    print(naive_matrix_fib(6))
    print("addition function execution time is", time_add)
    print("time_multi", time_multi)
    print("X_N", X_N)
