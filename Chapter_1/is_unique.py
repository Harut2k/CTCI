def repeats_datastruct(string):
    dict = {}
    for i in range(0,len(string)):
        if dict.get(string[i]):
            return True
        else:
            dict[string[i]]=1
    return False


def repeats_loop(string):
    for i in range(0,len(val)-1):
        for j in range (i+1,len(val)):
            if (string[i] ==string[j]):
                return True
    return False



val = input("enter string")


#time complexity is O(n)
if(repeats_datastruct(val)):
    print("The string contains repeating characters, used function with data structure")
else:
    print("The string does not contain repeating characters, used function with data structure")

#time complexity is O(n^2)
if(repeats_loop(val)):
    print("The string contains repeating characters, used function without data structure")
else:
    print("The string does not contain repeating characters, used function without data structure")
