def zeroMatrix(matrix, n, m):
    # Write your code here.
    for row in range(n):
        a = []
        for column in  range(m):
            if matrix[row][column] == 0:
                flag = 1
                row_value = row
                column_value = column
                continue   

    for row in range(n):
        for column in  range(m):
            matrix[row_value][column] = 0
            matrix[row][column_value] = 0

            # matrix += matrix.append(matrix)
            print(matrix[row][column], end=" ")
        
        print()

    
def main():
    matrix = []
    n = int(input("What is the row value"))
    m = int(input("What is the column value"))
    print("Enter the entries row wise:")
 
    for row in range(n):   
        a  = []
        for column in range(m):  
            a.append(int(input()))
        matrix.append(a)
 

    for row in range(n):
        for column in range(m):
            print(matrix[row][column], end=" ")
   
        print()

    # zeroMatrix(matrix, n, m)

main()

