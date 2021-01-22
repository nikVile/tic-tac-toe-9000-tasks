from typing import Callable

from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame

class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None) -> None:
        pass

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        pass

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        pass

    def get_game_info(self) -> TicTacToeGameInfo:
        pass