from random import *
score = 0
playing = True
doors = 0
print("""
Gameshow!
========
There is a numbers behind 3 doors!
Guess the correct door to get the biggest score!

     _________          __________           __________
   |           |      |            |       |            |          
   |           |      |            |       |            |        
   |    [1]    |      |     [2]    |       |     [3]    |        
   |           |      |            |       |            |     
   |          0|      |         0  |       |          0 | 
   |           |      |            |       |            |      
   |           |      |            |       |            |        
   | _________ |      | __________ |       | __________ |

""")
while score < 21:

  print("\nChoose a door (1,2 or 3)")

  choosendoor = input()
  choosendoor = int(choosendoor)

  windoor = randint(1,10)

  print("\nThe coosen door is",choosendoor)
  print("The score behind the door is",windoor)

  score = (score + windoor)
  doors = (doors + 1)
  if score > 21:
   print("\nYour score more than 21")
  else:
    print("Your score is",score)
if score > 20:
  print("Your opened",doors,"doors to win!")   
if score == 21:
  print("Exactly result, your score is 21")
