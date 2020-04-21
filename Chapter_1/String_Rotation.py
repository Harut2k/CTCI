#time complexity is O(n)
def isrotation(string1,string2):
    if(not len(string1) == len(string2)):
        return False
    string3 = string2 + string2
    if(string1 in string3):
        return True
    else:
        return False



str1 = input("Enter first string")
str2 = input("Enter second string")
if(isrotation(str1,str2)):
    print("it is rotation")
else:
    print("is not rotation")
