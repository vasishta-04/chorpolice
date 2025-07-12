num_nodes =0
from chor import chor
from game import game
from polices import polices
from utility import utility

import time

FPS = 5
frame_time = 1.0 / FPS  


class play:
    def __init__(self) -> None:
        self.game = game()
        self.score = self.game.score
        self.polices = polices()
        self.state = self.game.get_board()
        self.utility = utility()
        self.chor = chor()
        self.prev_time = time.time()

    def start(self):
        while True:
            self.game.display(self.game.get_score())

            elapsed_time = time.time() - self.prev_time
            if elapsed_time < frame_time:
                sleep_time = max(0, frame_time - elapsed_time)  
                time.sleep(sleep_time)
            self.prev_time = time.time()
            
            # print(self.game.chor_position,self.game.police1_position)
            # print(self.game.num_nodes_explored,self.utility.num_nodes)

            if self.game.chor_position == self.game.police1_position and self.game.chor_position == self.game.police2_position:
                print(self.game.chor_position,self.game.police1_position,"dfonigf")
                print("chor is caught by a police!")
                break

            if self.utility.is_game_finished(self.game):
                if self.utility.is_chor_win(self.game):
                    print("** chor IS WIN !!!")
                else:
                    print("chor LOST !")
                    break
            best_action = self.chor.best_action(self.game)
            new_pos_chors = self.chor.moves_chor(
                self.game.get_pos_chor(),
                best_action,
                self.game.get_size(),
                self.game.get_board(),
            )

            self.game.set_pos_chor(new_pos_chors)

            pos_g1 = self.game.get_pos_police(1)
            pos_g2 = self.game.get_pos_police(2)

            self.game.score -= 1

            poses = self.polices.move_polices(
                pos_g1, pos_g2, self.game.get_board(), self.game.get_size(),self.game.get_pos_chor()
            )

            self.game.set_pos_police(1, poses["polices1"])
            self.game.set_pos_police(2, poses["polices2"])

            # if self.game.get_pos_chor() == self.game.get_pos_police(
            #     1
            # ) or self.game.get_pos_chor() == self.game.get_pos_police(2):
            #     print("chor is caught by a police!")
            #     break

            if (
                self.game.get_board()[self.game.get_pos_chor()[0]][
                    self.game.get_pos_chor()[1]
                ]
                == "*"
            ):
                self.game.score += 10
                board = self.game.get_board()
                board[self.game.get_pos_chor()[0]][
                    self.game.get_pos_chor()[1]
                ] = " "
                self.game.set_board(board)

            

play().start()
