import time
#functions go here
score = 0
def quiz():
  print("What is the maori word for 'toilet' ")
  print("A: Whare")
  print("B: Karekau  ")
  print("C: Wharepaku")
  print("D: Taonga")
  question1 = input().lower
  if question1 == "c":
    print("Correct!")
    score + 1
  else:
    print("Incorrect")
      


print("Welcome to the test")
print("This test has 15 questions")
response = input(" Would you like to proceed? ").lower()

if response == "yes" or response == "y":
    print("Great! Lets get started!")
    quiz()
elif response == "no" or response == "n":
    print("Goodbye")
else: 
  print("Please answer Yes or no")

  



