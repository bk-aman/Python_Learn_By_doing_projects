import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    
    character = letters
    if numbers:
        character += digits
    if special_characters:
        character += special

    pwd = ''
    meets_Creteria = False
    has_number = False
    has_special = False

    while not meets_Creteria or len(pwd) <= min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_Creteria = True
        if numbers:
            meets_Creteria = has_number
        if special_characters:
            meets_Creteria = meets_Creteria and has_special
        
    return pwd

min_length = int(input('Enter the min length : '))
has_number = input('Do you want to have numbers(y/n)? ').lower() == 'y'
has_special = input('Do you want to have special character (y/n)? ').lower() == 'y'
pwd = generate_password(min_length, has_number, has_special)

print('The Generated password is : ',pwd)


