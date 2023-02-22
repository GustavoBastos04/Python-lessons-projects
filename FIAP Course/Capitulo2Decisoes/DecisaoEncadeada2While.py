name=input("Type your name: ")
age=int(input("Type your age: "))
illness=input("Illness suspect? ").upper()

# FIRST PROBLEM
while illness!="YES" or "NO":
    print("Type YES or NO")
    illness = input("Illness suspect?").upper()

if illness=="YES":
    print("Patient needs to go to YELLOW room")
else:
    print("Patient needs to go to WHITE room")

# SECOND PROBLEM TO BE SOLVED
if age>= 65:
    print("Priority patient")
else:
    gender=input("Type patient gender: ").upper()
    if gender=="FEMALE" and age>10:
        pregnancy=input("Is the patient pregnant? ").upper()
        if pregnancy=="YES":
            print("Priority patient")
        else:
            print("No priority patient")
        