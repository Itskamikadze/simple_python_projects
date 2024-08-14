import random

def main():

    #invoke the classes
    theBoard = Board()
    player = Player()

    while True:
        # assign the players and check whos goes first!
        print("Welcome in a Tic Tac Toe game!")
        player_X, player_O = player.choose_player()
        turn = player.whos_first()
        print(f'Player {turn} will start first!')
        #create new board
        newBoard = [' ']*9

        #get a message if you want to play!
        play = input("Do you want to play?[Y/N]").upper()
        if play == "Y":
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == "Player X":
                
                # Player X turn
                print(theBoard.display_board(newBoard))
                position = theBoard.player_choice(newBoard)
                theBoard.put_marker(newBoard, position, player_X)

                if theBoard.check_win(newBoard, player_X):
                    print(theBoard.display_board(newBoard))
                    print("Congratulations! Player X win this game!")
                    game_on = False
                    break
                else:
                    if theBoard.is_board_full(newBoard):
                        print(theBoard.display_board(newBoard))
                        print("Its a tie!")
                        break
                    else:
                        turn = "Player O"
            else:
                
                # Player O turn
                print(theBoard.display_board(newBoard))
                position = theBoard.player_choice(newBoard)
                theBoard.put_marker(newBoard, position, player_O)

                if theBoard.check_win(newBoard, player_O):
                    print(theBoard.display_board(newBoard))
                    print("Congratulations! Player O win this game!")
                    game_on = False
                    break
                else:
                    if theBoard.is_board_full(newBoard):
                        print(theBoard.display_board(newBoard))
                        print("Its a tie!")
                        break
                    else:
                        turn = "Player X"

        
        





class Board():

    def __init__(self):
        self.board = [' '] * 9
        self.test_board = ['#', '$', '#', '$', '#', '$', '#', '$', '#']

    def display_board(self, board):
        # create a fields  and board
        return f'''
        {board[6]}|{board[7]}|{board[8]}  7  8  9
        -----
        {board[3]}|{board[4]}|{board[5]}  4  5  6
        -----
        {board[0]}|{board[1]}|{board[2]}  1  2  3
        
        '''
    
    def space_check(self, board, position):
         # check if some fields are free
         return board[position-1] == " "
    
    def is_board_full(self, board):
        for space in range(1,10):
            if self.space_check(board, space):
                return False # if a single space is blank, return False
        return True #if no spaces are blank, return True
    
    def put_marker(self, board, position, marker):
        board[position-1] = marker

    def check_win(self, board, marker):
        return ((board[6] == board[7] == board[8] == marker) or #in the top
                (board[3] == board[4] == board[5] == marker) or #in the middle
                (board[0] == board[1] == board[2] == marker) or # in the bottom
                (board[6] == board[3] == board[0] == marker) or # in left to down
                (board[7] == board[4] == board[1] == marker) or # in middle to down
                (board[8] == board[5] == board[2] == marker) or # in right to down
                (board[6] == board[4] == board[2] == marker) or # diagonal
                (board[8] == board[4] == board[0] == marker))   # diagonal
    
    def player_choice(self, board):

        posiiton = 0
        # choose a position from 1 - 9 and it should has free field
        while posiiton not in [1,2,3,4,5,6,7,8,9] or not self.space_check(board, posiiton):
            posiiton = int(input("Please choose a field (1 - 9): "))
        return posiiton
    
    def replay(self):

        rep = input(" Do you want to play again?[Y/N] ")
        return rep
    
class Player:

    def __init__(self):
        self.player_1 = 'X'
        self.player_2 = 'O'

    def choose_player(self):
        
        choose = ""

        #choose a player X or O
        while not ( choose == "X" or choose == "O"):
            choose = input("Please choose a player:[X/O] ").upper()

        if choose == self.player_1:
            return ("X", "O") #if choose X, the next should be O
        elif choose == self.player_2:
            return ("O", "X") #if choose O, the next should be X
        
    def whos_first(self):
        
        if random.randint(0,1) == 0:
            return "Player X"
        else:
            return "Player O"



        

if __name__ == "__main__":
    main()