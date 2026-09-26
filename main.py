board = ["1","2","3","4","5","6","7","8","9"]
player = "X"
No_winner = True

while No_winner:
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

    #someone wins if the player gets three in a row
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("X wins!")
        break
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("X wins!")
        break
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("X wins!")
        break

    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("X wins!")
        break
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("X wins!")
        break
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("X wins!")
        break

    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("X wins!")
        break
    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("X wins!")
        break
    
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("O wins!")
        break
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("O wins!")
        break
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("O wins!")
        break

    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("O wins!")
        break
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("O wins!")
        break
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("O wins!")
        break

    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("O wins!")
        break
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("O wins!")
        break