from unittest import TestCase

from src.errors import DuplicatedPlayerError, GameHasAlreadyBeenWonError
from src.game import Game


class TestGame(TestCase):

    def test_dublicated_player_error_is_raised(self):
        self.assertRaises(DuplicatedPlayerError, Game, "Sinner", "Sinner")

    def test_get_player1_name(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        # Act
        name = game.get_player1_name()
        # Assert
        self.assertEqual("Sinner", name)

    def test_get_player2_name(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        # Act
        name = game.get_player2_name()
        # Assert
        self.assertEqual("Alcaraz", name)

    def test_game_status_at_the_beginning(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        # Act
        status = game.get_game_status()
        self.assertEqual("Sinner love - Alcaraz love", status)

    def test_first_player_wins(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Sinner wins", status)

    def test_second_player_wins(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Alcaraz wins", status)

    def test_fifteen_to_thirty(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Sinner fifteen - Alcaraz thirty", status)

    def test_forty_to_fifteen_(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Sinner forty - Alcaraz fifteen", status)

    def test_thirty_to_forty(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Sinner thirty - Alcaraz forty", status)

    def test_deuce(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Deuce", status)

    def test_deuce_after_advantage(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Deuce", status)

    def test_advantage_first_player(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Advantage Sinner", status)

    def test_advantage_second_player(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Advantage Alcaraz", status)

    def test_advantage_first_player_after_deuce(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Advantage Sinner", status)

    def test_advantage_second_player_after_deuce(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        player2 = game.get_player2_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player2)
        game.increment_player_score(player1)
        game.increment_player_score(player2)
        status = game.get_game_status()
        # Assert
        self.assertEqual("Advantage Alcaraz", status)

    def test_game_has_already_been_won_error(self):
        # Arrange
        game = Game("Sinner", "Alcaraz")
        player1 = game.get_player1_name()
        # Act
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        game.increment_player_score(player1)
        self.assertRaises(GameHasAlreadyBeenWonError, game.increment_player_score, player1)