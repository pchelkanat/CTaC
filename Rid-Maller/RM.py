import numpy as np

r = 1  # код первого порядка
m = 4  # 2**m длины
mistakes=2**(m-r-1)-1 #сколько может исправить
print("mistakes", mistakes)

x = np.array([1, 0, 0, 1, 1])
print("x", x)

H1 = np.array([[1, 1], [1, -1]], dtype=np.int8)  # матрица Адамара
# print(H1)

def Adamar_2(H1):
    temp1 = np.vstack((H1, H1))
    temp2 = np.vstack((H1, -1 * H1))
    H = np.hstack((temp1, temp2))
    return H


def Adamar_m(m, H):
    i = 1
    while i != m:
        H = Adamar_2(H)
        i += 1
    return H


def gen_G(m):
    G = np.zeros((m + 1, 2 ** m), dtype=np.int8)
    G[0] = np.array([1] * 2 ** m)
    # print(np.shape(G),G)

    for i in range(1, m + 1):
        G[i] = np.array(([0] * (2 ** (m - i)) + [1] * (2 ** (m - i))) * 2 ** (i - 1))
    # print("G", G)
    return G


def coding_RM(x, G):
    return np.dot(x, G) % 2

#по принципу максимального правдоподобия
def decoing_RM(y, m, H1):
    H_m = Adamar_m(4, H1)
    I = np.ones_like(H_m, dtype=np.int8)
    A_m = (I + H_m) // 2  # Двоичная матрица Адамара
    print("H_m", H_m)
    print ("A_m",A_m)

    Y = 2 * y - 1  # преобразование y'
    vec = np.dot(Y, H_m)  # находим вектор
    print("Y, vec", Y, vec)
    max = np.argmax(vec)
    y_new = A_m[max] + 1 // 2
    print("max, right y", max, y_new)

    x = np.zeros((m + 1), dtype=np.int8)
    x[0] = y_new[0]

    for i in range(m):
        x[m - i] = (y_new[0] + y_new[2 ** i]) % 2
        # print(i, m - i, y[2**i], x[m - i])
    return x


G = gen_G(m)
y = coding_RM(x, G)
print("y encoding", y)

y = np.array([1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0])
print("y with errors", y)
x_new = decoing_RM(y, m, H1)
print("x decoding", x_new)
