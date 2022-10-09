x_str = input("Enter a number: ")
x = int(x_str)
if x == 1:
    print(f"{x} is 1")
    print("This is part of if")
elif x == 2:
    print(f"{x} is 2")
    print("this is part of elif")
else:
    print(f"{x} is not 1")
    print("this is part of else")
