import random
#functions go here 

def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()
    
    if response == "yes" or response  == "y":
      response == "yes"
      return response
  
    elif response == "no" or response == "n":
      response = "no"
      return response
    
 
    else:
      print("Please answer Yes/No")
  



def instructions(): 
  print("How To Play")
  print()
  print("**The rules of the game: You can only select an ammount between $1-$10 to play with, if your balance goes under $1 the game stops")
  print()
  return ""


def num_check(question, low, high):
  error = "Please select a number between 1 and 10"
  
  valid = False
  while not valid:
    try:
      #ask the question 
      response = int(input(question))
      #if the ammount is too low/ too high give 
      if low < response <= high:
        return response
    
      #output the error
      else:
        print(error)
    
    except ValueError:
      print(error)
 
 
#main routine goes here 

def statement_gen(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)
  
  return ""



played_before = yes_no("Have you played the game before? ")

if played_before == "no":  
  instructions()

print()
#Ask the user how much the want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)


#set your balance for testing purposes
balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play... ").lower()
while play_again == "":

  #increase # of rounds played
  rounds_played += 1

  #print round number
  print()
  print("*** Round #{} ***".format(rounds_played))
  chosen_num = random.randint(1,100)
  
  #Adjust balance 
  #If the random # is between 1 and 5, user gets a unicorn (add $4 to balance)
  if 1 <= chosen_num <= 5:
    chosen = "Unicorn"
    balance += 4 
  
  #if the random # is between 6 and 36
  #user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "Donkey"
    
    balance -= 1
  
  #The token is either a horse or zebra...
  #in both cases subtract $0.50 from the balance
  else :
    #if the number is even, set the chosen item to a horse
    
    if chosen_num % 2 == 0 :
      chosen = "Horse"
     
    #otherwise set it to Zebra
    else: 
      chosen = "Zebra"
      prize_decoration = "Z"
      balance -= 0.5

  #output
  print("You got a {}.  Your balance is ""    ${:.2f}".format(chosen, balance))
  
  
  if balance < 1:
    play_again = "xxx"
    print("Sorry you have ran out of money")
  else:
    print(chosen_num)
    play_again = input("Press enter to play again or 'xxx' to quit: ")

print()
print("Final Balance", balance)

