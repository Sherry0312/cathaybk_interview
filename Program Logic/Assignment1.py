value = int(input("Enter the Value:"))

if value % 2 == 1:
    print("X")
elif value % 2 == 0 and 2 <= value < 5:
    print("O")
elif value % 2 == 0 and 6 <= value <= 20:
    print("X")
elif value % 2 == 0 and value > 20:
    print("O")
