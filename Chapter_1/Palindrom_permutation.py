#Time complexity is O(n)
def palindrome_permutation(string):
    List = [0] * 26
    MiddleOccured = False
    for i in string:
        ASCII =ord(i.lower())-97
        if(ASCII>=0):
            List[ord(i.lower())-97]+=1
    for i in range(0,26):
        if(List[i]%2 !=0):
            if(MiddleOccured):
                return False
            else:
                MiddleOccured = True
    return True

string = input("Enter string to check if it is permutation of palindrome")
if(palindrome_permutation(string)):
    print("it is permutation of palindrome")
else:
    print("it is not")
