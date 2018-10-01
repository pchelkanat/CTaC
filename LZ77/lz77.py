def findIndex(dict, buff):
    # т.к rfind возвращает -1 если не найдет подстроку
    size = 0
    # size<len & temp==-1(loop)
    while len(buff) - size > 0:  # смотрим по буферу и уже пройденной data = dict
        t = buff[:len(buff) - size]
        temp = dict.rfind(t)  # так как нумерация от 0 и слева направо, то ищем последнее вхождение
        if temp > -1:  # size<len & temp!=-1(ok)
            pos = len(dict) - temp
            mysize = len(t)
            return pos, mysize
        size += 1
    return 0, 0


def compressLZ77(data):

    print("compressing")

    result = ""
    buff_len = 256  # 256 bits for unicode
    dict = ""  # пройденое
    buff = data[:buff_len]
    step=0
    while len(data) > 0:
        pos, mysize = findIndex(dict, buff)
        # исключение для конца строки
        if len(buff) <= len(data):
            letter = data[mysize]  # т.к сам буфер может стать letter
        else:
            letter = ''

        #print(dict, data, buff, pos, mysize, letter)
        result += str(pos) + "~" + str(mysize) + "~" + str(letter) + "\n"

        dict += data[:(mysize + 1)]
        data = data[(mysize + 1):]

        if buff_len > len(data):
            buff = data
        else:
            buff = data[:buff_len]

        step+=1
        #print("c",step)
    output.write(result)
    return result


def convertToList(data):
    res = []
    temp = data.split("\n")
    for i in temp:
        if i != "":
            t = [int(i.split("~")[0]), int(i.split("~")[1]), (i.split("~")[2])]
            res.append(t)
    # print(res)
    return res


def decompressLZ77(data):

    print("decompressing")

    result = ""
    index = 0
    conv = convertToList(data)
    # print(conv)
    while index < len(conv):#построчно в списке
        pos, size, letter = conv[index][0], conv[index][1], conv[index][2]
        if pos == 0 & size == 0:
            result += str(letter)
        else:
            begin = len(result) - pos
            end = begin + size
            result += str(result[begin:end])+str(letter)
        index += 1
        #print("d",index)
    #print(result)
    output2.write(result)
    return result


##______COMPRESSING______##

fileName = "Zlodeya.txt"
input = open(fileName, encoding='utf-8', mode='r')
output = open("compress/lz77-" + fileName, encoding='utf-8', mode='w')

data = "".join(input.readlines()).replace("\n"," ")
#data = "abracadabrad"#"kabababababz"
compressLZ77(data)

input.close()
output.close()


##______DECOMPRESSING______##

input2 = open("compress/lz77-" + fileName, encoding='utf-8', mode='r')
output2 = open("decompress/dec-lz77-" + fileName, encoding='utf-8', mode='w')

data2 = "".join(input2.readlines())
# print(data2)
decompressLZ77(data2)
