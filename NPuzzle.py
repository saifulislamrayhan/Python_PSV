i_puzzle = [[7, 1, 2], [5, '10000', 4], [8, 3, 6]]
f_puzzle = []
dim = len(i_puzzle)
b = []

for i in range(0, dim):
    for j in range(0, dim):
        if i_puzzle[i][j] == '10000':
            b = [i, j]
            continue
        else:
            f_puzzle.append(i_puzzle[i][j])
inversion = 0
dim1 = len(f_puzzle)
k = 0
while k < dim1:
    for j in range(k, dim1):
        if f_puzzle[k] > f_puzzle[j]:
            inversion += 1
    k += 1
b_tile = dim - (b[0]) + 1
if (dim % 2 != 0) & (inversion % 2 == 0):
        print("Solvable")
elif (dim % 2 == 0) & (b_tile % 2 != 0) & (inversion % 2 == 0):
        print("Solvable")
elif (dim % 2 == 0) & (b_tile % 2 == 0) & (inversion % 2 != 0):
        print("Solvable")
else:
    print("Not Solvable")
