"""Using ASCI art for console printing"""
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

output = [rock , paper , scissors]

"""Take Input from user"""
print("Hello, Welcome to the game !")
user_input = input("Type 0 for Rock , Type 1 for Paper and Type 2 for Scissors.")
if int(user_input) >2 or int(user_input) < 0:
  print("Please select valid input and try again !")
else:
  print(output[int(user_input)])

"""Generate Random Output from Rock Paper and Scissors"""
import random

random_number = random.randint(0 , len(output)-1)
print(output[random_number]) 

if int(user_input) >= 3 or int(user_input) < 0: 
  print("You typed an invalid number, you lose!") 
elif int(user_input)==0 and random_number == 2:
  print("You Lost !")
elif random_number > int(user_input):
  print("You Lost !")
elif int(user_input) > random_number:
  print("You Win !")
elif random_number == int(user_input):
  print("Its a Draw !")