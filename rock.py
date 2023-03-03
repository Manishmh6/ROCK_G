import random 
user_wins = 0
comp_wins= 0

options = ["rock","paper", "scissor"]
user_name=input('YOU GOOD NAME : = ')
print(f"WLCOME {user_name} IN ROCK PAPER SCISSOR GAME ")
while True:
    user_ans = input("choose rock/ paper/ scissor or q to quit ; = ")
    if user_ans =="q":
        break
    if user_ans not in options:
        print("please choose a valid options")
        continue
    computer_choose = random.choice(options)
    print(f"computer choose {computer_choose}.")
    if user_ans == computer_choose:
        print("Tie")
    elif user_ans == "rock" and computer_choose == "scissor":
        print("You won")
        user_wins+=1
    elif user_ans == "paper" and computer_choose == "rock":
        print("you won!")
        user_wins+=1
    elif user_ans == "sicssor" and computer_choose == "paper":
        print("you won!")
        user_wins+=1 
    else:
        print("You lost")
        comp_wins+=1
print(f"You wine {user_wins} time.")
print(f"comp wine {comp_wins} time.")
# if user_name>comp_wins:
#     print("congrats.... you are winener!!!")
print("see you next time good bye")