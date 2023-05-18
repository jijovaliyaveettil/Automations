import random

MAXLINES = 3
MAXBET = 100
MINBET = 5

ROWS = 3
COLS = 3

symbolcount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolvalues = {
    "A": 5,
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
            winnings += values[symbol] *bet
            winning_lines.append(line + 1)

    return winnings,winning_lines


def get_slot_machine_spin(rows,cols, symbols):
    all_symbols = []
    for symbol, symbolcount in symbols.items():
        for i in range(symbolcount):
            all_symbols.append(symbol)

    columns =[]
    for col in range(cols):
        column = []
        currentsymbol = all_symbols[:]
        for row in range(rows):
            value = random.choice(currentsymbol)
            currentsymbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What is the deposit amt? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")

    return amount


def getnumberoflines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAXLINES)+") $")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXLINES:
                break
            else:
                print("Lines must be between 1 -"+str(MAXLINES) )
        else:
            print("Enter a number")

    return lines


def getbet():
    while True:
        amount = input("What is the bet amt? $")
        if amount.isdigit():
            amount = int(amount)
            if MINBET <= amount <= MAXBET :
                break
            else:
                print(f"Bet amount must be between {MINBET} - {MAXBET}")
        else:
            print("Enter a number")

    return amount

def spin(balance):
    lines = getnumberoflines()
    while True:

        bet = getbet()
        totalbet = bet*lines

        if  totalbet > balance:
            print(f"You do not have enough balance to bet that amt. Your current balance is {balance}.")
        else:
            break

    print(f"You are betting {bet} on {lines}. Therefore your total bet is {totalbet} ")

    slots = get_slot_machine_spin(ROWS,COLS, symbolcount)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots,lines,bet, symbolvalues)
    print(f"You won${winnings}." )
    print(f"You won on lines: ", *winning_lines)

    return winnings - totalbet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")



main()