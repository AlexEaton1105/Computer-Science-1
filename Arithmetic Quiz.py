import time
import random

question = 1
number1 = 1
number2 = 1
o = 1
score = 0
NAME = ""

def add(x, y):

   return x + y

def subtract(x, y):

   return x - y

def multiply(x, y):

   return x * y

while NAME == "":
   time.sleep(1)
   NAME = input("Hello, \nWhat is your name? ")
   
print("Welcome to this maths quiz", NAME, "Good luck")
time.sleep(1)
print("Please only type numbers as answers or this will crash the quiz")

time.sleep(1)

while question <= 10:
    number1 = random.randint(0, 12)
    number2 = random.randint(0, 12)
    operator = random.randint(1, 3)
    if operator == 1:
       print(number1,"+",number2)
    elif operator == 2:
      print(number1,"-",number2)
    elif operator == 3:
      print(number1,"*",number2)

    if operator == 1:
       ans = add(number1,number2)
    elif operator == 2:
      ans = subtract(number1,number2)
    elif operator == 3:
      ans = multiply(number1,number2)

    answer = int(input())
    
    if answer == ans:
        print("Correct")
        score = score + 1
    else:
        print("False, the answer was actually", ans)
        

    question = question + 1


if score < 5:
   print("Unfortunatly your score was", score)

else:
   print("Amazing, your score was", score)