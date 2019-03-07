import time
print('''Hello there! I am a bot who is able to beat anyone in "paper, rock, scissors!" Just input your move (paper, rock, or scissors) and I'll be able to choose a move that beats yours! Try it.''')
again = None
move = input("What is your move? ").lower()
computerScore = 0
def playagain():
  global move
  global again
  again = input("Do you want to play again? ").lower()
  if again == "yes" or again == "yeah":
    move = input("What is your next move? ").lower()
  elif again == "no" or again == "nah":
    print("Thanks for playing!")
    time.sleep(3)
    quit()
  elif again != "yes" or again != "no" or again != "yeah" or again != "nah":
    print("Are you sure you didn't make a typo?")
    again = input("Do you want to play again? ").lower()


while again != "no" or again != "nah":
  if move == "rock":
    print("I pick paper!")
    computerScore = computerScore+1
    print("Current score: Human | 0 - " + str(computerScore) + " | Computer")
    playagain()
  elif move == "paper":
    print("I pick scissors!")
    computerScore = computerScore+1
    print("Current score: Human | 0 - " + str(computerScore) + " | Computer")
    playagain()
  elif move == "scissors":
    print("I pick rock!")
    computerScore = computerScore+1
    print("Current score: Human | 0 - " + str(computerScore) + " | Computer")
    playagain()
  elif move != "rock" or move != "paper" or move != "scissors":
    print("Are you sure you didn't make a typo?")
    move = input("Please type your next move. ").lower()