def displayPathtoPrincess(n,grid):
#print all the moves here
    print(grid)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)