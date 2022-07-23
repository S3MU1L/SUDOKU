from random import randint, shuffle

class Generate:
    def __init__(self):
        grid = [[0 for j in range(9)] for i in range(9)]
        self.values = [i for i in range(1,10)]
        self.fill_grid(grid)
        self.solved = [row[:] for row in grid]
        attempts = 5
        global counter
        counter = 1
        while attempts > 0:
            row = randint(0, 8)
            col = randint(0, 8)
            while grid[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)
            
            original_value = grid[row][col]
            grid[row][col] = 0
            
            copy = [row[:] for row in grid]

            counter = 0
            self.solve_grid(copy)
            
            if counter != 1:
                grid[row][col] = original_value
                attempts -= 1

        self.sudoku = grid
        
        
    
    def check_3x3(self, grid, y, x, value):
        y0 = (y//3) * 3
        x0 = (x//3) * 3
        for y in range(3):
            for x in range(3):
                if grid[y0+y][x0+x] == value:
                    return False
        return True

    def check_grid(self, grid):
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    return False
        return True

    def fill_grid(self, grid):
        
        for i in range(0,81):
            row = i//9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(self.values)
                for value in self.values:
                    flag = False
                    for j in range(9):
                        if value == grid[j][col]:
                            flag = True
                        if value == grid[row][j]:
                            flag = True

                    if not flag:
                        if self.check_3x3(grid, row ,col, value):
                            grid[row][col] = value
                            if self.check_grid(grid):
                                return True
                            else:
                                if self.fill_grid(grid):
                                    return True
                break
        grid[row][col] = 0

    def solve_grid(self, grid):
        global counter
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    flag = False
                    for j in range(9):
                        if value == grid[j][col]:
                            flag = True
                        if value == grid[row][j]:
                            flag = True

                    if not flag:
                        if self.check_3x3(grid, row ,col, value):
                            grid[row][col] = value
                            if self.check_grid(grid):
                                counter += 1
                                break
                            else:
                                if self.solve_grid(grid):
                                    return True
                break
        grid[row][col] = 0





