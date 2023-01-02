import random
print("              🤜-🤚-✌️  Welcome To Rock-Paper-Scissor Game    🤜-🤚-✌️         ")
print("                            Have Fun and Enjoy the Game ")
while True:
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    images=[rock,paper,scissors,3,4,5,6,7,8,9]

    user=int(input("Enter your choice between '0' for ROCK, '1' for PAPER and '2' for SCISSOR "))
    print(f"you chooses {images[user]}" )
    comp_choice=random.randint(0,2)
    if comp_choice==user:
        print(f" Computer chooses{images[comp_choice]} its a tie" )
    elif comp_choice==0 and user==1:
       print(f"Computer chooses {images[comp_choice]}")
       print("Paper covers rock! You win!")
    elif comp_choice==1 and user==2:
       print(f"Computer chooses {images[comp_choice]}")
       print("Scissor cuts paper! You win!")
    elif comp_choice==2 and user==0:
       print(f"Computer chooses {images[comp_choice]}")
       print("Rock smashes scissor! You win!")
    elif comp_choice==2 and user==0:
       print(f"Computer chooses {images[comp_choice]}")
       print("Rock smashes scissor! You win!")
    elif comp_choice==1 and user==0:
       print(f"Computer chooses {images[comp_choice]}")
       print("Paper covers rock! You lose.")
    elif comp_choice==0 and user==2:
       print(f"Computer chooses {images[comp_choice]}")
       print("Rock smashes scissor! You lose.")
    elif comp_choice==2 and user==1:
       print(f"Computer chooses {images[comp_choice]}")
       print("Scissor cuts paper! You lose.")   
    else:
       print ("Invalid choice please read instructions")
    play_again=input("Play Again? (y/n): ")
    if play_again.lower() != ("y" or "Y"):
        print("Thank You for Playing")
        break

