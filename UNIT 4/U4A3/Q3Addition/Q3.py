import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

print(str(number1)+("+")+str(number2)+("="))
number4 = int(input())

number3 = int(number1 + number2)

if number4 == number3:
  print("Correct")

else:
  print("Incorrect")