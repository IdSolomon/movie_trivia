# Movie Trivia

score = 0

option1 = 'Die Hard 3: With a Vengeance'
option2 = 'Bloodsport'
option3 = 'The Matrix'
option4 = 'Predator'
  
print("In 1999, this sci-fi/action flick took audiences by storm starring Keanu Reeves, Laurence Fishburne, and Carrie-Anne Moss.\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'C'

if answer == 'C' or answer == 'c': 
  score += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")