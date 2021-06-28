"""
Author:         Zeyad E
Description:    simulates a 2 player game of Tic-Tac-Toe
Last Modified:  6/7/2021
"""
boardDict = {1: ' ', 2: ' ',3: ' ',     #representation of each position on the board
             4: ' ', 5: ' ',6: ' ',     #dictionary keys are integers 1-9
             7: ' ', 8: ' ',9: ' '}     #simplifies comparisons for winning conditions

def printBoard(board):                  #prints the positions and the board
                                        #each key pulls the current value from boardDict
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

print('''
      _____________________________________________
            Hello and welcome to Tic-Tac-Toe!
        The rules are simple. The grid is divided
              into 9 squares to select from
                     1 | 2 | 3
                    ---+---+---
                     4 | 5 | 6
                    ---+---+---
                     7 | 8 | 9
      _____________________________________________
        ''')

turn = 'X'                      #turn will start off as X then alternate X/O in the loop
switch = True                   #used to switch turns
playerNum = '1'

for i in range(9):              #9 possible turns
    print('Where would you like to play player ' + playerNum + '?')
    userIn = int(input())       #convert input to an integer so it can be used as a key in boardDict
    boardDict[userIn] = turn    #update the value on the board
    #all possible victory combinations.
    if  boardDict[1] == boardDict[2] == boardDict[3] == 'X' or\
        boardDict[4] == boardDict[5] == boardDict[6] == 'X' or\
        boardDict[7] == boardDict[8] == boardDict[9] == 'X' or\
        boardDict[1] == boardDict[4] == boardDict[7] == 'X' or\
        boardDict[2] == boardDict[5] == boardDict[8] == 'X' or\
        boardDict[3] == boardDict[6] == boardDict[9] == 'X' or\
        boardDict[1] == boardDict[5] == boardDict[9] == 'X' or\
        boardDict[3] == boardDict[5] == boardDict[7] == 'X' or\
        boardDict[1] == boardDict[2] == boardDict[3] == 'O' or\
        boardDict[4] == boardDict[5] == boardDict[6] == 'O' or\
        boardDict[7] == boardDict[8] == boardDict[9] == 'O' or\
        boardDict[1] == boardDict[4] == boardDict[7] == 'O' or\
        boardDict[2] == boardDict[5] == boardDict[8] == 'O' or\
        boardDict[3] == boardDict[6] == boardDict[9] == 'O' or\
        boardDict[1] == boardDict[5] == boardDict[9] == 'O' or\
        boardDict[3] == boardDict[5] == boardDict[7] == 'O' :
        printBoard(boardDict) #if fulfilled, print board/winning screen and exit the loop
        print('_____________________________________________')
        print('Congratz Player ' + playerNum + ', YOU WIN!')
        print('_____________________________________________')
        break

    if switch == True:  #initially true, so we will swap to player 2
        turn = 'O'
        switch = False
        playerNum = '2'
    else:               #after player 2 plays, swap back to player 1
        turn = 'X'
        switch = True
        playerNum = '1'


    printBoard(boardDict)

#Todo
'''
make victory comparisons neater
prevent issue with players overwriting positions on board
prevent invalid inputs and ask the user to try again
'''