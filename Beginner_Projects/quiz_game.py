print("Welcome to Computer Quiz!!")

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print('Okay lets play!')
score = 0

answer = input('What Does CPU stands for ?')
if answer.lower() == 'central processing unit':
    score += 1
    print('Correct!')

else:
    print(' Wrong answer :(')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    score += 1
    print('Correct!')
else:
    print('Incorrect answer')

answer = input('What does RAM stand for?')
if answer.lower() == 'random access memory':
    score += 1
    print('Correct!')
else:
    print('Incorrect answer')

answer = input('What does PSU stand for? ')
if answer.lower() == 'power supply':
    score += 1
    print('Correct!')
else:
    print('Incorrect answer')


print('You got ' + str(score) + 'question correct')
print('Thats ' +  str((score/4) * 100 ) + '%')
