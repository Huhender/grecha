matrix = [[3, 3, 5],
[2, 2, 3],
[7, 8, 9]]




for i in range(len(matrix)):
    m = max(matrix[i])
    m_in = matrix[i].index(m)
    matrix[i][m_in], matrix[i][i] = matrix[i][i], matrix[i][m_in]
for row in matrix:
    print(row)

