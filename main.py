#Functions go here
def statement_generator(statement, decoration):

    sides = decoration * 3
  
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
  
    print(top_bottom)
    print(statement)
    print(top_bottom)
    
    return ""

#Greet the user and ask them if they would like to partake in the quiz
score = 0
statement_generator("Welcome to the Te Reo Maori test!", "*")
print()
print("This test has 15 multiple choice questions")
response = input("Would you like to proceed? ").lower()
if response == "yes" or response == "y":
    print("Great! Lets get started!")
elif response == "no" or response == "n":
    print("Goodbye")
else:  
  print("Please answer Yes or no")





print()

#QUESTIONS GO HERE!
question1 = input("What is the Te Reo word for Hello: A: Wharepaku B: Karekau C: Kia ora D: Takaro ").lower()
if question1 == "c" or question1 == "kia ora":
  score += 1 
  print("Correct!")
else:
  print("Incorrect, The answer is Kia Ora ")

question2 = input("What is the Te Reo word for food: A: Tukituki B: Kai C: Aporo D: Hanawiti ").lower()
if question2 == "b" or question2 == "kai":
  score += 1 
  print("Correct!")
else: 
  print("Incorrect, The Answer is Kai") 

