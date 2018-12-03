#Множество кодовых слов
def gen_codes(n, m, a):
    arr=[]
    for i in range(n**2):
        arr.append(bin(i)[2:].zfill(n))

    sum = []
    for k in arr:
        sum.append(S_u(k, m))

    mod_arr = []
    for k in range(len(sum)):
        if sum[k] == a:
            mod_arr.append(arr[k])
    return mod_arr#, arr, sum,

#Подсчет суммы по формуле
def S_u(word, m):
    temp=0
    for t in range(len(word)):
        temp+=(t+1)*int(word[t])
    return temp%m

#Вес слова
def W(word):
    w=0
    for i in word:
        if i=='1':
            w+=1
    return w

#Удаление единицы при k<w(u)
def del_1(word,num):
    word=word[::-1]
    k=0
    while num!=0:
        if word[k]=='0':
            num-=1
            k+=1
        elif word[k]=='1':
            k+=1
    word=word[:k]+word[k+1:]
    return word[::-1]

#Удаление нуля при k>w(u)
def del_0(word,num):
    word = word[::-1]
    k = 0
    while num != 0:
        if word[k] == '1':
            num -= 1
            k += 1
        elif word[k]=='0':
            k+=1
    word = word[:k] + word[k + 1:]
    return word[::-1]

#Исправление ошибки
def correction(word, n, m):
    k=S_u(word,m)
    w=W(word)
    print("k, w:", k,w)

    if k==0:
        return word[:-1]
    elif k==w:
        return word[1:]
    elif k>w:
        return del_1(word,n+1-k)
    elif k<w:
        return del_0(word, k)

#Коды Варшамова-Тененгольца
n=4
m=5
a=0

tuple=gen_codes(n, m, a)
print(tuple)

u='10101'
code=correction(u, n, m)
print("correct code:", code)

