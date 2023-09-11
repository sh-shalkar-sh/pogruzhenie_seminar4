def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


my_matrix = [['a', 'b', 'c'],
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

result = transpose_matrix(my_matrix)

for rows in result:
    print(rows)