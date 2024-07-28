import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock OR paper OR scissors OR Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

#picking stuff from computer side
    #rock : 0, paper: 0, scissors: 0 
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print('Computer Picked ', computer_pick + '.')

    #main logic
    if user_input == 'rock' and computer_pick == 'scissors':
        print('You WON!!!')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('You WON!')
        user_wins += 1
    
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You WON!!')
        user_wins += 1
    
    elif user_input == computer_pick:
        print("You cut each other no points")
        continue

    else:
        print('You loose :(')
        computer_wins += 1
print('You won', user_wins, 'times')
print('Computer won', computer_wins,'times')
print('See you again!')


