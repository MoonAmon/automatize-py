grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0
y = 0

for y in range(0, 6):
    print(grid[x][y], end=' ')
    for x in range(0, 9):
        if x == 8:
            print(grid[x][y], end=' ')
            print('')
        elif x == 0:
            b = 0
        else:
            print(grid[x][y], end=' ')
