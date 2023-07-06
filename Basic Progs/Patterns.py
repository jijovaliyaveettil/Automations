
def pattern1():

    for i in range(4):
        for j in range(4):
            print("*", end="")
        print("*")


def pattern2():

    for i in range(5):
        for j in range(i):
            print("*", end="")
        print("*")


def pattern3():
    
    for i in range(5):
        for j in range(i):
            print(j+1, end="")
        print("")

def pattern4():
    
    for i in range(5):
        for j in range(i):
            print(i,end="")
        print("")

def pattern5(n):
    
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end="")
        print("")


def pattern6(n):
    
    for i in range(n):
        for j in range(n,i,-1):
            print(n-j+1,end="")
        print("")

def pattern7(n):

    for i in range(n):
        for j in range(n-i-1):
            print(' ',end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(' ',end="")
        print("")

def pattern8(n):

    for i in range(n):
        for j in range(i):
            print(' ',end="")
        for j in range(2*n-(2*i+1)):
            print("*",end="")
        for j in range(i):
            print(' ',end="")
        print("")
        
def pattern9(n):

    for i in range(n):
        for j in range(n-i-1):
            print(' ',end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(' ',end="")
        print("")
        
    for i in range(n):
        for j in range(i):
            print(' ',end="")
        for j in range(2*n-(2*i+1)):
            print("*",end="")
        for j in range(i):
            print(' ',end="")
        print("")

def main():

    n = 4
    # n = int(input("What is n ?"))
    # pattern1()
    # pattern2()
    # pattern3()
    # pattern4()
    # pattern5(n)
    # pattern6(n)
    # pattern7(n)
    # pattern8(n)
    pattern9(n)

main()