from typing import Tuple, List
import random as r




class game:

    def __init__(
        self,
        size_board=(9, 18),
        number_of_wall=30,
        chor_position=(6,14),
        police1_position=None,
        police2_position=None,
        score=0
    ) -> None:
        self.size_board = size_board
        self.number_of_wall = number_of_wall
        self.chor_position = chor_position
        self.police1_position = (6, 10)
        self.police2_position = (6,9)
        self.score = score
        self.num_nodes_explored = 0


        self.board = None
        self.create_board_game()

    def get_score(self) -> int:
        return self.score

    def get_pos_chor(self) -> Tuple:
        return self.chor_position

    def get_pos_police(self, choice: int) -> Tuple:
        if choice == 1:
            return self.police1_position
        elif choice == 2:
            return self.police2_position

    def get_board(self) -> List:
        return self.board

    def set_board(self, board) -> None:
        self.board = board

    def set_pos_chor(self, new_pos) -> None:
        self.chor_position = new_pos

    def set_pos_police(self, choice: int, new_pos) -> Tuple:
        if choice == 1:
            self.police1_position = new_pos
        elif choice == 2:
            self.police2_position = new_pos

    def set_score(self, score):
        self.score = score

    def get_size(self):
        return self.size_board

    def create_board_game(self) -> None:
        self.board =   [['*', '|', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '-'],
                        ['*', '|', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                        ['*', '|', '*', '|', '*', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '*', '*', '*'],
                        ['*', '*', '*', '|', '*', '*', '*', '*', '*', '*', '*', '|', '*', '*', '*', '*', '*', '*'], 
                        ['|', '*', '*', '-', '-', '-', '-', '*', '*', '*', '*', '*', '*', '*', '*', '*', '|', '*'], 
                        ['|', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '|', '*'], 
                        ['*', '*', '*', '*', '-', '-', '*', '*', '-', '*', '|', '*', '*', '*', '*', '*', '|', '*'], 
                        ['*', '-', '*', '*', '|', '*', '*', '*', '*', '*', '|', '*', '*', '*', '-', '-', '-', '*'], 
                        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '|', '*', '*', '*', '*', '*', '*', '*']]
        # self.board = [
        #     ["*" for _ in range(self.size_board[1])] for _ in range(self.size_board[0])
        # ]

        # counter = 1
        # while counter <= self.number_of_wall:
        #     i, j = r.randint(0, self.size_board[0] - 1), r.randint(
        #         0, self.size_board[1] - 1
        #     )
        #     if (
        #         (i, j) == self.chor_position
        #         or (i, j) == self.police1_position
        #         or (i, j) == self.police2_position
        #         or self.board[i][j] == "-"
        #     ):
        #         continue

        #     self.board[i][j] = "-"
        #     counter += 1

        # del counter

    def display(self, score: int) -> None:
        
        for x in range(self.size_board[0]):
            for y in range(self.size_board[1]):
                if (x, y) == self.chor_position:
                    print("P", end=" ")
                elif (x, y) == self.police1_position:
                    print("G", end=" ")
                elif (x, y) == self.police2_position:
                    print("G", end=" ")
                else:
                    print(self.board[x][y], end=" ")
            print()
        print(f"                                                Score: {self.score}")

    def get_pos_chor(self) -> Tuple:
        return self.chor_position

    def get_pos_police(self, choice: int) -> Tuple:
        if choice == 1:
            return self.police1_position
        elif choice == 2:
            return self.police2_position
        
    def incriment_num_nodes(self):
        self.num_nodes_explored+=1
