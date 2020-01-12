import random

def main():
    print("hello world")
    smaller = int(input("A smaller number:"))
    greater = int(input("A greater number:"))
    myNumber = random.randint(smaller,greater)
    count = 0
    while True:
        count += 1
        myGuess = int(input("Your Guess:"))
        if myGuess > myNumber:
            print("Too big")
        elif myGuess < myNumber:
            print("Too small")
        else:
            print("Get the number in",count,"entries")
            break

if __name__ == "__main__":
    main()