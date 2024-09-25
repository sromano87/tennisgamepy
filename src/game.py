from src.player import Player
from src.errors import DuplicatedPlayerError
from src.errors import GameHasAlreadyBeenWonError

ADVANTAGE = 'Advantage'
DEUCE = 'Deuce'
SPACE = ' '
DASH = '-'
WINS = 'wins'


class Game:
    """
    This class is meant to be used as follows:
    game = Game("Federer", "Nadal")
    player_name_1 = game.get_player1_name()
    player_name_2 = game.get_player2_name()
    game.increment_player_score(player_name_1)
    game.increment_player_score(player_name_2)
    game.increment_player_score(player_name_1)
    game.increment_player_score(player_name_1)
    game.increment_player_score(player_name_1)
    status = game.get_game_status()
    """

    def __init__(self, player_name_1: str, player_name_2: str):
        """
        Creates a game given the names of two players. At the beginning the two
        players have a score equal to zero.
        :param player_name_1: the name of the first player
        :param player_name_2: the name of the second player
        :raise DuplicatedPlayerError if the two players have the same name.
        """
        if player_name_1 == player_name_2:
            raise DuplicatedPlayerError

        self._player1 = Player(player_name_1, 0)
        self._player2 = Player(player_name_2, 0)
        self._game_status = ''
        self._update_game_status()

    def get_game_status(self) -> str:
        return self._game_status

    def get_player1_name(self) -> str:
        """
        Returns the name of the first player.
        :return: the name
        """
        return self._player1.get_name()

    def get_player2_name(self) -> str:
        """
        Returns the name of the second player.
        :return: the name
        """
        return self._player2.get_name()

    def increment_player_score(self, player_name: str) -> None:
        """
        Increments the score of a given player. Once the score has been incremented,
        this method updates the current status of this game.
        :param player_name: the name of player whose score should be incremented
        :raise GameHasAlreadyBeenWonError if there is already a winner
        """
        if not self._is_there_a_winner():
            if player_name == self.get_player1_name():
                self._player1.increment_score()
            elif player_name == self.get_player2_name():
                self._player2.increment_score()
            self._update_game_status()
        else:
            raise GameHasAlreadyBeenWonError

    def _update_game_status(self) -> None:
        if self._is_deuce():
            result = DEUCE
        elif self._is_there_an_advantage_player():
            result = ADVANTAGE + SPACE + self._advantage_player().get_name()
        elif self._is_there_a_winner():
            result = self._the_winner().get_name() + SPACE + WINS
        else:
            result = self.get_player1_name() + SPACE + self._player1.get_score_as_string()
            result += SPACE + DASH + SPACE
            result += self.get_player2_name() + SPACE + self._player2.get_score_as_string()
        self._game_status = result

    def _is_there_an_advantage_player(self) -> bool:
        return self._advantage_player() is not None

    def _advantage_player(self) -> Player:
        result = None

        if self._player2.has_at_least_forty_points() and self._player1.has_at_least_forty_points():
            if self._player1.has_one_point_advantage_on(self._player2):
                result = self._player1
            elif self._player2.has_one_point_advantage_on(self._player1):
                result = self._player2

        return result

    def _is_deuce(self):
        return self._player1.is_tied_with(self._player2) and self._player1.has_at_least_forty_points()

    def _is_there_a_winner(self) -> bool:
        return self._the_winner() is not None

    def _the_winner(self) -> Player:
        winner = None

        if self._player1.has_more_than_forty_points() and self._player1.has_at_least_two_points_advantage_on(self._player2):
            winner = self._player1
        elif self._player2.has_more_than_forty_points() and self._player2.has_at_least_two_points_advantage_on(self._player1):
            winner = self._player2

        return winner

