print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
print("**************************\n")
name2 = input("What is their name?\n") 
print("**************************\n")

combine_name=name1+name2
lower_names=combine_name.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
first_digit=t+r+u+e

l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit=l+o+v+e

score=int(str(first_digit)+str(second_digit))

if (score>10) or (score<50):
  print(f"Your score is {score},Your love is like mentos and coke")
elif (score<10):
  print(f"Your score is {score}, Your love is impossible")
elif (score>50):
  print(f"Your score is {score}, Your love is like ram and sita")
else:
  print(f"Your score is {score}, Your love is unbelievable")


