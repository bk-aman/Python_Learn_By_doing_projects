import random 

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)

    return roll

while True:
    players = input('Enter Number of Players(2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must Enter between 2 - 4: ')
    else:
        print('Invalid Input... \n Please enter a number')

max_score = 10
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print('Player #', player_idx + 1, 'turn has started...')
        print('Your Current Score is : ', player_score[player_idx], '\n')
        current_score = 0

        while True:
            should_roll = input('Do you want to roll? (y)')

            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print('BOOM! Now you are at 0')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a :', value)
            
            print(player_idx, "Current score is:", current_score)

        player_score[player_idx] += current_score
        print('Your Total score is : ',player_score[player_idx])
    
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print('Winner is :',winning_idx,'with the score of', max_score)



