import random

def get_difficulty():
    
    try: 
        difficulty_choice = int(input("(1) 1-10\n(2) 1-15\n(3) 1-20\nChoose: "))
        if difficulty_choice == 1:
            return 1,10

        elif difficulty_choice == 2:
            return 1,15

        elif difficulty_choice == 3:
            return 1,20
        else:
            return None, None
        
    except ValueError:
        return None, None
        

def mathematical_sign():

    a, b = get_difficulty() 
    if a is None or b is None:
        return "Invalid difficulty"
        
   
    randomnumber1 = random.randint(a, b)
    randomnumber2 = random.randint(a, b)

    try:    
        math_sign = int(input("(1) + Addition\n(2) - Subtraction\n(3) x Multiplication\n(4) ÷ Division\nChoose: "))
        if math_sign == 1: 
            print (f"{randomnumber1} + {randomnumber2}: ?")
            return randomnumber1 + randomnumber2
        elif math_sign == 2:
            print(f"{randomnumber1} - {randomnumber2}: ?")
            return randomnumber1 - randomnumber2
        elif math_sign == 3:
            print(f"{randomnumber1} x {randomnumber2}: ?")
            return randomnumber1 * randomnumber2
        elif math_sign == 4:
            print(f"{randomnumber1} ÷ {randomnumber2}: ?")
            return randomnumber1 /randomnumber2
        else:
            return None, None
    except ValueError:
        return "Error. Please Input Again"


wrong = 0
correct = 0
while True:
	
	play1 = int(input("(1)Yes or (2)No\nChoose: "))
	
	if play1 == 1:
		answer = mathematical_sign()
		user = int(input("Input Your answer: "))
		if user == answer:
			correct += 1
			print("--------------------")
			print("Good, Your Correct")
			print("--------------------")
		else:
			wrong += 1
			print("--------------------")
			print("Try Again")
			print(f"The Correct Answer is {answer}")
			print("--------------------")
		print(f"Score - Correct: {correct}, Wrong: {wrong}")
		
		
	else:
		print("Exiting")
		break
