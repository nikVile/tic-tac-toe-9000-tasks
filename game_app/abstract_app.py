from abc import ABC, abstractmethod

from game_engine import TicTacToeGameInfo, TicTacToeTurn
from .user_info import UserInfo


class AbstractTicTacToeApp(ABC):
    """Дискуссионный вопрос, нужен ли здесь вообще класс, но меня покусали джависты"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        """создаём игру, кладём в словарик (или другую вашу любимую коллекцию) с играми"""

    @abstractmethod
    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:
        """получаем игру, отдавать нужно только если юзер с таким user_id реально в неё играет,
        но проверку секретного ключа пользователя нужно делать в обработчиках запросов,
        а не здесь, но здесь мы реализуем методы, которые в этом помогут"""

    @abstractmethod
    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        pass

    @abstractmethod
    def add_user(self) -> UserInfo:
        """регистрация"""

    @abstractmethod
    def is_autentified(self, user: UserInfo) -> bool:
        """проверка авторизации"""
