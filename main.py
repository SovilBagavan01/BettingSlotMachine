'''

Once upon a time, in the mystical kingdom of Pylandia, a curious and daring programmer named sovil embarked on a quest to create his 
own version of an enchanting slot machine. Let's dive into the story and explain each line of code that sovil used to bring his magical creation 
to life'''
import random  # importing the random library
MAX_LINES = 3  # constants in python must be written using uppercase letters even though it's not compulsory
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 10,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet *50
            winning_lines.append(line + 1)  # +1 to convert 0-based index to line number
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], " | ", end="")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a digit")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a number")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_amount = bet * lines
        if total_amount > balance:
            print("Insufficient balance to bet. Please deposit some more amount.")
        else:
            break
    
    print(f"Your bet is ${bet} on {lines} lines hence total bet is ${total_amount}")
    
    slots = get_slot_machine_spin(ROWS, COLS)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    return winnings - total_amount

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")

        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
