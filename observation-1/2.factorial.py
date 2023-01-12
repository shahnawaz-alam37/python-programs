n = int(input("Enter the number to get factorial:"))
fact = 1
i = 1
for i in range(1,n+1):
    fact = fact * i

print(f"factorial is {fact}")