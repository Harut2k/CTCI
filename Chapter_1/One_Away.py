#time complexity O(n)
def One_Away(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    lengthdiff = abs(len1 - len2)
    change = False
    if(lengthdiff>1):
        return False
    index1 = 0
    index2 = 0
    while(index1<len1 and index2<len2):
        if(string1[index1] == string2[index2]):
            index1+=1
            index2+=1
        elif(lengthdiff==1):
            if(index1+1<len1 and string1[index1+1] == string2[index2]):
                index1+=2
                index2+=1
            elif(index2+1<len2 and string1[index1] == string2[index2+1]):
                index1+=1
                index2+=2
            else:
                return False
            lengthdiff=0
        elif(change==False):
            index1+=1
            index2+=1
            change = True
        else:
            return False
    return True





string1 = input("Enter first: ")
string2 = input("Enter second: ")

if(One_Away(string1,string2)):
    print("One away")
else:
    print("Not one away")
