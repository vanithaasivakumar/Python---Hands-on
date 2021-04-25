'''2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board'''
def display_board(board):
    print('_____________')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def user_choice():
    choice='wrong'
    while choice=='wrong':
        user_choice=input("Hello Player 1, You want to choose 'X' or 'O'?\n")
        if user_choice in ('X','x'):
            choice='right'
            return ('X','O')
        elif user_choice in ('O','o'):
            choice = 'right'
            return('O','X')
        else:
            print("Invalid Character Choice!")

def position_input(board):
    position_no=int(input("Please enter the position on the board (1-9)\n"))
    position='wrong'
    while position=='wrong':
        if position_no in range(1,10) and board[position_no-1]==' ':
            position='right'
            return position_no-1
        else:
            print("Wrong Position")

#def insert_board(board,user_choice,position):
#    board.insert(position-1,user_choice)

def validate_board(board):
    if (board[0] == board[1] == board[2] and board[0]!=' ') or (board[0] == board[3] == board[6] and board[0]!=' ') or (board[0] == board[4] == board[8] and board[0]!=' ') or (board[3] == board[4] == board[5] and board[3]!=' ') or (board[1] == board[4] == board[7] and board[1]!=' ') or (board[2] == board[5] == board[8] and board[2]!=' ') or (board[6] == board[7] == board[8] and board[6]!=' ') or (board[2] == board[4] == board[6] and board[2]!=' '):
            return True
    else:
        return False

def is_game_on():
    continue_game='wrong'
    while continue_game=='wrong':
        game_on=input("Would you like to continue a new game? (Y/N)\n")
        if game_on.lower()=='y':
            continue_game='right'
            return True
        elif game_on.lower()=='n':
            continue_game = 'right'
            return False
        else:
            print(" Wrong Character!")

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_on=True
while game_on==True:
    display_board(board)
    (char_choice1,char_choice2)=user_choice()
    players = {'player1': char_choice1, 'player2': char_choice2}
    print("Player 1: {} \nPlayer 2: {}".format(players.get('player1'),players.get('player2')))
    valid_board=False
    while valid_board==False:
        for player in players.keys():
            position=position_input(board)
            #insert_board(board,players.get(player),position)
            board[position]=players.get(player)
            display_board(board)
            if validate_board(board)==True:
                print('{} is won'.format(player))
                valid_board=True
                break
            else:
                continue
    if is_game_on() == True:
        game_on=True
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        continue
    else:
        break
