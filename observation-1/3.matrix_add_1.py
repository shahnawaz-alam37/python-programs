def matrix_input(m,n):
    li = []
    for i in range(1,m+1):
        row = []
        for j in range(1,n+1):
            inp = int(input(f"enter matrix[{i}][{j}]:"))
            row.append(inp)
        li.append(row)
    return li

def sum(A,B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    print("addition of matrix")
    return output

def multiply(A,B):
    resmult = []
    for i in range(len(A)):
        list3=[]
   # iterate through columns of Y
        for j in range(len(B[i])):
            sum1=0
            for k in range(len(A[i])):
                sum1 = sum1+A[i][k]*B[k][j]
            list3.append(sum1)
        resmult.append(list3)
    print("multiplication")
    return resmult

print("matrix A:")
M = int(input("enter the no of rows(M):"))
N = int(input("enter the no of coloums(N):"))
A = matrix_input(M,N)

print("enter the matrix B:")
M = int(input("enter the no of rows(M):"))
N = int(input("enter the no of coloums(N):"))
B = matrix_input(M,N)

li = sum(A,B)
for i in li:
    print(f"\n{i}")
li = multiply(A,B)
for i in li:
    print(f"\n{i}")

