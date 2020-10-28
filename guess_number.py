from random import randint

P1 = input("Player 1 please enter your name: ")
P2 = input("Player 2 please enter your name: ")

start = 1
end = 150

value = randint(start, end)
guess = None
turn = randint(1,2)
    
while guess != value:
    if turn == 1:
        print("It is ", P1, "'s turn")
        print("Please enter the number between", start, "and" , end)
        text = input("Your Guess: ")
        try:
            guess = int(text)
            if guess < value:
                start = guess
                turn = 2
                        
            elif guess > value:
                end = guess
                turn = 2                       
        except ValueError:
            print("Please input a valid value.")

    elif turn == 2:
        print("It is ", P2, "'s turn")
        print("Please enter the number between", start, "and" , end)
        text = input("Your Guess: ")
        try:
            guess = int(text)
            if guess < value:
                start = guess
                turn = 1
                        
            elif guess > value:
                end = guess
                turn = 1
        except ValueError:
                 print("Please input a valid value.")

if turn == 1:
    print("Congratulations!", P1, "wins")

elif turn == 2:
    print("Congratulations!", P2, "wins")
