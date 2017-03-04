def findSkew(r,i,j):
    skewDiagonal = []
    while j < N and (r- i) >= 0:
        skewDiagonal.insert(i, a[r - i][j])
        i += 1
        j += 1.
    total = sum(skewDiagonal)
    avg = float(float(total) / len(skewDiagonal))
    return avg

def newMatrix(m,n,row,avg):
    while n< N and (row-m) >= 0 :
        A[row-m][n]=avg
        m += 1
        n += 1


def main():

    # first find skew matrix row wise
    for row in range(0,M):
        avg=findSkew(row,0,0)
        # update Hanker matrix A[][] with average value
        A[row][0]=avg
        newMatrix(1,1,row,avg)

    row=M-1
    # start finding skew matrix from col 1 onwards
    for col in range(1,N):
        avg=findSkew(row,0,col)
        # update Hanker matrix A[][] with average value
        newMatrix(0,col,row,avg)
    print(A)

if __name__ == "__main__":
    M = int(input('number of rows, m = '))
    N = int(input('number of columns, n = '))
    if M > N:
        exit(0)
    a = [x[:] for x in [[0] * N] * M]
    for i in range(0, M):
        for j in range(0, N):
            print ('entry in row: ', i + 1, ' column: ', j + 1)
            a[i][j] = int(input())
    print (a)
    A = [[0 for x in range(N)] for y in range(M)]  # final matrix
    main()