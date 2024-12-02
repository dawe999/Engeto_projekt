# druhý projekt do engeto Online Python Akademie

# author: David Čadek
# email: david.cadek@cezdistribuce.cz
# discord: coudy999

# Hra piškvorky

def greet_user():
    print("Vítejte ve hře Tic-tac-toe!")
    print("Cílem hry je umístit 3 hrací kameny (X nebo O) horizontálně, vertikálně nebo diagonálně.")
    print(100 * "=")

def print_board(board):
    print("----+---+----")
    for idx, row in enumerate(board):
        print("| " + " | ".join(row) + " |")
        print("----+---+----")

def check_winner(board, player):
    # Kontrola řádků, sloupců a diagonál
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([spot != " " for row in board for spot in row])

def get_move(player):
    while True:
        try:
            move = int(input(f"Hráč {player}, zadejte číslo pozice (1-9): ")) - 1
            print(40 * "=")
            if move < 0 or move >= 9:
                print("Neplatná pozice. Zkuste to znovu.")
            else:
                return move
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")

def main():
    greet_user()
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        move = get_move(players[current_player])
        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("Pole je obsazené. Zkuste to znovu.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(50 * "=")
            print(f"Hráč {players[current_player]} vyhrál!")
            break

        if is_full(board):
            print_board(board)
            print("Remíza!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
