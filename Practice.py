import random
#Get Difficulty 

def get_difficulty():
    #Handles the Difficulty selection and return (a,b).
    while True:
        try:
            choose = int(input("(1)Easy 1-5\n(2)Medium 1-10\n(3)Hard 1-50\nChoose:"))
            if choose == 1:
                return 1,5
            elif choose == 2:
                return 1,10
            elif choose == 3:
                return 1,50
            
        except ValueError:
            print("Please enter valid number.")

def play_game():
    # 1. Get the range based on the difficulty
    a,b = get_difficulty()

    # 2.Generate Fresh secret numbre for this round
    secret_number = random.randint(a,b)
    attempts = 0    
    
    #3. Guess the loop
    while True:
        try :
            user  = int(input(f"Input a number between {a} to {b}: "))
            attempts += 1
            if user > secret_number:
                print("Too high! Try again.\n")
            elif user < secret_number:
                print("Too low! Try again.\n")
            else:
                print("You Guessed It!!")
                print(f"Number of attempts: {attempts}")
                break
        except ValueError:
            print("Please Enter Valid number\n")


#Main Game
while True:
    play_game()

    try:
        wants_to_play = int(input("(1)Yes (0)No\nPlay Again?"))
        if wants_to_play != 1:
            print("Thanks for Playing.")
            break
    except ValueError:
        print("Invalid input. Exiting the game.")
        break