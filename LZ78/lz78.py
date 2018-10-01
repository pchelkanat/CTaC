def compressLZ78(data):
    result = ""
    buff = ""
    dict = {}
    index = 0
    pos = 1

    while index != len(data):
        buff += data[index]
        #print("buff", buff)
        if buff not in dict:
            dict[buff] = pos
            pos += 1
            if len(buff) == 1:
                result += str(0) + "~" + str(buff) + '\n'
            elif len(buff) == 0:
                result += str(0) + "~" + str(" ") + '\n'
            else:
                char = buff[:-1]
                position = dict[char]
                #print(buff, char)
                result += str(position) + "~" + str(buff[-1]) + "\n"
            buff = ""
        index += 1
    #print("dect en", dict)
    output.write(result)
    return result

def convertToList(data):
    res=[]
    temp = data.split("\n")
    for i in temp:
        if i!="":
            t=[int(i.split("~")[0]),(i.split("~")[1])]
            res.append(t)
    #print(res)
    return res

def decompressLZ78(data):
    result = ""
    dict = {}
    pos = 1
    size=0
    conv = convertToList(data)
    while size < len(conv):
            index, letter=conv[size][0], conv[size][1]
            if index==0:
                char=letter
            else:
                char=dict[index]+letter
            dict[pos]=char
            pos+=1
            #print(dict)
            result+=char
            size+=1

    #print(result)
    output2.write(result)
    return result


##______COMPRESSING______##

fileName = "test.txt"
input = open(fileName, encoding='utf-8', mode='r')
output = open("lz78-" + fileName, encoding='utf-8', mode='w')

data = "".join(input.readlines()).replace("\n"," ")
# print(data)
#data = "abracadabra"
compressLZ78(data)

input.close()
output.close()



##______DECOMPRESSING______##

input2 = open("lz78-"+fileName, encoding='utf-8', mode='r')
output2 = open("dec-lz78-" + fileName, encoding='utf-8', mode='w')

data2 = "".join(input2.readlines())
#print(data2)
decompressLZ78(data2)

input2.close()
output2.close()
