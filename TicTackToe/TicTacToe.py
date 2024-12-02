''' 
Oliver Davis
10/31/2024
Description:
   A simple code to play tic-tac-toe with either 1 or 2 players
Bugs:
    I dont currently know of any bugs
Constaints:
    - the program ends after each runthrough and no score is kept
Instructions:
    First, insert the number of players (must be either 1 or 2), next, to insert a tile, type either 1,2, or 3
    for the vertical spot you want to play. Then, type space and then either a, b, or c for the horizontal spot
    you want to play. If it is singleplayer, the computer will play a random move then return the board for you
    to play again. If not, the next player inputs a move
'''

import random

"""
Create the main tic_tac_toe class
"""
class tic_tac_toe:
    def __init__(self):
        self.board = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]
        #self.player_count = player_count
    def show_board(self):
        """
        prints out the board in the proper format

        Args:
            None

        Returns:
            none
        """
        print(f'''Current Board:
    A | B | C 
===============
1 ]  {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
  ] -----------
2 ]  {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
  ] -----------
3 ]  {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}''')
    
    def end_check(self):
        """
        Checks if the board has a victory or a tie.

        Args:
            None

        Returns:
            Can be one of three returns:
            str: "x_victory"
            str: "o_victory"
            str: "draw"
        Note:
            this is done in the worst way possible but because its only 3x3 board in tic_tac_toe I dont think its
            worth doing in a better way
        """
        empty_count = 0
        for i in self.board:
            for j in i:
                if j == ' ': empty_count+=1 
        if empty_count == 0: return 'draw'
        if (self.board[0][0] == self.board[1][0] == self.board[2][0]):
            if self.board[0][0] == 'x':
                return 'x_victory'
            elif self.board[0][0] == 'o':
                return 'o_victory'
        elif (self.board[0][1] == self.board[1][1] == self.board[2][1]):
            if self.board[0][1] == 'x':
                return 'x_victory'
            elif self.board[0][1] == 'o':
                return 'o_victory'
        elif (self.board[0][2] == self.board[1][2] == self.board[2][2]):
            if self.board[0][2] == 'x':
                return 'x_victory'
            elif self.board[0][2] == 'o':
                return 'o_victory'
        elif (self.board[0][0] == self.board[0][1] == self.board[0][2]):
            if self.board[0][0] == 'x':
                return 'x_victory'
            elif self.board[0][0] == 'o':
                return 'o_victory'
        elif (self.board[1][0] == self.board[1][1] == self.board[1][2]):
            if self.board[1][0] == 'x':
                return 'x_victory'
            elif self.board[1][0] == 'o':
                return 'o_victory'
        elif (self.board[2][0] == self.board[2][1] == self.board[2][2]):
            if self.board[2][0] == 'x':
                return 'x_victory'
            elif self.board[2][0] == 'o':
                return 'o_victory'
        elif (self.board[0][0] == self.board[1][1] == self.board[2][2]):
            if self.board[1][1] == 'x':
                return 'x_victory'
            elif self.board[1][1] == 'o':
                return 'o_victory'
        elif (self.board[2][0] == self.board[1][1] == self.board[0][2]):
            if self.board[1][1] == 'x':
                return 'x_victory'
            elif self.board[1][1] == 'o':
                return 'o_victory'

    def begin_multiplayer(self):
        turn_number = 0
        # dictionary to turn 0 to o and 1 to x
        number_to_player = {0:'x',1:'o'}
        second_coordinate = {'a':1,'b':2,'c':3}                                                             # Dictionary to turn letter coordinate into a number
        while True:
            turn = number_to_player[turn_number%2]                                                          # if the turn number is an even number (divisible by two) it is x's turn. If not, its o's turn
            print(f"{turn.upper()}'s Turn!")                                                                # print whose turn it is but with the letter in upercase because it looks better
            while True:
                players_move = input('Where would you like to go?\n   ').split(' ')
                if (players_move[0] == '1' or players_move[0] == '2' or players_move[0] == '3') and (players_move[1] == 'a' or players_move[1] == 'b' or players_move[1] == 'c'): # checks if input coordinates are valid. its ugly but it works
                    if self.board[int(players_move[0])-1][second_coordinate[players_move[1]]-1] == ' ':     # Checks if chosen point on board is empty
                        self.board[int(players_move[0])-1][second_coordinate[players_move[1]]-1] = turn     # set point in its chosen position to the currently active player's icon
                        break
                    else:
                        print('Input position is already occupied')
                else:
                    print('Invalid Coordinate Input.')
            # check if there is a victory for x and break game loop if there is
            if self.end_check() == 'x_victory':
                print('X has won!')
                break
            # check if there is a victory for y and break game loop if there is
            elif self.end_check() == 'o_victory':
                print('O has won!')
                break
            # check if there is a draw and break game loop if there is
            elif self.end_check() == 'draw':
                print('Match is a draw')
                break
            turn_number+=1
            new_game.show_board()

    def singleplayer_move(self):
        while True: 
            computer_choice = (random.randint(0,2),random.randint(0,2))                                     # pick random spot on board
            if self.board[computer_choice[0]][computer_choice[1]] == ' ':                                   # checks if the random spot is empty
                self.board[computer_choice[0]][computer_choice[1]] = 'x'                                    # sets the chosen spot to 'o' (the computers symbol)
                break

    def begin_singleplayer(self):
        turn_number = 0                                                                                     # starts at 0 because in singleplayer goes second and is always x
        second_coordinate = {'a':1,'b':2,'c':3}                                                             # Dictionary to turn letter coordinate into a number
        while True:
            self.singleplayer_move()                                                             # have computer make its move
            # make player move
            while True:
                players_move = input('Where would you like to go?\n   ').split(' ')
                if (players_move[0] == '1' or players_move[0] == '2' or players_move[0] == '3') and (players_move[1] == 'a' or players_move[1] == 'b' or players_move[1] == 'c'): # checks if input coordinates are valid. its ugly but it works
                    if self.board[int(players_move[0])-1][second_coordinate[players_move[1]]-1] == ' ':     # Checks if chosen point on board is empty
                        self.board[int(players_move[0])-1][second_coordinate[players_move[1]]-1] = 'o'      # sets the players chosen position on the board to 'x' (that player's icon)
                        break                                                                               # break so it stops asking
                    else:
                        print('Input position is already occupied')

            # check if there is a victory for x and break game loop if there is
            if self.end_check() == 'x_victory':
                print('X has won!')
                break
            # check if there is a victory for y and break game loop if there is
            elif self.end_check() == 'o_victory':
                print('O has won!')
                break
            # check if there is a draw and break game loop if there is
            elif self.end_check() == 'draw':
                print('Match is a draw')
                break
            turn_number +=1                                                                                 # increment the counter for number of turns by one
            self.show_board()

if __name__ == "__main__":
    # continue to prompt user for the number of people playing until they return a valid response
    while True:
        player_count = input('Would you like to play with one or two players\n   ')
        if player_count != '1' and player_count != '2':
            print('Invalid Response')
        else:
            break
    new_game = tic_tac_toe()                                                                            # make a new tic_tac_toe game
    
    # start the game with the right number of player (start multiplay if 2 players, singleplayers if not)
    if player_count == '2':
        new_game.begin_multiplayer()
    else:
        new_game.begin_singleplayer()
