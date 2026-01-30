import unittest
from rps_game import normalize_input, decide_winner


class TestRPSGame(unittest.TestCase):

    def test_normalize_input_short(self):
        self.assertEqual(normalize_input("r"), "r")
        self.assertEqual(normalize_input("p"), "p")
        self.assertEqual(normalize_input("s"), "s")

    def test_normalize_input_words(self):
        self.assertEqual(normalize_input("rock"), "r")
        self.assertEqual(normalize_input("paper"), "p")
        self.assertEqual(normalize_input("scissors"), "s")

    def test_normalize_input_case_spaces(self):
        self.assertEqual(normalize_input("  Rock  "), "r")
        self.assertEqual(normalize_input(" PAPER "), "p")

    def test_normalize_input_invalid(self):
        with self.assertRaises(ValueError):
            normalize_input("invalid")

    def test_decide_winner_tie(self):
        self.assertEqual(decide_winner("r", "r"), "tie")

    def test_decide_winner_user_wins(self):
        self.assertEqual(decide_winner("r", "s"), "win")  # rock beats scissors
        self.assertEqual(decide_winner("p", "r"), "win")  # paper beats rock
        self.assertEqual(decide_winner("s", "p"), "win")  # scissors beats paper

    def test_decide_winner_user_loses(self):
        self.assertEqual(decide_winner("r", "p"), "lose")
        self.assertEqual(decide_winner("p", "s"), "lose")
        self.assertEqual(decide_winner("s", "r"), "lose")


if __name__ == "__main__":
    unittest.main()
