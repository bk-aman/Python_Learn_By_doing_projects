import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}



def get_number_of_lines():
    while True:
        lines = input('Enter number of lines to bet on (1 - ' +  str(MAX_LINES) + ')?')
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines : ')
        else:
            print('Please enter digits only ')
    

    return lines

def get_bet():
    while True:
        amount = input('Enter amount you want to bet : ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('Enter a valid amount: ')
        else:
            print('Please enter digits only ')
    

    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

       

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= '|')
            else:
                print(column[row], end = '')

    print()

def check_winning(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winnings_lines.append(line + 1)
    
    return winnings, winnings_lines


def deposite():
    while True:
        amount = input(' What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Enter amount greater than 0')
        else:
            print('Enter legit amount')
        
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You dont have enough to bet that amount, your current balance is Rs{balance}')
        else:
            break
    print(f'You are betting Rs{bet} on {lines} lines, Total bet is : Rs{total_bet}')

    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winning(slots,lines, bet, symbol_value)
    print(f'You won ${winning}')
    print(f'You won on lines: ', *winning_lines)
    return winning - total_bet




def main():
    balance = deposite()
    while True:
        print(f'Your current balance is Rs{balance}')
        answer = input('Press Enter to play or q to quit')
        if answer.lower() == 'q':
            break
        balance += spin(balance)

    print(f'You are left with: {balance}')

main()

