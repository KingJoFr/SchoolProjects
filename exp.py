import random
matrix = []

numRows = int(input("Enter number of rows:"))
numColumns = int(input("Enter number of columns"))

for row in range(numRows):
    matrix.append([]) #adds empy row
    for column in range(numColumns):
        matrix[row].append(random.randint(0,99))
    
print(matrix)

for row in matrix:
    for value in row:
        print(value, end = ",")
    print()