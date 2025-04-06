def display_board(board):
 print("\n")
 print(f"{board[0]} |{board[1]} | {board[2]}")
 print("--------")
 print(f"{board[3]} |{board[4]} | {board[5]}")
 print("--------")
 print(f"{board[6]} |{board[7]} | {board[8]}")
 print("\n")

def player_input(player,board):
 while True:
  position = int(input(f"player {player}, enter your move(1-9):"))-1
  if board[position] == " ":
    board[position] = player
    break
 else:
    print("Invalid move.try again.")

def check_win(board):
  win_combination = [
      [0,1,2],[3,4,5],[6,7,8],
      [0,3,6],[1,4,7],[2,5,8],
      [0,4,8],[2,4,6]
  ]
  for combo in win_combination:
    if board[combo[0]] == board[combo[1]] == board[combo[2]] !=" ":
      return True
  return False

def check_tie(board):
    return" " not in board

def tic_tac_toc():
  board = [" "]*9
  players = ["x","0"]
  trun=0
  print("welcome to Tic Tac Toe! By Muqadas/uzma")
  display_board(board)
  while True:
    current_player = players[trun%2]
    player_input(current_player, board)
    display_board(board)
    if check_win(board):
      print(f"{current_player} wins!")
      break


tic_tac_toc()
