# poker-sim
Python implementation of a Texas Hold'em Monte Carlo Simulator

This project provides a Monte Carlo simulator for Texas Hold'em hands.
It requires as input a number of iterations to run, as well as two 2-card Texas Hold'em hands.
You must also specify the community cards. You may specify each card, or allow the program to simulate them.

The program outputs how many times each hand won during the Monte Carlo simulation in absolute terms as well as percentage.

Program Help:

Jeremys-Computer> python pokersim.py --help
usage: pokersim.py [-h] [--hand1 HAND1] [--hand2 HAND2]
                   [--community COMMUNITY]
                   num_iterations

Run a Monte Carlo simulation of a Texas Hold'em Poker Hand

positional arguments:
  num_iterations        Number of simulations to run. For accurate results,
                        run at least 1000 simulations.

optional arguments:
  -h, --help            show this help message and exit
  --hand1 HAND1         Hand 1 in format [rank][suit], example AcTd
  --hand2 HAND2         Hand 2 in format [rank][suit], example Qh5s
  --community COMMUNITY
                        Community cards in format [rank][suit], example
                        AdTsXxXxXx. You may use Xx for up to five simulated
                        cards

Sample Run (using examples from --help):
Jeremys-Computer> python pokersim.py --hand1 AcTd --hand2 Qh5s --community AdTsXxXxXx 1000
Total Hands: 1000
Hand1: 929 Hand2: 66 Ties: 5
Hand1: 92.90% Hand2: 6.60% Ties: 0.50%

The program also includes a test suite (test-pokersim.py) to validate that comparisons are working.
It is intended to be run with nosetests:

Jeremys-Computer> nosetests -v
test_best_five (test-pokersim.TestPokerSim) ... ok
test_check_flush (test-pokersim.TestPokerSim) ... ok
test_check_straight (test-pokersim.TestPokerSim) ... ok
test_check_straightflush (test-pokersim.TestPokerSim) ... ok
test_compare_hands (test-pokersim.TestPokerSim) ... ok
test_fourofakind (test-pokersim.TestPokerSim) ... ok
test_fullhouse (test-pokersim.TestPokerSim) ... ok
test_hand_copy (test-pokersim.TestPokerSim) ... ok
test_hand_to_numeric (test-pokersim.TestPokerSim) ... ok
test_highest_card (test-pokersim.TestPokerSim) ... ok
test_highest_card_straight (test-pokersim.TestPokerSim) ... ok
test_onepair (test-pokersim.TestPokerSim) ... ok
test_readable_hand (test-pokersim.TestPokerSim) ... ok
test_threeofakind (test-pokersim.TestPokerSim) ... ok
test_twopair (test-pokersim.TestPokerSim) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.008s

OK
