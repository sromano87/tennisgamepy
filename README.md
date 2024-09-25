# tennisgamepy

The _tennisgamepy_ program consists of an API for keeping the score a tennis game. In particular, it allows creating a new game, updating the score of the game, and returning the current status of the game -- i.e., a string that summarizes the score of the game (see the examples below).

The rules of a tennis game can be summarized as follows:
*	A game is won by the first player that has at least four points in total and at least two points more than the opponent. If this happens, the game status is, for example, _“Federer wins”_.
*	The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as “love”, “fifteen”, “thirty”, and “forty” respectively. Examples of game status are: _“Federer fifteen - Nadal love”_ or _“Federer thirty - Nadal thirty”_.
*	If at least three points have been scored by each player and the scores are equal, the score is “deuce”. In this case, the game status is simply _“Deuce”_.
*	If at least three points have been scored by each side and a player has one point more than his opponent, the score of the game is “advantage” for the player in the lead. An example of such a game status is _“Advantage Federer”_.
