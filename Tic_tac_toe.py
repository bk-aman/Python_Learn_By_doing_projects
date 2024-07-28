'''
Tic-Tac toe programe, you play your move and computer plays accordingly
'''

board = [' ' for x in range(10)]
# print(board)

#function to insert letter at a particular position
def insertLetter(letter, pos):
    board[pos] = letter

#Check if position is free
def spaceIsFree(pos):
    return board[pos] == ' '

#print board
def printBoard(board):
    print('  |     |')
    print(' '+ board[1] + '| ' + board[2] + '   | ' + board[3])
    print('  |     |')
    print('-----------')
    print('  |     |')
    print(' '+ board[4] + '| ' + board[5] + '   | ' + board[6])
    print('  |     |')
    print('-----------')
    print('  |     |')
    print(' '+ board[7] + '| ' + board[8] + '   | ' + board[9])
    print('  |     |') 

#function to tell if winner
def isWinner(bo, le):
    return((bo[7] == le and bo[8] == le and bo[9] == le) or  # Horizontal match
           (bo[4] == le and bo[5] == le and bo[4] == le) or  
           (bo[1] == le and bo[2] == le and bo[3] == le) or  
           (bo[7] == le and bo[4] == le and bo[1] == le) or  # Vertical match
           (bo[8] == le and bo[5] == le and bo[2] == le) or
           (bo[9] == le and bo[6] == le and bo[3] == le) or  # diagonal match
           (bo[7] == le and bo[5] == le and bo[3] == le) or
           (bo[9] == le and bo[5] == le and bo[1] == le)
          )

# print(isWinner(board, ' '))

#return True if board is full or not
def isBoardFull(board):
    if board.count(' ') > 1:   #There is already one ' ' element so more than 1
        return False
    else:
        True

#asking user to play the move and we validate it and if all good we update the board
def playerMove(choice):
    run = True
    while run:   #keep running untill we get valid move
        move = input('Please enter position to place (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:  #check if entered position is valid
                if spaceIsFree(move):   #check if space is free at entered position
                    run = False
                    insertLetter(choice, move)
                else:
                    print('This position is already occupied!')
            else:
                print('Please type a number within range!')
        except:
            print('Please type a number')


#function will randomly decide which of possible option to take
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


#making computer watch out board and fill in the best position
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    #Check possible winning move or block opponent's winning move
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    #Try to take one of corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #try to take center
    if 5 in possibleMoves:
        move = 5
        return move
    
    #take any edges
    edgeOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)
    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)

    return move


#main function that will call all other function
def main():
    #Main game loop
    print('Welcome to Tic Tac Toe, to win make a complete a straight line (Diagonals included)')
    printBoard(board)
    
    choice = input('X or O : ')

    if choice == 'X':
        comp_choice = 'O'
    elif choice == 'O':
        comp_choice = 'X'
    

    while not(isBoardFull(board)):
        if not (isWinner(board, choice)):
            playerMove(choice)
            printBoard(board)
        else:
            print(choice, ' Congratulation wins this...')
            break

        if not(isWinner(board, comp_choice)):
            move = compMove()
            if move == 0:
                print('Game is tie, no more spaces left to move')
                break
            else:
                insertLetter(comp_choice, move)
                print('Computer placed an', comp_choice, ' in position', move, ':')
                printBoard(board)
        else:
            print(comp_choice, 'win, Try again!')
            break

    if isBoardFull(board):
        print('Game is a tie! No more space left to move')


while True:
    answer = input('Do you want to play? (Y/N) : ')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-------------------------------------------------')
        main()
    else:
        break


