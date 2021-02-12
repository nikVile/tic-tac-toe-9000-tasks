from copy import deepcopy
from typing import Callable, List, Optional
from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    """Наследуемся от абстрактного класса и реализуем ручками все методы"""

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Optional[Callable[[TicTacToeGameInfo], TicTacToeTurn]] = None) -> None:
        self._game_id = game_id
        self._first_player_id = first_player_id
        self._second_player_id = second_player_id
        self._winner_id = ""
        self._strategy = strategy
        self._turns: List[TicTacToeTurn] = []

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        raise NotImplementedError

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        raise NotImplementedError

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self._game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self._turns),
            first_player_id=self._first_player_id,
            second_player_id=self._second_player_id,
            winner_id=self._winner_id
        )
        for turn in self._turns:
            if turn.player_id == self._first_player_id:
                symb = "X"
            else:
                symb = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = symb
        return result
