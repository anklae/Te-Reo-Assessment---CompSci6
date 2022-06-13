import os
import time

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
statement_generator("Welcome to the Te Reo Maori test!","%")
print()
print("This test has 15 multiple choice questions")
time.sleep(.5)
print()
print("if you get 10 or more of the 15 questions correct you will be granted several bonus questions")
#This function asks the user if they would like to proceed
score = 0
def respo():
  response = input("Would you like to proceed ").lower()
  print()
  if response == "yes" or response  == "y":
    response == "yes"
    question_hab()
    os.system('clear')
  elif response == "no" or response == "n":
    response = "no"
    print("Have a good day")
  else:
    print("Please answer Yes/No")
    print()
    respo()

#This Function starts the quiz and shows the questions when called apon

def end():
  global score
  statement_generator("Results", "=")
  statement_generator("You got a score of {} out 29 points".format(score), "*")
  if score <= 5:
    print("you did not do very well, you could do way better")
  elif score >=5 and score <= 9: 
    print("You did alright, well done")
  if score >= 10 and score <= 14:
    print("Good job , you almost answered half of the questions correctly ")
  if score >= 15 and score <= 20:
    print("Great job, you got more than half of the questions correct")
  if score >= 25:
    print("You did amazing!!!! You got almost all the questions correct!!")
  if score == 29:
    statement_generator("😱😱😱YOU ABSOLUTELY ACED THE TEST😱😱😱","!")
  if score >= 29:
    print("how have you done this")
def question_hab():
  global score
  score = 0
  print("Q1: What is the Te Reo word for Hello?: A:wharepaku B:karekau C:kia ora D:takaro")
  question1 = input().lower()
  if question1 == "c" or question1 == "kia ora":
    score += 29
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

  print("Q12:What is the Te Reo word for Mountain: A:awhe B:maunga C:puke D:pepi ")
  question12 = input().lower()
  if question12 == "b" or question12 == "maunga":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Maunga") 
    print()
  
  print("Q13: What is the Te Reo word for River: A:moana B:rakau C:oro D:awa ")
  question13 = input().lower()
  if question13 == "d" or question13 == "awa":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is Awa ") 
    print()

  print("Q14: What is the Te Reo word for Car: A:whakaora oros B:uma C:whaaa ah D:motoka")
  question14 = input().lower()
  if question14 == "d" or question14 == "motoka":
    score += 1 
    print("Correct!")
    print()
  else: 
    print("Incorrect, The Answer is motoka") 
    print()

  print("Q15: What is the Te Reo word for purity: A:karekau B:mā C:parakore D: ma")
  question15 = input().lower()
  if question15 == "b" or question15 == "mā":
    score += 1 
    print("Correct!")
    print()
    
  else: 
    print("Incorrect, The Answer is  mā") 
    print()
  if score >= 10:
    print()
    print("You have done great, you have answered {}/15 questions!, here are a few bonus questions for having such a wrinkly brain".format(score))
    print()
    time.sleep(4)
    os.system('clear')
    time.sleep(0.5)
    bonus_questions()
  elif score <= 10:
    end()


def bonus_questions():
  global score
  print("These bonus questions will give you 2x more points, Make sure to try your best")
  print()
  print("Bonus #Q1:What is the te reo word for bread?: A:taro B:kongakonga taro c:takakau D:Te petipeti")
  bonus_question = input().lower()
  if bonus_question == "a" or bonus_question == "taro":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is taro")
    print()

  print("Bonus #Q2: What is the maori word for Hatchet?: A:rangatira B:toki C:paotahi D: patu")
  bonus_question2 = input().lower()
  if bonus_question2 == "c" or bonus_question2 == "paotahi":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is paotahi")
    print()
  
  print("Bonus  #Q3: what is the Te reo word for porcupine?: A:porcupine B:poaka C:rotarota D:goorg ")
  bonus_question3 = input().lower()
  if bonus_question3 == "a" or bonus_question3 == "porcupine":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is porcupine")
    print()

  print("Bonus #Q4: What is the te reo word for plane?: A:sanguis B:hanawiti C: whenua D:rererangi ")
  bonus_question4 = input().lower()
  if bonus_question4 == "d" or bonus_question4 == "rererangi":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is rererangi ")
    print()

  print("Bonus #Q5: What is the te reo word for wing? A:tuna B:hau C:parirau D:Kararehe pakau")
  bonus_question5 = input().lower()
  if bonus_question5 == "c" or bonus_question5 == "parirau":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is parirau")
    print()
  
  print("Bonus Question #Q6: What is the te reo word for High school?: A:te kura tuarua B:rekereke C:pourewa D:mokete")
  bonus_question6 = input().lower()
  if bonus_question6 == "a" or bonus_question6 == "te kura tuarua":
    score += 2
    print("Correct!")
    print()
  else:
    print("Incorrect, The answer is te kura tuarua")
    print()

  print("Bonus #Q7: What is the te reo word for berserk?: A:puku B:whakapouri c:kaha te hopu D:hake")
  bonus_question7 = input().lower()
  if bonus_question7 == "b" or bonus_question7 == "whakapouri":
    score += 2
    print("Correct!")
    end()
  else:
    print("Incorrect, The answer is whakapouri")
    print()
    end()
        
#calls the respo function
resp_call = respo()
end()

#QUESTIONS GO HERE!