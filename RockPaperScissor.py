import random
user_choice=int(input("Enter your choice : Type 0 for Rock, 1 for Paper, 2 for Scissor:"))

if user_choice >=3 or user_choice<0:
    print("You Enter invalid number , you lose")
else:    
    computer_choice=random.randint(0,2)

    print("Computer Chose:")

    print(computer_choice)

    if computer_choice==user_choice:
        print('It is Draw')
    elif computer_choice==0 and user_choice==2:
        print("You Lose")
    elif user_choice==0 and computer_choice==2:
        print("You Win")
    elif computer_choice > user_choice:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win")



# User_input : 0 or 1 or 2  

#Computer_Output: 0 or 1 or 2
