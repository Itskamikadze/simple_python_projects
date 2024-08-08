import random

class Board:

    test_board = ["#", "$", "#", "$", "#", "$", "#", "$", "#"]


    def display(self, board):
        print(board[6] + " | " + board[7] + " | " + board[8])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[0] + " | " + board[1] + " | " + board[2])

    def place_mark(self, board, position, mark):
        board[position-1] = mark
        

    def check_win(self, board, mark):
        return ((board[6] == mark and board[7] == mark and board[8] == mark) or
                (board[3] == mark and board[4] == mark and board[5] == mark) or
                (board[0] == mark and board[1] == mark and board[2] == mark) or
                (board[6] == mark and board[3] == mark and board[0] == mark) or
                (board[7] == mark and board[4] == mark and board[1] == mark) or
                (board[8] == mark and board[5] == mark and board[2] == mark) or
                (board[6] == mark and board[4] == mark and board[2] == mark) or
                (board[8] == mark and board[4] == mark and board[0] == mark))
    
    
    def space_check(self, board, position):
       return board[position] == " "
    
    
    def full_board_check(self, board):
        for place in range(1,10):
            if self.space_check(board, place):
                return False
        return True
    
    def replay(self):
        return input("Do you want to play again?[Y/N]: ").upper()


class Player():

    def __init__(self) -> None:
        self.current_player_X = ("X", "O")
        self.current_player_O = ("O", "X")

    def choose_player(self):
        choose = ""
        while choose != 'X' or choose != "O":

            choose = input("Please choose a player you want to play[X/O]: ").upper()
            if choose == 'X':
                return self.current_player_X
            elif choose == "O":
                return self.current_player_O
            else:
                print("Wrong value!")

    def whos_first(self):
        return random.choice("XO")
    
    def put_place(self):
        pass

    
        
            
        

    
if __name__ == "__main__":

    while True:
        theBoard = [' ']*9
    #invoke the both classes4
        board = Board()
        player = Player()
    
    
        print("Welcome in a Tic Tac Toe game!")
        #invoke the board
        print(board.display(theBoard))
        print(board.place_mark(board.test_board, 4, mark="Y"))
        print(board.display(board.test_board))
        print(board.check_win(board.test_board, "#"))
        #print(player.choose_player())
    