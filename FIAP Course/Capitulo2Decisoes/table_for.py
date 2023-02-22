table = int(input("Type a number: "))
print("Number table ", table)
for value in range(1, 11, 1):
    print(str(table) + " x " + str(value) + " = " + str((table*value)))
