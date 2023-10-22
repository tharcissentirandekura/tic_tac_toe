import sys


print("Welcome to Tharcisse's Tictactoe game!\n")

print("----------------WHAT TO KNOW ABOUT THIS GAME!-------------------")
print("You will need to create an account to play if you are a new user to Tharciise's Titactoe.\n If you are not new, just log in only")

def const_board(board): # a function to initialize the game board pattern 
    print("This is the state of the game a this time!")
    print("\t...................")
    for i in range(len(board)):

        print("\t",board[i],"|",end ="")
        if (i+1) % 3 == 0:
            
            print("\n\t...................")
            
    return board

cur_board = [""]*9 # initialize the game board values to empty space in the columns and rows
# print(cur_board)
c_board = const_board(cur_board) # display the game board of initial values using the game board pattern

#initialize the played place list and the current state of the board.
played_place = []
cu_board = []

def reshape_board(board): # Turn the board on 2D form from  1 D board shape
    new_board = []# initialize the new board variables of 2D
    for i in range(0,len(board),3):
        
        row = board[i:i+3]
        new_board.append(row)
    return new_board

#check diagonals for winner if it has the same values by using set builtin function
#from left to right
def diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    
    #print([board[i][2-i] for i in range(len(board))])
    # check diagonal from right to left side
    if len(set([board[i][2-i] for i in range(len(board))])) == 1:
        return board[2][0]
    
    return None
        
#check rows for winner
def rows(board):
    for row in board:  
        if len(set(row)) ==1:
            return row[0]
    return None
#check columns for winner here
def columns(board): # we use nested loop because it is a 2D array to access the columns
    for col in range(len(board)):
        #if len(set([board[row][col] for row in range(len(board))])) == 1:

        i = [board[row][col] for row in range(len(board))]
        if len(set(i)) == 1:
            return i[0]
    return None

#check the winner of the game or if it is the draw!
def check_win(board):
        
    x = reshape_board(c_board) # call the reshape_board function to turn the board with values into a 2D
    if rows(x): # check if elements in each rows are same
        print(rows(x),"wins")

    if diagonals(x): # check if elements in each diagonals are the same
        print(diagonals(x),"wins")

    if columns(x): # check if elements in each columns are the same
        print(columns(x),"wins")
        
    if "" not in board[0] and "" not in board[1] and "" not in board[2]: # check if all spaces in game board are full
        if not rows(x) and not columns(x) and not diagonals(x): #check if there is not any row or colum or diagonal with same values to decide the tie/draw
            print("Tie!")  

# The function to get user input

def first_player(player1):

    if player1 not in played_place:

        played_place.append(player1)
        c_board[player1-1] = "X"
        
        const_board(c_board) # display the constant board at this time after the player1 make a move
        cur_board = reshape_board(c_board)
        
        cu_board = cur_board # update the 2D initialized array to be with values player1 entered

        check_win(cu_board) # check if there is any winner at this time, if not continue the game
        print("\n")
        if rows(cu_board) or columns(cu_board) or diagonals(cu_board): # if there is any winner, end the game
            print("The Game Over!")

    else:
        print("Wrong position because it is taken!,try again")

    return c_board

def second_player(player2):

    if player2 not in played_place and player2 > 0 and player2 <=9:
        played_place.append(player2)
        c_board[player2-1] = "O"
        
        const_board(c_board)
        
        cur_board = reshape_board(c_board)
        cu_board = cur_board # update the 2D initialized array to be with values player2 entered
        check_win(cu_board)
        print("\n")
        
        if rows(cu_board) or columns(cu_board) or diagonals(cu_board):
            print("The Game Over!")
    else:
        print("Wrong position because it is taken, try again")

    return c_board

def reset(continue_play):

    c_board.clear()
    played_place.clear()

    if continue_play.lower() == "y":

        played_place.clear()
        c_board.clear()

        main()

    elif continue_play.lower() == "n":

        print("Game over see you next time")
    
def main():

    while "" in c_board:

        player_one = int(input("Choose the x's position(1-9)"))

        first_player(player_one)


        player_two = int(input("Choose the o's position(1-9)"))

        second_player(player_two)

    else:
        print("Game is now over")

if __name__ == "__main__":
     main()
