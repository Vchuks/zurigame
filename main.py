import random


print("Welcome to Rock, Paper and Scissors game")
is_running =True
while is_running:
    try:
        user_input = input('Enter "R" or "P" or "S" \n')
        user_input=user_input.upper()
        print(f"You entered {user_input}")

        my_list= ['R','P','S']
        comp = random.choice(my_list)
        print("The computer's choice is ")
        print(comp)

    except:
        print("invalid character")
        continue

    if user_input == comp:
        print("It is a tie")
    elif user_input == 'R' and comp == 'P':
        print ('Player(Rock): CPU(Paper) You loose,the computer won')
    elif comp == 'R' and user_input == 'P':
        print ('Player(Paper): CPU(Rock) Congrats, you won!')
    elif user_input == 'R' and comp == 'S':
        print ('Player(Rock): CPU(Scissors) Congrats, you won!')
    elif comp == 'R' and user_input == 'S':
        print ('Player(Scissors): CPU(Rock) You loose,the computer won')
    elif user_input == 'P' and comp == 'S':
        print ('Player(Paper): CPU(Scissors) You loose,the computer won')
    elif user_input == 'S' and comp == 'P':
        print ('Player(Scissors): CPU(Paper) Congrats, you won!')
    else:
        print('Enter the correct character')
        continue
    
    if user_input != comp:
        is_running= False