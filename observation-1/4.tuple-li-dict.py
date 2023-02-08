# creating a tuple of numbers
numbers = (1, 2, 3, 4, 5)

# creating a list of strings
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# creating a dictionary with numbers as keys and fruits as values
fruit_dict = {
    "1":"mango",
    "2":"apple"
}

# printing the elements of the tuple
print("Elements of the tuple:")
for num in numbers:
    print(num)

# printing the elements of the list
print("\nElements of the list:")
for fruit in fruits:
    print(fruit)

# printing the elements of the dictionary
print("\nElements of the dictionary:")
for key, value in fruit_dict.items():
    print(f"{key}: {value}")