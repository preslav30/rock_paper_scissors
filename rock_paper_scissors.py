import random

rock = f'''
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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Type 3 to end the game.\n"))
choice_list = [rock, paper, scissors]
computer_choice = random.choice(choice_list)
win = 0
lost = 0
draw = 0
while user_choice != 3:
    if user_choice < 0 or user_choice > 3:
        print("Wrong input!")
    elif user_choice == 0:
        print(rock)
        if computer_choice == choice_list[0]:
            print(f"Computer chose: {rock}")
            print(f"Draw.")
            draw += 1
        elif computer_choice == choice_list[1]:
            print(f"Computer chose: {paper}")
            print(f"You lose.")
            lost += 1
        elif computer_choice == choice_list[2]:
            print(f"Computer chose: {scissors}")
            print(f"You win!")
            win += 1
    elif user_choice == 1:
        print(paper)
        if computer_choice == choice_list[0]:
            print(f"Computer chose: {rock}")
            print(f"You win!")
            win += 1
        elif computer_choice == choice_list[1]:
            print(f"Computer chose: {paper}")
            print(f"Draw.")
            draw += 1
        elif computer_choice == choice_list[2]:
            print(f"Computer chose: {scissors}")
            print(f"You lose.")
            lost += 1
    elif user_choice == 2:
        print(scissors)
        if computer_choice == choice_list[0]:
            print(f"Computer chose: {rock}")
            print(f"You lose.")
            lost += 1
        elif computer_choice == choice_list[1]:
            print(f"Computer chose: {paper}")
            print(f"You win!")
            win += 1
        elif computer_choice == choice_list[2]:
            print(f"Computer chose: {scissors}")
            print(f"Draw.")
            draw += 1
    print(f"\nResult so far: win - {win}; lose - {lost}; draw - {draw}")
    user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Type 3 to end the game.\n"))
    computer_choice = random.choice(choice_list)
if user_choice == 3:
    print("\nThank you for playing!")
