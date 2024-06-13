#MINH TRAN
#M02 Lab - Case Study: if...else and while
#FILE NAME: main.py
#Python app that will accept student names and GPAs and 
# test if the student qualifies for either the Dean's List or the Honor Roll.


while True:
    last_name = input("Your last name OR enter ZZZ to quit: ")
    if last_name == "ZZZ":
        print("Quit the program")
        break
    first_name = input("Your first name: ") 
    GPA = float(input("Your GPA: "))
    if GPA >= 3.5:
        print(first_name,last_name,"has made the Dean's List.")
    elif GPA>=3.25:
        print(first_name,last_name,"has made the Honor Roll.")
    else:
        print("nothing")
