#time complexity
def compress(string):
    strlen = len(string)
    compressL=[string[0]]
    num = 1
    indexc=0

    for i in range(1,strlen):
        if(string[i] != compressL[indexc]):
            compressL.append(str(num))
            compressL.append(string[i])
            indexc+=2
            num=1
        else:
            num+=1
    compressL.append(str(num))


    word= "".join(compressL)
    if(len(word) <= strlen):
        return word
    else:
        return string







string1 = input("enter string")
string2 = compress(string1)
print(string2)
