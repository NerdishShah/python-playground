number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print("Choices Available are ")
print("1 - Add")
print("2 Subtract")
print("3 - Divide")
print("4 - Multiply")

choice = int(input('Enter the choice: '))

if choice == 1:
    print(f"Result = {number1 + number2}")
elif choice == 2:
    print(f"Result = {number1 - number2}")
elif choice == 3:
    print(f"Result = {number1 / number2}")
elif choice == 4:
    print(f"Result = {number1 * number2}")
else:
    print("Invalid Operation")
