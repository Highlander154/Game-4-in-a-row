from colorama import init, Back, Fore, Style  # colorama used for color formatting the board in the console

VER = '0.1.1'
VER_DATE = '09.02.2022'
BOARD_WIDTH = 7  # Default board width: 7
BOARD_HEIGHT = 6  # Default board height: 6
NUM_TO_CONNECT = 4  # default num to connect: 4

# Setup playing board
init(autoreset=True)  # Initializes colorama
empty_slot = ' '  # Representing an empty slot in the board

player_1 = Style.BRIGHT + Fore.BLUE + 'o' + Style.RESET_ALL  # set player 1 icon
player_2 = Style.BRIGHT + Fore.RED + 'o' + Style.RESET_ALL  # set player 2 icon


def create_board(slot: str = ' ', width: int = 7, height: int = 6):
    row_ph = [slot for _ in range(width)]  # create a row placeholder
    board = [row_ph[:] for _ in range(height)]  # create board with row placeholders
    return board


def print_board(game_board: list, width: int = 7, height: int = 6):
    print("\nBOARD REPRESENTATION\n")
    print("|", end='')
    for col in range(width):
        print(col, end='|')
    print()

    for row in range(height):
        print("|", end='')
        for col in game_board[row]:
            print(col, end='|')
        print()
    print('--' * width + '-')


def is_win(player: str, game_board: list):
    placeholder_win_line = Style.BRIGHT + Back.LIGHTBLACK_EX + (Fore.YELLOW if player == player_1 else Fore.RED) + \
                           player + Style.RESET_ALL

    # Check horizontal lines for win
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - (NUM_TO_CONNECT - 1)):
            if game_board[row][col] != empty_slot:
                check = [game_board[row][col + i] for i in range(NUM_TO_CONNECT)]
                if len(set(check)) == 1:
                    for i in range(NUM_TO_CONNECT):
                        game_board[row][col + i] = placeholder_win_line
                    return True

    # Check vertical lines for win
    for row in range(BOARD_HEIGHT - (NUM_TO_CONNECT - 1)):
        for col in range(BOARD_WIDTH):
            if game_board[row][col] != empty_slot:
                check = [game_board[row + i][col] for i in range(NUM_TO_CONNECT)]
                if len(set(check)) == 1:
                    for i in range(NUM_TO_CONNECT):
                        game_board[row + i][col] = placeholder_win_line
                    return True

    # part 1 - check top left to bottom right diagonals for win
    for row in range(BOARD_HEIGHT - (NUM_TO_CONNECT - 1)):
        for col in range(BOARD_WIDTH - (NUM_TO_CONNECT - 1)):
            if game_board[row][col] != empty_slot:
                check = [game_board[row + i][col + i] for i in range(NUM_TO_CONNECT)]
                if len(set(check)) == 1:
                    for i in range(NUM_TO_CONNECT):
                        game_board[row + i][col + i] = placeholder_win_line
                    return True

    # part 2 - check bottom left to top right diagonals
    for row in range((NUM_TO_CONNECT - 1), BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - (NUM_TO_CONNECT - 1)):
            if game_board[row][col] != empty_slot:
                check = [game_board[row - i][col + i] for i in range(NUM_TO_CONNECT)]
                if len(set(check)) == 1:
                    for i in range(NUM_TO_CONNECT):
                        game_board[row - i][col + i] = placeholder_win_line
                    return True
    return False


def is_valid_move(game_board: list, col: int):
    # check if user selected column still has at least 1 valid open slot (check if top slot is free)
    if game_board[0][col] == empty_slot:
        return True
    return False


def main():
    board = create_board(slot=empty_slot, width=BOARD_WIDTH, height=BOARD_HEIGHT)
    print_board(game_board=board)
    current_player = player_1

    while True:
        # User to select a column to play
        idx = int(input(f"\nPlayer" + Style.BRIGHT + Fore.RED + f" {current_player}" + Style.RESET_ALL + ": "))

        if is_valid_move(game_board=board, col=idx):
            # loop through column to find first available empty slot (in reversed order)
            for i in range(BOARD_HEIGHT - 1, -1, -1):
                if board[i][idx] == empty_slot:
                    board[i][idx] = current_player
                    break

            # Check if player turn results in win
            win = is_win(game_board=board, player=current_player)

            # print the current board to the console
            print_board(game_board=board, width=BOARD_WIDTH, height=BOARD_HEIGHT)

            if win:
                print(f"\nPlayer {current_player} has {NUM_TO_CONNECT} in a row!")
                break

            # change player
            current_player = player_2 if current_player == player_1 else player_1


if __name__ == "__main__":
    main()
