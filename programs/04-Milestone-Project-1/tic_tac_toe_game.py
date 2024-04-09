'''
# Simple Tic Tac Toe game for two players

By Breno D. Chrispim - https://github.com/DChrispim

Task: Create a Tic Tac Toe game.

Requirements:

* 2 players should be able to play the game (both sitting at the same computer)
* The board should be printed out every time a player makes a move
* You should be able to accept input of the player position and then place a symbol on the board
'''

# Imports
import random
from IPython.display import clear_output
import os
import time

# Functions
def clear_board():
    '''
    Function that clears the output, uses different function depending on the environment
    '''
    try:
        # Check if running in IPython environment
        ipython = get_ipython()
        if ipython is not None:
            # Execute in IPython environment
            time.sleep(1)
            clear_output(wait=True)
    except NameError:
        # Execute in Python terminal
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


def display_board(board):
    '''
    Clear the output and print the board
    Input: board 10 spaces list
    '''
    clear_board()
    print(board[1:4])
    print(board[4:7])
    print(board[7:10])


def player_input():
    '''
    Input: Player input, choice between X and O.
    Output: (Player 1 marker, Player 2 marker)
    '''
    # This original choice value can be anything that isn't an integer
    choice_X_or_O = 'wrong'

    # While the choice is not a digit, keep asking for input.
    while choice_X_or_O not in ['O', 'X']:

        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice_X_or_O = input("Player 1, choose X or O:").upper()

        if choice_X_or_O not in ['O', 'X']:
            print("Sorry, Player 1 need to choose between O and X.")

    player1 = choice_X_or_O

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return str(board[position]).isnumeric()


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


if __name__ == '__main__':
    # Game logic
    print('Welcome to Tic Tac Toe!')

    while True:
        # Play the game

        # Set initial parameters
        # the_board = [" "]*10
        the_board = [i for i in range(0,10)]
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print(turn + " goes first")

        play_game = input("Ready to play? Yes or No?")
        if play_game == "Yes":
            game_on = True
        else:
            game_on = False

        while game_on:

            if turn == "Player 1":
                # Player 1 Turn

                # Display the current board
                display_board(the_board)

                # Choose a position and place the marker
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                # Check if won of tie
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print("Player 1 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Tie game!")
                        break
                    else:
                        # Next player turn
                        turn = "Player 2"

            else:
                # Player 2 Turn

                # Display the current board
                display_board(the_board)

                # Choose a position and place the marker
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                # Check if won of tie
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Tie game!")
                        break
                    else:
                        # Next player turn
                        turn = "Player 1"
        if not replay():
            break
