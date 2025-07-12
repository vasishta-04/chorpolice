from utility import utility
from game import game
from polices import polices
import os
from typing import Tuple, List
import random as r



class chor:
    def __init__(self):
        self._ways_possible_for_polices = [
            "up",
            "down",
            "left",
            "right",
        ]
        self.num_nodes_exp =0 
        self.utility = utility()

    def _min_max(
        self, state, is_chor, depth, alpha=float("-inf"), beta=float("-inf")
    ) -> set:
        if self.utility.is_game_finished(state) or depth == 0:
            self.num_nodes_exp +=1
            return self.utility.get_utility(state)

        if is_chor:
            v = float("-inf")
            actions_values = [
                (action, self._min_max(self.transfer(state, action, 1), 0, depth - 1))
                for action in self._ways_possible_for_chor(state)
            ]
            v = max(actions_values, key=lambda x: x[1])[1]
            if v >= beta:
                return v
            alpha = max(alpha, v)
            return v
        else:
            actions_values = [
                (action, self._min_max(self.transfer(state, action, 0), 1, depth - 1))
                for action in self._ways_possible_for_polices
            ]
            v = min(actions_values, key=lambda x: x[1])[1]
            if v <= alpha:
                return v
            beta = min(beta, v)
            return v

    def best_action(self, state):
        actions_values = [
            (
                action,
                self._min_max(
                    self.transfer(create_copy_state(state), action, 1),
                    0,
                    depth=4,
                ),
            )
            for action in self._ways_possible_for_chor(state)
        ]
        best_word = max(actions_values, key=lambda temp: temp[1])
        best_action, best_score = best_word
        best_action = [
            elements[0] for elements in actions_values if elements[1] == best_score
        ]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nNumber of nodes explored - " ,self.num_nodes_exp)
        print()
        return r.choice(best_action)

    def transfer(self, state, action, is_chor):
        if is_chor:
            new_state = create_copy_state(state)
            xp, yp = state.get_pos_chor()

            board = state.get_board()
            board_size = state.get_size()
            new_pos_chor = self.moves_chor((xp, yp), action, board_size, board)
            new_state.set_pos_chor(new_pos_chor)
            return new_state

        else:
            G = polices()
            new_state = create_copy_state(state)
            pos_g1 = state.get_pos_police(1)
            pos_g2 = state.get_pos_police(2)

            board = state.get_board()
            board_size = state.get_size()

            new_pos_polices = G.move_polices(
                pos_g1, pos_g2, board, board_size, False, action,state.get_pos_chor()
            )

            new_pos_g1 = new_pos_polices["polices1"]
            new_pos_g2 = new_pos_polices["polices2"]

            new_state.set_pos_police(1, new_pos_g1)
            new_state.set_pos_police(2, new_pos_g2)

            return new_state

    def _ways_possible_for_chor(
        self,
        state,
    ) -> List:
        x, y = state.get_pos_chor()
        board = state.get_board()
        board_size = state.get_size()

        actions = []

        if x > 0 and board[x - 1][y] not in {"-", "|"}:
            actions.append("up")

        if x < board_size[0] - 1 and board[x + 1][y] not in {"-", "|"}:
            actions.append("down")

        if y > 0 and board[x][y - 1]  not in {"-", "|"}:
            actions.append("left")

        if y < board_size[1] - 1 and board[x][y + 1] not in {"-", "|"}:
            actions.append("right")
        return actions

    def moves_chor(self, chor_pos, way_posibale, board_size, board) -> set:
        x, y = chor_pos
        ways = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        dx, dy = ways[way_posibale]
        new_x = x + dx
        new_y = y + dy

        if (
            0 <= new_x < board_size[0]
            and 0 <= new_y < board_size[1]
            and board[x][y] not in {"-", "|"}
        ):
            return (new_x, new_y)

        else:
            chor_pos


def create_copy_state(state) -> game:
    new_board = game()
    new_board.set_pos_chor(state.get_pos_chor())
    new_board.set_pos_police(1, state.get_pos_police(1))
    new_board.set_pos_police(2, state.get_pos_police(2))
    new_board.set_score(state.get_score())
    new_board.set_board(state.get_board())
    return new_board
