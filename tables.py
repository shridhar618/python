

from tkinter import END


num=int(input("Enter a number you want to get tables of it:"))
def tables():
    for i in range(1,11):
        result=num*i
        print(num,"X",i,"=",result)
if num>0:
    tables()
elif num<0:
    tables()
else:
    print("You entered a null value...it cannot be accessed\n   Sorry...")
    
    

    
