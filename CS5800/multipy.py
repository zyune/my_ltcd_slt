# caculate n to the power p function 计算 n 的幂 p 函数
import numpy as np


def power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    else:
        # return power(n, np.floor(p/2))*power(n, p-np.floor(p/2))

        return power(n, int(p/2))*power(n, p-int(p/2))


print(power(2, 8))
print(power(2, 9))
print(power(5, 4))
