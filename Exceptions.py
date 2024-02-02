name= input("What is your name?")
age=input("How old are you?")
# print("Hello,", name, "!", sep="")
try:
 age=int(age)
 birth_year=2024-age
 print("You were born in",birth_year, ".",sep="")
 number= input("give me a number to divide the age")
 number=int(number)
 print(age/number)
except ValueError:
 print("Invalid age. Please enter a number")
except ZeroDivisionError:
 print("you cannot divide by zero.")
else:
    print("No exceptions were raised.")
finally:
    print("thank you for playing")