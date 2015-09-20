elo2.py -- Computes expected outcomes of a 3-game series between a number of players. Inputs are the following information about
the distribution of the possible Elos of the players: (1) Means; (2) Standard deviations; (3) Covariance. The Elos of any two
players are assumed to be binormally distributed according to these variables.

A single line of the input file should look like <M1> <M2> <S1> <S2> <C>, where M1 and M2 are the means of the two players, S1 and S2 are the _squares_ of the standard deviations of these players, and C is the covariance of the elos of these two players. The input fields should be separated by tab ('\t') characters. (This code is designed to work with copy-paste from a google sheet.) The output will be a list of lines <P30> <P21> <P12> <P03>, where P30 is the probability that player 1 wins 3-0 against player 2, etc.

CEloRatingCUI.cpp -- A small change to a file in Remi Coulom's Bayesian Elo estimator (http://www.remi-coulom.fr/Bayesian-Elo/) that allows printing of the covariance matrix (the command printcovariance in the elo calculator). Was using this to get more accurate predictions of 3-game match outcomes (which may tend more toward even outcomes when Elos are positively correlated).

Bayeselo is distributed under the GNU General Public License, as are all files in this repository.