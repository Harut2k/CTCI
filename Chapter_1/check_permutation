
#time complexity is O(n)
def is_permutation_array(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if(len1 != len2):
        return False
    bucket = [0] * 128
    for i in range(0,len(string1)):
        bucket[ord(string1[i])]+=1
    for i in range(0,len(string2)):
        bucket[ord(string2[i])]-=1
    for i in range(0,127):
        if(bucket[i] !=0):
            return False
    return True


#time complexity is O(n)
from collections import Counter
def is_permutation_counter(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if(len1 != len2):
        return False
    count = Counter()
    for c in string1:
        count[c] += 1
    for c in string2:
        if count[c] == 0:
            return False
        count[c] -= 1
    return True



#time complexity is O(n*log(n))
def is_permutation_sort(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if(len1 != len2):
        return False
    list1 = sorted(string1)
    list2 = sorted(string2)
    for i in range(0,len1):
        if(list1[i]!=list2[i]):
            return False
    return True




val1 = input("Enter string one")
val2 = input("Enter string two")


if(is_permutation_array(val1,val2)):
    print("They are permutations of eachother")
else:
    print("They are not permutations of eachother")

if(is_permutation_counter(val1,val2)):
    print("They are permutations of eachother")
else:
    print("They are not permutations of eachother")


if(is_permutation_sort(val1,val2)):
    print("They are permutations of eachother")
else:
    print("They are not permutations of eachother")
