board = ["1","2","3","4","5","6","7","8","9"]
player = "X"
GAME = True

while GAME:
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
    print("Player:", player)

    move = input("Choose 1-9: ")
    move = int(move) - 1
    if board[move].isdigit():
        board[move] = player
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Square already taken")