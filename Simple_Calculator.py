def add(a,b):
    ans = a + b
    print(f"{a} + {b} = {ans}")

def subtract(a,b):
    ans = a - b
    print(f"{a} - {b} = {ans}")

def multiply(a,b):
    ans = a * b
    print(f"{a} x {b} = {ans}")

def divide(a,b):
    ans = a / b
    print(f"{a} / {b} = {ans}")

def main():
    print("Here are the functions of the Calculator:\n 1) Addition\n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) MOD \n 6) Exit")
    n = input("Enter your input: $")
    a = input("Enter the first number: $")
    b = input("Enter the second number: $")
    while(n):
        if n == 1 :
            add(a,b)
        if n == 2 :
            subtract(a,b)
        if n == 3 :
            multiply(a,b)
        if n == 4 :
            divide(a,b)
        if n == 6 :
            break

main()