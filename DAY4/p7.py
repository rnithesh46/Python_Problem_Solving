def find(maze,x,y,path):
    if(x<4 and y<4 and maze[x][y]==1):
        return
    elif(x==3 and y==3 and maze[x][y]==0):
        print(path)
        return
    elif(x>3 or y>3):
        return
    else:
        find(maze,x+1,y,path+"D")
        find(maze,x,y+1,path+"R")
maze=[[0,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,0]]
path=""
find(maze,0,0,path)