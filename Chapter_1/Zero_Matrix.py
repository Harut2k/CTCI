#time complexity is O(n)
def zero(matrix,n,m):
    listCol=[]
    listRow=[]
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                listCol.append(j)
                listRow.append(i)
    for j in listCol:
        for i in range(m):
            matrix[i][j]=0
    for i in listRow:
        for j in range(n):
            matrix[i][j]=0




h = 5
w = 5
matrix = [[1 for j in range(w)] for i in range(h)]

matrix[1][1]=0
matrix[1][4]=0
matrix[3][2]=0
for row in matrix:
    print(row)
print("")

zero(matrix,5,5)

for row in matrix:
    print(row)
