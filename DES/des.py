import numpy as np

# начальная перестановка
IP1 = np.array(
    [58, 50, 42, 34, 26, 18, 10, 2,
     60, 52, 44, 36, 28, 20, 12, 4,
     62, 54, 46, 38, 30, 22, 14, 6,
     64, 56, 48, 40, 32, 24, 16, 8,
     57, 49, 41, 33, 25, 17, 9, 1,
     59, 51, 43, 35, 27, 19, 11, 3,
     61, 53, 45, 37, 29, 21, 13, 5,
     63, 55, 47, 39, 31, 23, 15, 7])

# конечная перестановка
IP2 = np.array(
    [40, 8, 48, 16, 56, 24, 64, 32,
     39, 7, 47, 15, 55, 23, 63, 31,
     38, 6, 46, 14, 54, 22, 62, 30,
     37, 5, 45, 13, 53, 21, 61, 29,
     36, 4, 44, 12, 52, 20, 60, 28,
     35, 3, 43, 11, 51, 19, 59, 27,
     34, 2, 42, 10, 50, 18, 58, 26,
     33, 1, 41, 9, 49, 17, 57, 25])

# бокс расширения
Pi_box = np.array(
    [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1])

# прямой бокс
Pi2_box = np.array(
    [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25])

# S-боксы
Si_box = np.array(
    [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],  # S1 -четырех битовый b'1
     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 1, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],  # S2 -четырех битовый b'2..
     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],  # S3
     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],  # S4
     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],  # S5
     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],  # S6
     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],  # S7
     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]])  # S8
# axis0 = Si, axis1 = Si[m] , axis2 = Si[m][l]

# удаление проверочных битов ключа + перестановка
CD_key = np.array([57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
                   10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,  # C
                   63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
                   14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4])  # D

# левый циклический сдвиг
CD_shift = np.array([1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1])

# перестановка сжатия ключа
Zip_key = np.array([14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32])


def bin_to_hex(list):
    t = "".join(str(i) for i in list)
    res = hex(int(t, 2))
    return res


# функция словаря
def save_dict(bin_text):
    dict = {}
    pos = 0
    for i in bin_text:
        pos += 1  # без потери индекса, с 1 до 64
        dict[pos] = i
    return dict


# текст + перестановка
def text_IP(dict, IP):
    text = []
    for i in IP: text.append(dict[i])
    return text


# расширение R для раунда
def P_ex(R):
    dictR = save_dict(R)
    R_ex = []
    for i in Pi_box: R_ex.append(dictR[i])
    return R_ex


# Вычисление позиции в S-боксах и нахождение шифрообознаения
def S_box(listR):
    R_new = np.ones((8, 4), dtype=np.uint8)
    for i in range(8):  # i 0..7 соответствует в Si_box Si
        # print("rr", i, listR[i])
        m = int(str(listR[i][0]) + str(listR[i][5]), base=2)  # 0..3 соответствует Si[m]
        l = int(str(listR[i][1]) + str(listR[i][2]) + str(listR[i][3]) + str(listR[i][4]), base=2)
        num = Si_box[i][m][l]
        # print(num)
        R_new[i] = np.array((list(bin(num)[2:].zfill(4))), dtype=np.uint8)
    # print("S_box", R_new, np.shape(R_new))
    return R_new


# прямой P бокс 32 бита
def P2(R_new):
    dictRnew = save_dict(R_new)
    R2 = []
    for i in Pi2_box:
        R2.append(dictRnew[i])
    return R2


# генерация ключей для раундов
def gen_keys(key):
    keyCD = []
    dictK = save_dict(key)
    for i in CD_key:
        keyCD.append(dictK[i])  # удаление проверочных битов ключа + перестановка
    key_C = keyCD[:28]  # 0..27
    key_D = keyCD[28:]
    # print("keyCD", type(key_D), key_C, key_D)

    keys = np.zeros((16, 48), dtype=np.uint8)  # раундовые ключи 0..15 -> !нужно вычитать при функции раунда
    t = 0
    for i in CD_shift:
        key_C = np.hstack((key_C[i:], key_C[:i]))  # смещение влево на i бит
        key_D = np.hstack((key_D[i:], key_D[:i]))
        temp = np.hstack((key_C, key_D))  # соединение C и D

        dictZip = save_dict(temp)  # для перестановки сжатия до 48 бит
        tempR = []
        for k in Zip_key:
            tempR.append(dictZip[k])
        keys[t] = tempR
        t += 1
    # print("keys", type(keys), np.shape(keys))
    return keys


# функция одного раунда
def func(R, keyi):
    R_ex = np.array(P_ex(R))
    res = R_ex ^ keyi
    # print("res",res, len(res))
    listR = np.array([res[0:6], res[6:12], res[12:18], res[18:24],
                      res[24:30], res[30:36], res[36:42], res[42:48]])
    # print("listR", listR, np.shape(listR))
    R_new = np.hstack(S_box(listR)[i] for i in range(8))
    # print("Rnew", R_new, len(R_new))

    R2 = np.array(P2(R_new))
    # print("R2",R2, len(R2))
    return R2


# Фейстель
def Feistel(L, R, keys):
    Li = np.array([L])
    Ri = np.array([R])  #

    print("             L0:", bin_to_hex(Li[0]), "    R0:", bin_to_hex(Ri[0]))
    for i in range(1, 17):
        Li = np.vstack((Li, Ri[i - 1]))
        temp = Li[i - 1] ^ func(Ri[i - 1], keys[i - 1])
        Ri = np.vstack((Ri, temp))
        print("round:", i, "    Li:", bin_to_hex(Li[i]), "    Ri:", bin_to_hex(Ri[i]), "    key:",
              bin_to_hex(keys[i - 1]))
    return Li[-1], Ri[-1]


bit = 64
bit_key = 48

text = 0x123456ABCD132536  # 0x5890DB2A46EBDC24 # input()
key = 0xAABB09182736CCDD  # 0xAC49FB4120DFEB23 #

# ** -> bin, убираем 0b, расширяем до 64 бит -> список с char -> np.array с uint8 (для того, чтобы потом xor'ить)
bin_text = np.array(list(bin(text)[2:].zfill(64)), dtype=np.uint8)
bin_key = np.array(list(bin(key)[2:].zfill(64)), dtype=np.uint8)

new_keys = gen_keys(bin_key)

dict = save_dict(bin_text)
IP1_text = text_IP(dict, IP1)
L = np.array(IP1_text[:32])
R = np.array(IP1_text[32:])
Ln, Rn = Feistel(L, R, new_keys)
resFeistel = np.hstack((Rn, Ln))  # после 16 раунда объединяются в R16L16
dict2 = save_dict(resFeistel)
IP2_text = text_IP(dict2, IP2)

print("bin_text", bin_text, len(bin_text))
print("dict", dict)
print("IP1_text", bin_to_hex(IP1_text))
print("L0, R0", L, R, len(L))
# print("newkeys for rounds", new_keys)
# print("Ln", Ln,"Rn",Rn, len(Ln))
# print("result after rounds", resFeistel)
print("IP2_text", bin_to_hex(IP2_text))
