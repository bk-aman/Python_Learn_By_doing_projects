with open('story.txt', 'r') as f:
    story = f.read()

# print(story)
words = set()
start_of_word = -1

target_start  = '<'
target_stop = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_stop and start_of_word != -1:
        word = story[start_of_word : i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answers[word] = input('Enter a word for' + word + ':')
    story = story.replace(word, answers[word])
    
    
    

print(story)



