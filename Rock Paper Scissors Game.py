import random

# Rock
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of options (indexed from 0, 1, 2)
choices = [Rock, Paper, Scissors]

# Randomly generate the computer's choice as an integer (0, 1, or 2)
computerChoice = random.randint(0, 2)

# Get user input (integer choice)
choice = int(input("What do you choose? Rock - 0, Paper - 1, Scissors - 2: "))

# User's choice - displaying the corresponding ASCII art
if choice == 0:
    print(Rock)
elif choice == 1:
    print(Paper)
elif choice == 2:
    print(Scissors)
else:
    print("Invalid choice. Please select 0, 1, or 2.")
    exit()

# Computer's choice
print("Computer chose: ")
print(choices[computerChoice])

# Determine the winner
if choice == computerChoice:
    print("It's a tie!")
elif (choice == 0 and computerChoice == 2) or (choice == 1 and computerChoice == 0) or (choice == 2 and computerChoice == 1):
    print("You win!")
else:
    print("You lose!")
