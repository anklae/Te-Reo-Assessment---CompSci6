import time
time.sleep(.5)

response = input("Hello, Welcome to the Te Reo Quiz, Would you like to proceed? ").lower()

if response == "yes" or response == "y":
    print("Great! Lets get started!")
    quiz()
elif response == "no" or response == "n":
    print("Goodbye")
else: 
  print("Please answer Yes or no")

  
  
def quiz():
  print("What is the maori word for 'toilet' ")
  print("A: Whare")
  print("B: ")
  