import random
print("number guesing game")
number = random.randint(1, 9)
chances = 0
print("guess a number (between 1 and 9):")

while chances < 5:

   guess =int(input("enter your guess:-"))

   if guess == number:
      print("congragulation you won!!!")
      break
   
   elif guess < number:
      print("your guess was too low: Guess a number higher than", guess)

   else:
      print("your guessing was too high: Guess a number lower than", guess)

   chances +=1

if not chances < 5:
   print("YOU LOSE!!! the number is", number)
