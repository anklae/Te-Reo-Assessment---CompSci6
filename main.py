#Functions go here

#This function adds a border to a selected statement to give it more style and "pazaz"
def statement_generator(statement, decoration):

    sides = decoration * 3
  
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
  
    print(top_bottom)
    print(statement)
    print(top_bottom)
    
    return ""
def respo():
  valid = False
  while not valid:
    response = input("Would you like to proceed ").lower()
    
    if response == "yes" or response  == "y":
      response == "yes"
      question_hab()
    elif response == "no" or response == "n":
      response = "no"
      return response
    
 
    else:
      print("Please answer Yes/No")

def question_hab():
  score = 0
  print("Q1: What is the Te Reo word for Hello?: A:wharepaku B:karekau C:kia ora D:takaro")
  question1 = input().lower()
  if question1 == "c" or question1 == "kia ora":
    score += 1 
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is Kia Ora ")
    print()

  
  print("Q2: What is the Te Reo word for Food?: A:tukituki B:kai C:Aporo D:hanawiti ")
  question2 = input().lower()
  if question2 == "b" or question2 == "kai":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Kai") 
    print()
  
  print("Q3: What is the Te Reo word for Sea Food? A:kai moana B: aporo C:tepu D:taraka")
  question3 = input().lower( )
  if question3 == "a" or question3 == "kai moana":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The answer is kai moana ") 
    print()
 
  print("Q4: What is the Te Reo word for Breakfast? A:watea B:punetēpu C:aroha D:parakuihi")
  question4 = input().lower()
  if question4 == "d" or question4 == "parakuihi":
    score += 1
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is parakuihi") 
    print()

  print("Q5: What is the Te Reo word for Lunch? A:pene B:mokowhiti C:tina D:kai")
  question5 = input().lower()
  if question5 == "c" or question5 == "tina":
    score += 1 
    print("Correct!")
    print()
  
  else: 
    print("Incorrect, The Answer is tina ") 
    print()

  print("Q6: What is the Te Reo word for Mom: A:mama B: karaihe C:petipeti D: hautoa ") 
  question6 = input().lower()
  if question6 == "a" or question6 == "mama":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Mama") 
    print()
  
  print("Q7: What is the Te Reo word for Dad: A:whanau B: tepu C:aporo D:papa")
  question7 = input().lower()
  if question7 == "d" or question7 == "papa":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Papa") 
    print()
  
  print("Q8: What is the Te Reo word for Family?: A:motokā B:whanau C: mokomoko D: KAMARAMA")
  question8 = input().lower()
  if question8 == "b" or question8 == "whanau":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Whanau ") 
    print()

  print("Q9: What is the Te Reo word for Cousin A:riu B: matimati C:whanaunga D:maunga ")
  question9 = input().lower()
  if question9 == "c" or question9 == "whanaunga":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is whanaunga") 
    print()

  print("Q10: What is the Te Reo word for house?: A:kainga B:whare C:hamipere D:tiihi tiihi")
  question10 = input().lower()
  if question10 == "b" or question10 == "whare":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Whare ") 
    print()
    
  print("Q11: What is the Te Reo word for Toilet: A: oro B:karekau C:kāore he aha D:wharepaku")
  question11 = input().lower()
  if question11 == "D" or question11 == "wharepaku":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Wharepaku  ") 
    print()

    print("Q12: What is the Te Reo word for : ")
  question12 = input().lower()
  if question12 == "" or question12 == "":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is ") 
    print()
  
  print("Q13: What is the Te Reo word for ")
  question13 = input().lower()
  if question13 == "" or question13 == "":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is ") 
    print()

  print("Q14: What is the Te Reo word for ")
  question14 = input().lower()
  if question14 == "" or question14 == "":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is ") 
    print()

  print("Q15: What is the Te Reo word for ")
  question15 = input().lower()
  if question15 == "" or question15 == "":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is ") 
    print()
  
  
    #Greet the user and ask them if they would like to partake in the quiz
statement_generator("Welcome to the Te Reo Maori test!", "*")
print()
print("This test has 15 multiple choice questions")
respo()




print()
#QUESTIONS GO HERE!

