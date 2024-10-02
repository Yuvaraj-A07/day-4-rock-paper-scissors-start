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
user=int(input("What do you choose? Type 0 for Rock,1 for Paper,2 for Scissor\n"))
computer=random.randint(0,2)
if(user==0):
  print(rock)
elif(user==1):
  print(paper)
elif(user==2):
  print(scissors)
else:
  print("you entered wrong choice,play again")
  exit()
print("Computer's Chose\n")
if(computer==0):
  print(rock)
elif(computer==1):
  print(paper)
else:
  print(scissors)
#Descison for who win's the game
if(user==computer):
  print("Match Draw")
elif((user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1) ):
  print("you Win")
else:
  print("you Lose")
