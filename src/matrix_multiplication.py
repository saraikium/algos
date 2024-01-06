type Matrix = list[list[int]]

def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    """We'll assume that both matrix are square of the order n x n. """
    # Find the dimensions of the matrix A
    m = len(a)
    n = len(a[0])
    # Find the dimensions of the matrix B
    q = len(b)
    r = len(b[0])
    # If they're not multiplication compatible raise a ValueError
    if n != q:
        raise ValueError(f"{m}x{n} matrix can't be multiplied with {q}x{r} matrix.")
    # Prepare the result matrix and fill it with 0s
    # It's dimensions will be m x r
    result = [[0]*r for _ in range(m)]
    # if the matrices are m x n and n x r
    # The first loop will run m times
    for i in range(m):
        # The second loop will run n times
        for j in range(r):
            for k in range(n):
                value = a[i][k] * b[k][j]
                result[i][j] += value
    return result

X = [[3, 1, 4]]
Y = [
    [4, 3],
    [2, 5],
    [6, 8],
        ]

A = [
    [12,7,3],
    [4 ,5,6],
    [7 ,8,9]
    ]

B = [
    [5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]
    ]


print(matrix_multiply(X, Y))
print(matrix_multiply(A, B))
