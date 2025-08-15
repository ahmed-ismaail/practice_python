
print("hello world") 

#variables
age = 27
print("I am", age, "years old")

name = "ahmed zayan"
print("My name is", name)

is_student = False
print("Am I a student?", is_student)


# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)#power

# Operator behavior with different data types

# Addition with numbers
num1 = 10
num2 = 20
print(num1 + num2)

# Concatenation with strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# Repetition with strings
print(str1 * 3)



# Logical Operators
x = True
y = False
print("Logical AND:", x and y)
print("Logical OR:", x or y)


#if else statements
product_stock = 200
if product_stock > 150:
    print("Product is in high stock")
elif product_stock > 100:
    print("Product is in medium stock")
else:
    print("Product is in low stock")



#for loop example
products = ["a", "b", "c", "d"]
stock_levels = [200, 150, 80, 50]
for product, stock in zip(products, stock_levels):
    if stock > 100:
        print(f"{product} is in high stock")
    elif stock > 50:
        print(f"{product} is in medium stock")
    else:
        print(f"{product} is in low stock")    


#replace the above 2 lists with dictionaries
products = {
    "a": 200,
    "b": 150,
    "c": 80,
    "d": 50
}
# Iterate through the dictionary and print stock levels
for product, stock in products.items():
    if stock > 100:
        print(f"{product} is in high stock")
    elif stock > 50:
        print(f"{product} is in medium stock")
    else:
        print(f"{product} is in low stock")   


# While loop example
count = 0
while count < 5:
    print("Count:", count)
    count += 1


# Function to calculate average stock from product data
def calculate_average_stock(stock_list):
    total_stock = sum(stock_list)
    return total_stock / len(stock_list)# len() returns the number of items in the list

# Using the function with stock levels from product_data
average_stock = calculate_average_stock(stock_levels)
print("Average stock level:", average_stock)



# Syntax example for a lambda function
add = lambda x, y: x + y  # Adds two numbers
print(add(3, 5))


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))  # Squares each number in the list 
print("Squared numbers:", squared)


words = ["hello", "world", "python"]
uppercase_words = list(map(lambda x: x.upper(), words))  # upper each word in the list
print("uppercase words:", uppercase_words)


# String concatenation example
employee_name = "ahmed zayan"
# Concatenation
greeting = "Hello, " + employee_name + "!"
print(greeting)


department = "BI REPORTING"
print(f"welcome to {employee_name} in {department} department")  # f-string for formatted string literals


# slicing example
sample_text = "This is a sample text for string manipulation."
print(f" first 10 characters: {sample_text[:10]}")  # Slicing to get the first 10 characters
print(f" last 13 characters: {sample_text[-13:]}")  # Slicing to get the last 13 characters
print(f" middle 11 characters: {sample_text[10:21]}")  # Slicing to get the middle 11 characters


# String Methods
print("Lowercase:", sample_text.lower())
print("Uppercase:", sample_text.upper())
print("Replace:", sample_text.replace("text", "example"))


# Error handling when reading a non-existent file
try:
    with open("datasets/nonexist_file.csv", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")    
else:
    print("File read successfully.")
finally:
    print("Execution completed.")


# Tuples
# A tuple is a collection of ordered, immutable (unchangeable) elements.
# Unlike lists ([]), tuples use parentheses ().
# Defining a tuple
coordinates = (51.5074, -0.1278)  # Coordinates for London

# Accessing tuple elements
latitude = coordinates[0]
longitude = coordinates[1]

print(f"Latitude: {latitude}, Longitude: {longitude}")



# Lists 
# A list is a collection of ordered, mutable (changeable) elements.
# Defining a list of product names
product_names = ["Widget A", "Widget B", "Widget C"]

# Adding a new product
product_names.append("Widget D")

# Removing a product
product_names.remove("Widget B")

# Printing the updated list
print("Updated product names:", product_names)



# Sets
# A set is a collection of unique, unordered elements.
# Sets are defined using curly braces {} or the set() function.
# Defining a set of unique product IDs
product_ids = {101, 102, 103, 104, 101}  # Duplicates are ignored
# product_ids = set([101, 102, 103, 104, 101])  # same as above

# Adding a new unique ID
product_ids.add(105)

# Removing an ID
product_ids.discard(102)

print("Unique product IDs:", product_ids)



# Dictionaries
# A dictionary is a collection of key-value pairs, where each key is unique.
# Defining a dictionary for a product with key-value pairs
product_info = {
    "Product ID": 101,
    "Name": "Widget A",
    "Price": 9.99,
    "Stock": 100
}

# Accessing values by keys
product_name = product_info["Name"]
product_price = product_info["Price"]

# Adding a new key-value pair
product_info["testkey"] = "testvalue"

# Updating the stock count
product_info["Stock"] = 120

print("Product Information:", product_info)