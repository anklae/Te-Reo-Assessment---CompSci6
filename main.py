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
statement_generator("Welcome to the Te Reo Maori test!", "%")
print()
print("This test has 15 multiple choice questions")
#This function asks the user if they would like to proceed
score = 0
def respo():
  response = input("Would you like to proceed ").lower()
  print()
  if response == "yes" or response  == "y":
    response == "yes"
    question_hab()
  elif response == "no" or response == "n":
    response = "no"
    print("Have a good day")
  else:
    print("Please answer Yes/No")
    print()
    respo()




def bonus_questions():
  
  print("These bonus questions will give you 2x more points then the usual questions, Make sure to try your best")
  print()
  print("Bonus Question 1:  What is the te reo word for bread: A:taro B:kongakonga taro c:takakau D:")
  bonus_question = input().lower()
  if bonus_question == "a" or bonus_question == "taro":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is ")
    print()

  print("Bonus Question 2:")
  bonus_question2 = input().lower()
  if bonus_question2 == "c" or bonus_question2 == "":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is ")
    print()
  
  print("Bonus Question 3:")
  bonus_question3 = input().lower()
  if bonus_question3 == "" or bonus_question3 == "":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is ")
    print()

  print("Bonus Question 4:")
  bonus_question4 = input().lower()
  if bonus_question4 == "" or bonus_question4 == "":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is ")
    print()

    print("Bonus Question 5:")
  bonus_question5 = input().lower()
  if bonus_question5 == "" or bonus_question5 == "":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is ")
    print()
  
  print("Bonus Question 6:")
  bonus_question6 = input().lower()
  if bonus_question6 == "" or bonus_question6 == "":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is ")
    print()

  print("Bonus Question 7:")
  bonus_question7 = input().lower()
  if bonus_question7 == "" or bonus_question7 == "":
    score += 2
    print("Correct!")
    print()
    end()
  else:
    print("Incorrect, The answer is ")
    print()
    end()
    



#This Function starts the quiz and shows the questions when called apon

def end():
  if score <= 5:
    print("you did not do very well, you could do way better")
  if score <= 10: 
    print("You did alright, well done")
  if score <= 15:
    print("Good job , you answered more than half of the questions  ")
  if score <= 20:
    print("Great job,")

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
  if question11 == "d" or question11 == "wharepaku":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Wharepaku  ") 
    print()

  print("Q12: What is the Te Reo word for Mountain: A:awhe B:maunga C:puke D:pepi ")
  question12 = input().lower()
  if question12 == "b" or question12 == "maunga":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Maunga") 
    print()
  
  print("Q13: What is the Te Reo word for River: A:moana B:rakau C: D:awa ")
  question13 = input().lower()
  if question13 == "d" or question13 == "awa":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Awa ") 
    print()

  print("Q14: What is the Te Reo word for Car: A:whakaora oros B:uma C:whaaa ah D:waka")
  question14 = input().lower()
  if question14 == "d" or question14 == "waka":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Waka") 
    print()

  print("Q15: What is the Te Reo word for purity: A:karekau B:mā C:parakore D: ma ")
  question15 = input().lower()
  if question15 == "b" or question15 == "mā":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is  mā") 
    print()
  if score >= 10:
    print("You have done great, you have answered {}/15 questions!, here are some bonus questions for having such a wrinkly brain ".format(score))
    bonus_questions()
  elif score <= 10:
    end()

resp_call = respo()

#QUESTIONS GO HERE!

