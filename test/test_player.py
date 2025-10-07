from unittest import TestCase

from src.player import Player


class TestPlayer(TestCase):

    def test_get_name(self):
        #Arrange
        player = Player("Sinner", 0)
        #Act
        name = player.get_name()
        #Assert
        self.assertEqual("Sinner", name)

    def test_get_score(self):
        # Arrange
        player = Player("Sinner", 2)
        # Act
        score = player.get_score()
        # Assert
        self.assertEqual(2, score)

    def test_set_name(self):
        #Arrange
        player = Player("Sinner", 0)
        #Act
        player.set_name("Alcaraz")
        name = player.get_name()
        #Assert
        self.assertEqual("Alcaraz", name)

    def test_set_score(self):
        #Arrange
        player = Player("Sinner", 0)
        #Act
        player.set_score(3)
        score = player.get_score()
        #Assert
        self.assertEqual(3, score)

    def test_increment_score(self):
        # Arrange
        player = Player("Sinner", 0)
        # Act
        player.increment_score()
        score = player.get_score()
        #Assert
        self.assertEqual(1, score)

    def test_get_score_as_string_love(self):
        # Arrange
        player = Player("Sinner", 0)
        # Act
        score_as_string = player.get_score_as_string()
        #Assert
        self.assertEqual("love", score_as_string)

    def test_get_score_as_string_none(self):
        # Arrange
        player = Player("Sinner", 4)
        # Act
        score_as_string = player.get_score_as_string()
        # Assert
        self.assertIsNone(score_as_string)

    def test_there_is_a_tie(self):
        # Arrange
        player1 = Player("Sinner", 2)
        player2 = Player("Alcaraz", 2)
        # Act
        tie = player1.is_tied_with(player2)
        # Assert
        self.assertTrue(tie)

    def test_there_is_not_a_tie(self):
        # Arrange
        player1 = Player("Sinner", 3)
        player2 = Player("Alcaraz", 2)
        # Act
        tie = player1.is_tied_with(player2)
        # Assert
        self.assertFalse(tie)

    def test_has_at_least_forty_points(self):
        # Arrange
        player = Player("Sinner", 3)
        # Act
        forty_points = player.has_at_least_forty_points()
        # Assert
        self.assertTrue(forty_points)

    def test_does_not_has_at_least_forty_points(self):
        # Arrange
        player = Player("Sinner", 2)
        # Act
        forty_points = player.has_at_least_forty_points()
        # Assert
        self.assertFalse(forty_points)


