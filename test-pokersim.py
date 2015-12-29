##
# test-pokersim.py
#
# Tests
#   check hand logic
#   check readable_hand, hand_to_numeric
#   check best_five
#   valid_hand

import unittest
import pokersim


class TestPokerSim(unittest.TestCase):

    def test_readable_hand(self):
        self.assertEqual("Qd3c3d3h3s",
                         pokersim.readable_hand([[10, 1], [1, 0],
                                                [1, 1], [1, 2], [1, 3]]))
        self.assertEqual("As2cAh2d3d",
                         pokersim.readable_hand([[12, 3], [0, 0],
                                                 [12, 2], [0, 1], [1, 1]]))
        self.assertEqual("2c3d4h5s7c",
                         pokersim.readable_hand([[0, 0], [1, 1],
                                                [2, 2], [3, 3], [5, 0]]))

    def test_hand_to_numeric(self):
        hand = pokersim.hand_to_numeric("AcAdAhAsKc")
        self.assertEqual([[12, 3], [12, 2], [12, 1], [12, 0], [11, 0]], hand)

    def test_hand_copy(self):
        hand = [[12, 3], [12, 2], [12, 1], [12, 0], [11, 0]]
        hand2 = pokersim.hand_copy(hand)
        self.assertEqual(hand, hand2)

    def test_best_five(self):
        p1_cards = [[12, 3], [12, 2]]
        community_cards = [[12, 1], [12, 0], [11, 0], [5, 2], [6, 1]]
        hand = pokersim.best_five(p1_cards, community_cards)
        self.assertEqual([[12, 3], [12, 2], [12, 1], [12, 0], [11, 0]], hand)

    def test_check_straightflush(self):
        hand = pokersim.hand_to_numeric("AcKcQcJcTc")
        self.assertTrue(pokersim.check_straightflush(hand))
        hand = pokersim.hand_to_numeric("7c6c5c4c3c")
        self.assertTrue(pokersim.check_straightflush(hand))
        hand = pokersim.hand_to_numeric("Ac5c4c3c2c")
        self.assertTrue(pokersim.check_straightflush(hand))
        hand = pokersim.hand_to_numeric("AcTc5c4c3c")
        self.assertFalse(pokersim.check_straightflush(hand))
        hand = pokersim.hand_to_numeric("7c6c5c4c3d")
        self.assertFalse(pokersim.check_straightflush(hand))

    def test_check_flush(self):
        hand = pokersim.hand_to_numeric("AcTc5c4c3c")
        self.assertTrue(pokersim.check_flush(hand))
        hand = pokersim.hand_to_numeric("AcTc5c4c3d")
        self.assertFalse(pokersim.check_flush(hand))

    def test_check_straight(self):
        hand = pokersim.hand_to_numeric("7c6d5c4c3c")
        self.assertTrue(pokersim.check_straight(hand))
        hand = pokersim.hand_to_numeric("Ac5c4c3c2d")
        self.assertTrue(pokersim.check_straight(hand))
        hand = pokersim.hand_to_numeric("AcTc5c4c3c")
        self.assertFalse(pokersim.check_straight(hand))

    def test_fourofakind(self):
        hand = pokersim.hand_to_numeric("Ad7c7d7h7s")
        self.assertTrue(pokersim.check_fourofakind(hand)[0])
        hand = pokersim.hand_to_numeric("5c5d5h5s2c")
        self.assertTrue(pokersim.check_fourofakind(hand)[0])
        hand = pokersim.hand_to_numeric("AcAd5c5h5s")
        self.assertFalse(pokersim.check_fourofakind(hand)[0])

    def test_fullhouse(self):
        hand = pokersim.hand_to_numeric("AdAc7d7h7s")
        self.assertTrue(pokersim.check_fullhouse(hand)[0])
        hand = pokersim.hand_to_numeric("5c5d5h3s3c")
        self.assertTrue(pokersim.check_fullhouse(hand)[0])
        hand = pokersim.hand_to_numeric("AcAd5c5h4s")
        self.assertFalse(pokersim.check_fullhouse(hand)[0])

    def test_threeofakind(self):
        hand = pokersim.hand_to_numeric("AdQc7d7h7s")
        self.assertTrue(pokersim.check_threeofakind(hand)[0])
        hand = pokersim.hand_to_numeric("5c5d5h3s2c")
        self.assertTrue(pokersim.check_threeofakind(hand)[0])
        hand = pokersim.hand_to_numeric("AcAd5c5h4s")
        self.assertFalse(pokersim.check_threeofakind(hand)[0])

    def test_twopair(self):
        hand = pokersim.hand_to_numeric("AdAc7d7h6s")
        self.assertTrue(pokersim.check_twopair(hand)[0])
        hand = pokersim.hand_to_numeric("5c5d4h3s3c")
        self.assertTrue(pokersim.check_twopair(hand)[0])
        hand = pokersim.hand_to_numeric("AcAd5c4h3s")
        self.assertFalse(pokersim.check_twopair(hand)[0])

    def test_onepair(self):
        hand = pokersim.hand_to_numeric("AdAc5d3h2s")
        self.assertTrue(pokersim.check_onepair(hand)[0])
        hand = pokersim.hand_to_numeric("5c5d4h3s2c")
        self.assertTrue(pokersim.check_onepair(hand)[0])
        hand = pokersim.hand_to_numeric("AcQd5c4h3s")
        self.assertFalse(pokersim.check_onepair(hand)[0])

    def test_highest_card(self):
        hand1 = pokersim.hand_to_numeric("AdQc5d3h2h")
        hand2 = pokersim.hand_to_numeric("KdQs5s3s2s")
        self.assertEqual(pokersim.highest_card(hand1,hand2), 0)
        self.assertEqual(pokersim.highest_card(hand2,hand1), 1)
        hand1 = pokersim.hand_to_numeric("KhQh5h3h2d")
        hand2 = pokersim.hand_to_numeric("KdQd5d3d2h")
        self.assertEqual(pokersim.highest_card(hand1,hand2), 2)
        self.assertEqual(pokersim.highest_card(hand2,hand1), 2)

    def test_highest_card_straight(self):
        hand1 = pokersim.hand_to_numeric("AdKcQdJhTs")
        hand2 = pokersim.hand_to_numeric("KdQcJdTh9s")
        self.assertEqual(pokersim.highest_card_straight(hand1,hand2), 0)
        self.assertEqual(pokersim.highest_card_straight(hand2,hand1), 1)
        hand1 = pokersim.hand_to_numeric("Ad5d4c3h2s")
        hand2 = pokersim.hand_to_numeric("KdQcJdTh9s")
        self.assertEqual(pokersim.highest_card_straight(hand1,hand2), 1)
        self.assertEqual(pokersim.highest_card_straight(hand2,hand1), 0)
        hand1 = pokersim.hand_to_numeric("Ad5d4c3h2s")
        hand2 = pokersim.hand_to_numeric("KdQcJdTh9s")
        self.assertEqual(pokersim.highest_card_straight(hand1,hand2), 1)
        self.assertEqual(pokersim.highest_card_straight(hand2,hand1), 0)

    def test_compare_hands(self):
        # higher straight flush, lower straight flush
        hand1 = pokersim.hand_to_numeric("AdKcQdJhTs")
        hand2 = pokersim.hand_to_numeric("KdQcJdTh9s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # 5-high straight flush, K-high straight flush
        hand1 = pokersim.hand_to_numeric("Ad5d4c3h2s")
        hand2 = pokersim.hand_to_numeric("KdQcJdTh9s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 1)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 0)
        # A-high hand, K-high hand
        hand1 = pokersim.hand_to_numeric("AdQc5d3h2h")
        hand2 = pokersim.hand_to_numeric("KdQs5s3s2s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # K-high hands, 3rd kicker 6 vs 5
        hand1 = pokersim.hand_to_numeric("KhQh6h3h2d")
        hand2 = pokersim.hand_to_numeric("KdQd5d3d2h")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # Equal K-high hands
        hand1 = pokersim.hand_to_numeric("KhQh5h3h2d")
        hand2 = pokersim.hand_to_numeric("KdQd5d3d2h")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 2)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 2)
        # A-high flush vs 7-high straight flush
        hand1 = pokersim.hand_to_numeric("AcKcQcJc9c")
        hand2 = pokersim.hand_to_numeric("7c6c5c4c3c")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 1)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 0)
        # four of a kind vs. full house
        hand1 = pokersim.hand_to_numeric("AcAdAhAs9c")
        hand2 = pokersim.hand_to_numeric("7c7d7h4c4s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # four of a kind vs. full house
        hand1 = pokersim.hand_to_numeric("AcAdAh9s9c")
        hand2 = pokersim.hand_to_numeric("7c7d7h7s4s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 1)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 0)
        # Q-high full house, 7-high full house
        hand1 = pokersim.hand_to_numeric("QcQdQh9s9c")
        hand2 = pokersim.hand_to_numeric("KsKs7c7d7h")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # 7-high full house, A-high trips
        hand1 = pokersim.hand_to_numeric("AcAdAh9s8c")
        hand2 = pokersim.hand_to_numeric("KsKs7c7d7h")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 1)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 0)
        # 7-high trips, A-high trips
        hand1 = pokersim.hand_to_numeric("AcAdAh9s8c")
        hand2 = pokersim.hand_to_numeric("KsQs7c7d7h")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # A-high four-of-a-kind, K-high straight flush
        hand1 = pokersim.hand_to_numeric("AcAdAhAs9c")
        hand2 = pokersim.hand_to_numeric("KdQdJdTd9d")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 1)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 0)
        # A-high four-of-a-kind, K-high straight
        hand1 = pokersim.hand_to_numeric("AcAdAhAs9c")
        hand2 = pokersim.hand_to_numeric("KdQdJdTd9s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # 5-high four-of-a-kind, K-high straight
        hand1 = pokersim.hand_to_numeric("5c5d5h5s9c")
        hand2 = pokersim.hand_to_numeric("KdQdJdTd9s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 0)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 1)
        # 5-high four-of-a-kind, T-high four-of-a-kind
        hand1 = pokersim.hand_to_numeric("5c5d5h5s9c")
        hand2 = pokersim.hand_to_numeric("TcTdThTs6s")
        self.assertEqual(pokersim.compare_hands(hand1,hand2), 1)
        self.assertEqual(pokersim.compare_hands(hand2,hand1), 0)


if __name__ == '__main__':
    unittest.main()
