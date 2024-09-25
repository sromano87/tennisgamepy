class Player:

    _score_map = {
        0: 'love',
        1: 'fifteen',
        2: 'thirty',
        3: 'forty'
    }

    def __init__(self, name: str, score: int = 0):
        """
        Creates a player given its name and score
        :param name: the name of the player
        :param score: the score of the player
        """
        self._name = name
        self._score = score

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_score(self) -> int:
        return self._score

    def set_score(self, score: int) -> None:
        self._score = score

    def increment_score(self) -> None:
        """
        Increments the score of this player by one unit.
        """
        self._score += 1

    def get_score_as_string(self) -> str:
        """
        Translates the score of this player into a string that is peculiar to tennis.
        That is, 0 is translated into "love", 1 is translated into "fifteen", 2 is
        translated into "thirty", and 3 is translated into "forty".
        :return: the translation of the score as a string (or None if there is no translation).
        """
        return Player._score_map.get(self._score)

    def is_tied_with(self, opponent: 'Player') -> bool:
        """
        Returns if there is a tie between this player and the opponent.
        :param opponent: the opponent
        :return: True if there is a tie, False otherwise.
        """
        return self._score == opponent.get_score()

    def has_at_least_forty_points(self) -> bool:
        """
        Returns if this player has at least "forty" points.
        :return: True if this player has at least "forty" points, False otherwise.
        """
        return self._score >= 3

    def has_less_than_forty_points(self) -> bool:
        """
        Returns if this player has less than "forty" points.
        :return: True if this player has less than "forty" points, False otherwise.
        """
        return self._score < 3

    def has_more_than_forty_points(self) -> bool:
        """
        Returns if this player has more than "forty" points.
        :return: True if this player has more than "forty" points, False otherwise.
        """
        return self._score > 3

    def has_one_point_advantage_on(self, opponent: 'Player') -> bool:
        """
        Returns if this player has one point of advantage on the opponent.
        :param opponent: the opponent
        :return: True if this player has one point of advantage, False otherwise.
        """
        return self._score - opponent.get_score() == 1

    def has_at_least_two_points_advantage_on(self, opponent: 'Player') -> bool:
        """
        Returns if this player has at least two points of advantage on the opponent.
        :param the opponent:
        :return: True if this player has at least two points of advantage, False otherwise
        """
        return self._score - opponent.get_score() >= 2
