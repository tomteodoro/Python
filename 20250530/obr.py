ledGrid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            ledGrid[i][j] = 1
            
for row in ledGrid:
    print(row)