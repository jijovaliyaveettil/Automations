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

def getslotmachinespin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbolcount in symbol.items():
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

        columns.append(value)

    return columns

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


def main():
    balance = deposit()
    lines = getnumberoflines()
    while True:

        bet = getbet()
        totalbet = bet*lines

        if  totalbet > balance:
            print(f"You do not have enough balance to bet that amt. Your current balance is {balance}.")
        else:
            break




    print(f"You are betting {bet} on {lines}. Therefore your total bet is {totalbet} ")





main()