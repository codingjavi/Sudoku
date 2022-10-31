#using numpy to print a matrix
import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,9]]

#print (np.matrix(grid))

#checking if guess is valid
def is_valid(y,x,n):
    global grid
    #checking the rows
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    #checking the columns
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    #checking the 3X3 boxes
    x_start = (x // 3) *3
    y_start = (y // 3) *3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y_start + i][x_start + j] == n:
                return False


    #guess is not in table
    return True
    

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            #check its an empty space(0)
            if grid[y][x] == 0:
                #assining a random guess
                for i in range(1, 10):
                    n = i
                    if is_valid(y,x,n):
                        grid[y][x] = n
                        #using recursion here to keep calling the same fuction
                        solve()
                        #if the guess doesn't work
                        #backtracking here(changing the solution if the guess doesn't work)
                        grid[y][x] = 0
                return
    
    print(np.matrix(grid))
#calling the function to solve it
solve()

