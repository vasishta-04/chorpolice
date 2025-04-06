from typing import Tuple, List
import random as r
import time as t


class dfs_class:
    def __init__(self, board, board_size,packman_pos):
        self.N,self.M = board_size
        self.E = 6
        self.m = board
        self.packman_pos = packman_pos

        # print(board)
        # print(board_size)

        self.path=[]
        self.dx=[0,1,0,-1]
        self.dy=[1,0,-1,0]
        self.vis =[[0 for i in range(self.M)] for i in range(self.N)]

    def inbound(self,x,y):
        return x<self.N and x>=0 and y<self.M and y>=0


    def dfs(self,map, x,y, curr_path):
        if(len(curr_path)>self.E):
            return
        if map[x][y] in {"-", "|"}:
            return
        curr_path.append((x,y))
        # print(self.m)
        # print(curr_path)
        if self.packman_pos == tuple((x,y)):
            self.path.append(list(curr_path))
            curr_path.pop()
            return
        
        for i in range(len(self.dx)):
            curr_x=x+self.dx[i]
            curr_y=y+self.dy[i]
            if self.inbound(curr_x, curr_y) and not self.vis[curr_x][curr_y] :
                self.vis[curr_x][curr_y]=1
                self.dfs(map, curr_x, curr_y, curr_path)
                self.vis[curr_x][curr_y]=0

        curr_path.pop()


    def find_len_path(self,start_x,start_y,packman_pos):
        self.dfs(self.m, start_x,start_y,[])
        if(len(self.path)>0):
            least_path = self.path[0]
            for pth in self.path:
                if(len(least_path)>len(pth)):
                    least_path = pth
                
            # print(len(least_path),least_path)
            
            return len(least_path)
        else:
            return abs(packman_pos[0]-start_x)+abs(packman_pos[1]-start_y)+3


    def find_next(self,start_x,start_y):
        self.dfs(self.m, start_x,start_y,[])
        if(len(self.path)>1) and len(self.path[0])>1:
            # print("hi")
            least_path = self.path[0]
            for pth in self.path:
                if(len(least_path)>len(pth)):
                    least_path = pth
            # print("least path" ,least_path)

            if(len(least_path)==0):
                return ghosts().randomally_moves(tuple((start_x,start_y)), tuple((self.N,self.M)))
            else:
                return tuple(least_path[1])
        else:
            return ghosts().randomally_moves(tuple((start_x,start_y)), tuple((self.N,self.M)))






class ghosts:
    def __init__(self):
        pass

    def move_ghosts(
        self, pos_ghosts1, pos_ghosts2, board, board_size,pacman_pos, random=True, action=None
    ) -> Tuple:
        

        if(random):
            if(r.random() < 1):
                new_pos_ghosts1 = dfs_class(board, board_size,pacman_pos).find_next(pos_ghosts1[0],pos_ghosts1[1])
                new_pos_ghosts2 = dfs_class(board, board_size,pacman_pos).find_next(pos_ghosts2[0],pos_ghosts2[1])
            else:
                new_pos_ghosts1 = self.randomally_moves(pos_ghosts1, board_size, random, action)
                new_pos_ghosts2 = self.randomally_moves(pos_ghosts2, board_size, random, action)

        else:
            new_pos_ghosts1 = self.randomally_moves(pos_ghosts1, board_size, random, action)
            new_pos_ghosts2 = self.randomally_moves(pos_ghosts2, board_size, random, action)
        # new_pos_ghosts2 = self.randomally_moves(pos_ghosts2, board_size, random, action)

        if self._is_not_possible(new_pos_ghosts1, board, board_size):
            new_pos_ghosts1 = pos_ghosts1

        if self._is_not_possible(new_pos_ghosts2, board, board_size):
            new_pos_ghosts2 = pos_ghosts2

        return {"ghosts1": new_pos_ghosts1, "ghosts2": new_pos_ghosts2}
    


    def randomally_moves(self, pos, board_size, random=True, action=None) -> Tuple:
        ways = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

        if random:
            way_key = r.choice(list(ways.keys()))
            way = ways[way_key]

            x, y = pos
            new_x = x + way[0]
            new_y = y + way[1]

        else:
            x, y = pos
            way = ways[action]
            new_x = x + way[0]
            new_y = y + way[1]

        if 0 <= new_x < board_size[0] and 0 <= new_y < board_size[1]:
            """
            Here it is removed from the game screen,
            so it is better to stay in place
            """

            return (new_x, new_y)
        else:
            return pos

    def _is_not_possible(self, pos, board, board_size) -> True:
        x, y = pos
        if 0 <= x < board_size[0] and 0 <= y < board_size[1] and board[x][y] not in {"-", "|"}:
            return False
        else:
            return True
