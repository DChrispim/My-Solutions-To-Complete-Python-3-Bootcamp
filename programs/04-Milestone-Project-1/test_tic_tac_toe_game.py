import unittest
from unittest.mock import patch
from tic_tac_toe_game import *

class TestTicTacToeGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['X', 'O'])
    def test_player_input(self, mock_input):
        # Test player input function with mocked input
        player1_marker, player2_marker = player_input()
        self.assertEqual(player1_marker, 'X')
        self.assertEqual(player2_marker, 'O')

    def test_win_check(self):
        # Test win check function
        # Test horizontal wins
        horizontal_wins = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        for win in horizontal_wins:
            board = [' '] * 10
            for i in range(3):
                board[win[i]] = 'X'
            self.assertTrue(win_check(board, 'X'))

        # Test vertical wins
        vertical_wins = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        for win in vertical_wins:
            board = [' '] * 10
            for i in range(3):
                board[win[i]] = 'O'
            self.assertTrue(win_check(board, 'O'))

        # Test diagonal wins
        diagonal_wins = [
            [1, 5, 9],
            [3, 5, 7]
        ]
        for win in diagonal_wins:
            board = [' '] * 10
            for i in range(3):
                board[win[i]] = 'X'
            self.assertTrue(win_check(board, 'X'))

        # Test no win condition
        board = [' '] * 10
        board[1], board[2], board[3] = 'X', 'O', 'X'
        self.assertFalse(win_check(board, 'X'))

    def test_full_board_check(self):
        # Test full board check function
        # Test when the board is full
        board = ['X'] * 10
        self.assertTrue(full_board_check(board))
        # Test when the board is not full
        board[1] = ' '
        self.assertFalse(full_board_check(board))

    @patch('builtins.input', side_effect=[5, 1, 2, 3, 4])
    def test_player_choice(self, mock_input):
        # Test player choice function with mocked input
        board = [' '] * 10
        position = player_choice(board)
        self.assertEqual(position, 5)
        position = player_choice(board)
        self.assertEqual(position, 1)
        position = player_choice(board)
        self.assertEqual(position, 2)
        position = player_choice(board)
        self.assertEqual(position, 3)
        position = player_choice(board)
        self.assertEqual(position, 4)

    # Add more test functions as needed

if __name__ == '__main__':
    unittest.main()
