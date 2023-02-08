a = 10
b = 20
print(f"a = {a}, b = {b}")
# if statement
if a > b:
    print("a > b")

# if-else statement
if a == b:
    print("a equals b")
else:
    print("a != b")

# if elif and else statement
if a == b:
    print("a == b")
elif a > b:
    print("a > b")
else:
    print("a < b")

# if else ladder
if a > 10:
    print("a > 10")
    if a > b:
        print("a > b")
    else:
        print("a < b")
else:
    print("a != 10")