equipment = []
value = []
serialNumber = []
department = []

inventory = []
answer = "Y"
while answer == "Y":
    equipment.append(input("Equipment: "))
    value.append(float(input("Value: ")))
    serialNumber.append(int(input("Serial number: ")))
    department.append(input("Department: "))
    answer = input("Type Y to continue: ").upper()
for index in range(0, len(equipment)):
    print(
          "Equipment : ", index+1)
    print("Name: ", equipment[index])
    print("Value: ", value[index])
    print("Serial Number: ", serialNumber[index])
    print("Department: ", department[index])

search = input("Type the equipment you look for: ")
for index in range(0, len(equipment)):
    if search == equipment[index]:
        print("Value: ", value[index])
        print("Serial: ", serialNumber[index])

reduction = input("Type the equipment that'll be depreciated:")
for index in range(0,len(equipment)):
    if reduction == equipment[index]:
        print("Old value: ", value[index])
        print("New value: ", value[index] * 0.9)

serial = int(input("Type the Serial Number of the equipment that'll be deleted: "))
for index in range(0, len(department)):
    if serialNumber[index] == serial:
        del department[index]
        del equipment[index]
        del serialNumber[index]
        del value[index]
        break

for index in range(0, len(equipment)):
    print("Equipment: ", index+1)
    print("Name: ", equipment[index])
    print("Value: ", value[index])
    print("Serial Number: ", serialNumber[index])
    print("Department: ", department[index])
    





