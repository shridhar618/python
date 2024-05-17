print("Hi! Welcome " +input("What is your name?\n") + "!")


print("BMI calculator")
weight=int(input("Enter your weight in kilo gram\n"))
height=float(input("Enter your height in meter\n"))
age=int(input("Enter your age\n"))

bmi=weight/height**2


if bmi<18:
    print(f"Your bmi was {bmi}"+ "\nYou are under weighted")
elif bmi<25:
    print(f"Your bmi was {bmi}"+ "\nYour weight is normal")
    if age<12:
        print("You have to pay only 50rs for horse riding")
    elif age>=12:
        print("You have to pay 100 rs for horse riding")
else:
    print(f"Your bmi was {bmi}"+ "\nYou are over weighted")

