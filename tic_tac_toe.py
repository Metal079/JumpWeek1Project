import random

BOARD = {7: '7',  8: '8',  9: '9',

         4: '4',  5: '5',  6: '6',

         1: '1',  2: '2',  3: '3'}

mode = None


def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''

    print(f" {BOARD[7]} | {BOARD[8]} | {BOARD[9]} ")
    print(" - + - + - ")
    print(f" {BOARD[4]} | {BOARD[5]} | {BOARD[6]} ")
    print(" - + - + - ")
    print(f" {BOARD[1]} | {BOARD[2]} | {BOARD[3]} ")


def get_action(player, available_moves):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    if player == 'O' and mode == 'S':
        print(f"Computer is choosing a move...")
        action = available_moves[random.randint(0, len(available_moves) - 1)]
        available_moves.remove(action)
    else:
        action = int(input(
            f"Player {player}, please choose a number between 1 and 9 to indicate where to place your move: "))
        while action not in available_moves:
            action = int(input(
                f"Player {player}, please choose a number between 1 and 9 to indicate where to place your move: "))
        available_moves.remove(action)

    return action


def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    print(f"Player {player} wins!")
    render()
    with open('log.txt', 'a') as f:
        f.write("------------------------\n")
        f.write("TicTacToe\n")
        f.write("------------------------\n")
        f.write(f"Player {player} wins!\n")
        f.write(f" {BOARD[7]} | {BOARD[8]} | {BOARD[9]} \n")
        f.write(" - + - + - \n")
        f.write(f" {BOARD[4]} | {BOARD[5]} | {BOARD[6]} \n")
        f.write(" - + - + - \n")
        f.write(f" {BOARD[1]} | {BOARD[2]} | {BOARD[3]} \n")


def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    winning_combinations = [
        [7, 8, 9], [4, 5, 6], [1, 2, 3],
        [7, 4, 1], [8, 5, 2], [9, 6, 3],
        [1, 5, 9], [3, 5, 7]
    ]

    if any(all(BOARD[position] == player for position in combination) for combination in winning_combinations):
        victory_message(player)
        return True

    return False


def player_turn(player, game_round, available_moves):
    # Print the current state of the board
    render()

    # Get the current player's action and assign it to a variable called 'action'.
    action = get_action(player, available_moves)

    # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
    BOARD[action] = player

    # Check if the game is winnable (game_round >= 4),
    # then check for win conditions (check_win(player)),
    # and if there's a win, end the game (game_over = True),
    # and break the loop (break).
    if game_round >= 4:
        if check_win(player):
            return True

    # Check if there are any open spots left (game_round == 9),
    # and if there aren't, print a tie message,
    # end the game,
    # and break the loop.
    if len(available_moves) == 0:
        print("It's a tie!")
        with open('log.txt', 'a') as f:
            f.write("------------------------\n")
            f.write("TicTacToe\n")
            f.write("------------------------\n")
            f.write("It's a tie!")
            f.write(f" {BOARD[7]} | {BOARD[8]} | {BOARD[9]} \n")
            f.write(" - + - + - \n")
            f.write(f" {BOARD[4]} | {BOARD[5]} | {BOARD[6]} \n")
            f.write(" - + - + - \n")
            f.write(f" {BOARD[1]} | {BOARD[2]} | {BOARD[3]} \n")
        return True


def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    player_1 = 'X'
    player_2 = 'O'
    game_round = 0
    game_over = False
    available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Ask for mode selection
    global mode
    mode = input(
        "Would you like to play against a single-player or the multi-layer? (S/M) ").upper()
    while mode != "S" and mode != "M":
        print("Invalid input. Please enter 'S' or 'M'.")
        mode = input(
            "Would you like to play against a single-player or the multi-layer? (S/M) ")

    # Game loop
    while not game_over:
        game_round += 1
        if player_turn(player_1, game_round, available_moves):
            break

        game_round += 1
        if player_turn(player_2, game_round, available_moves):
            break

    # prompt for a restart and assign the input to a 'restart' variable.
    restart = input("Would you like to play again? (Y/N) ").upper()
    while restart != "Y" and restart != "N":
        restart = input("Would you like to play again? (Y/N) ")
    if restart == "Y":
        for key in BOARD:
            BOARD[key] = key
        play_t3()
    else:
        print("Thanks for playing!")
        return
