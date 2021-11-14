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

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

computer_choice = random.randint(0,2)

print("Computer chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

if computer_choice == user_choice:
  print("Draw!")

if user_choice == 0:
  if computer_choice == 1:
    print("You lose.")
  elif computer_choice == 2:
    print("You win!")

if user_choice == 1:
  if computer_choice == 0:
    print("You win!")
  elif computer_choice == 2:
    print("You lose.")

if user_choice == 2:
  if computer_choice == 0:
    print("You lose.")
  if computer_choice == 1:
    print("You win!")