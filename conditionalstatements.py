# if else statements
num = int(input("Enter Number : "))
if num > 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a Negative Number")

age=int(input("Enter Age to vote: "))
if age >= 18 and age<=81 :
    print("You are eligible to vote")
else:
    print("Sorry you are not eligible to vote. Right age to vote is between 18 and 81")