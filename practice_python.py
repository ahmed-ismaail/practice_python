import os
import pandas as pd
import json



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



# Handling Data Strcutures Effectively
sales_records = [
    {"Date": "2024-01-01", "Product": "Widget A", "Sales": 200},
    {"Date": "2024-01-02", "Product": "Widget B", "Sales": 150},
    {"Date": "2024-01-03", "Product": "Widget A", "Sales": 300},
    {"Date": "2024-01-02", "Product": "Widget B", "Sales": 320}
]

print(type(sales_records))  # Check the type of sales_records
print(type(sales_records[0]))  # Check the type of the first record in sales_records


# Calculate total sales for each product
total_sales = {}
for record in sales_records:
    product = record["Product"]
    sales = record["Sales"]
    if product in total_sales:
        total_sales[product] += sales
    else:
        total_sales[product] = sales

print("Total Sales by Product:", total_sales)



# file handling (.txt) 

# If datasets/ doesn't already exist, Python will throw a FileNotFoundError. To avoid that, you can ensure the folder exists:
os.makedirs("datasets", exist_ok=True) 

# open("datasets/sample_text.txt", "w"): Opens the file in write mode ("w"), which:
# Creates the file if it doesn’t exist
# Overwrites the file if it already exists
# with: Ensures the file is properly closed after writing (even if there's an error)
# file.write(...): Writes strings to the file. \n adds a newline after each line.
with open("datasets/sample_text.txt", "w") as file:
    file.write("Hello, Data Engineering!\n")
    file.write("Working with text files in Python.\n")

# Reading from a text file
with open("datasets/sample_text.txt", "r") as file:
    content = file.read()
    print("Content of the text file:\n", content)



# CSV Files (.csv - Comma Separated Values)
# Writing a DataFrame to a CSV file
product_data = pd.DataFrame({
    "Product": ["Widget A", "Widget B", "Widget C"],
    "Price": [10.99, 14.99, 7.99],
    "Stock": [50, 20, 100]
})
product_data.to_csv("datasets/product_data.csv", index=False)

# Reading from a CSV file
df = pd.read_csv("datasets/product_data.csv") 
print("Content of product_data.csv:\n", df)




# JSON Files (.json - JavaScript Object Notation)
# Writing to a JSON file
employee_data = [
    {
        "employee_id": 101,
        "name": "Alice",
        "department": "Engineering",
        "projects": ["Project X", "Project Y"]
    },
    {
        "employee_id": 102,
        "name": "Bob",
        "department": "Sales",
        "projects": ["Project A", "Project B"]
    }
]

# "w" stands for write mode.
# If the file exists, it will be truncated (emptied) before writing new content.
# If the file does not exist, it will be created
with open("datasets/employees.json", "w") as json_file:
    json.dump(employee_data, json_file, indent=4) #pump is used to write JSON data to a file, indent=4 makes it more readable

# Reading from a JSON file
with open("datasets/employees.json", "r") as json_file:
    existing_data = json.load(json_file) # load is used to read JSON data from a file
    print("Content of employees.json:\n", existing_data)

new_employee_data = [
    {
        "employee_id": 101,
        "name": "Ahmed",
        "department": "Engineering",
        "projects": ["Project X", "Project Y"]
    },
    {
        "employee_id": 102,
        "name": "Ismail",
        "department": "Sales",
        "projects": ["Project A", "Project B"]
    },
    {
        "employee_id": 103,
        "name": "Zayan",
        "department": "Finance",
        "projects": ["Project L", "Project M"]
    }
]


# Iterates over each emp (employee) in the list existing_data
# Uses emp["employee_id"] as the key
# Uses the entire emp dictionary as the value
employee_dict = {emp["employee_id"]: emp for emp in existing_data}  # Convert list to dictionary for easier access

for new_emp in new_employee_data:
    if new_emp["employee_id"] in employee_dict:
        # If employee already exists, update their information
        employee_dict[new_emp["employee_id"]].update(new_emp)
    else:
        # If employee does not exist, add them
        employee_dict[new_emp["employee_id"]] = new_emp

updated_employee_data = list(employee_dict.values())  # Convert back to list for JSON serialization

# Writing the updated employee data back to the JSON file
with open("datasets/employees.json", "w") as json_file:
    json.dump(updated_employee_data, json_file, indent=4) #pump is used to write JSON data to a file, indent=4 makes it more readable

# Reading from a JSON file
with open("datasets/employees.json", "r") as json_file:
    new_data = json.load(json_file) # load is used to read JSON data from a file
    print("Content of employees.json:\n", new_data)


# -------------------------------------------------------------------------------------------------
# Parquet Files (.parquet - Columnar Storage Format)
# Parquet is a columnar storage file format optimized for use with big data processing frameworks.
# Writing a DataFrame to a Parquet file
user_data = pd.DataFrame({
    "user_id": range(1, 6),
    "age": [23, 35, 45, 30, 27],
    "purchase_amount": [100.5, 200.75, 300.1, 150.0, 250.5]
})
user_data.to_parquet("datasets/user_purchase.parquet", index=False)

df_user = pd.read_parquet("datasets/user_purchase.parquet")
print("Content of user_purchase.parquet:\n", df_user)
print(df_user.columns)  # Print the columns of the DataFrame



# -------------------------------------------------------------------------------------------------
# Excel Files (.xlsx - Microsoft Excel Format)
# Writing a DataFrame to an Excel file
# Writing to an Excel file
sales_data = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=5, freq="D"), # Generates a date range starting from 2024-01-01 for 5 days
    "Product": ["Widget A", "Widget B", "Widget A", "Widget B", "Widget C"],
    "Sales": [200, 150, 300, 250, 100]
})
sales_data.to_excel("datasets/sales_data.xlsx", index=False)

df_sales = pd.read_excel("datasets/sales_data.xlsx")
print("Content of sales_data.xlsx:\n", df_sales)
print(df_sales.columns)  # Print the columns of the DataFrame




# -------------------------------------------------------------------------------------------------
# 1. Titanic Sample Data (CSV)
titanic_data = pd.DataFrame({
    "PassengerId": [1, 2, 3, 4, 5, 3, 5],  # Duplicate Passenger IDs for demonstration
    "Survived": [0, 1, 1, 0, 1, 1, 1], # Adding duplicate Survived values
    "Pclass": [3, 1, 3, 1, 3, 3, 3], # Adding duplicate Pclass values
    "Name": ["John Doe", "Jane Smith", "Alice Brown", "William Johnson", "Linda Lee", "Alice Brown", "Linda Lee"],  # Duplicate Names
    "Sex": ["male", "female", "female", "male", "female", "female", "female"],
    "Age": [22, 38, None, 35, None, None, 28],  # Adding null values in Age
    "Fare": [7.25, 71.2833, None, 53.1, 8.05, None, 8.05]  # Adding null values in Fare, with duplicates
})

titanic_data.to_csv("datasets/titanic.csv", index=False)

# Loading the Titanic dataset
df_titanic = pd.read_csv("datasets/titanic.csv")
print("First 5 rows of Titanic dataset:\n", df_titanic.head()) #head() displays the first 5 rows of the DataFrame


# Data Cleaning and Preprocessing Techniques
print("Missing values:\n", df_titanic.isnull().sum())

df_titanic['Age'].fillna(df_titanic['Age'].median(), inplace=True) # Fill missing Age values with the median, inplace=True modifies the DataFrame directly without creating a new one
df_titanic.dropna(subset=['Fare'], inplace=True) # Drop rows where Fare is missing, inplace=True modifies the DataFrame directly without creating a new one


print("Data after handling missing values:\n", df_titanic.isnull().sum()) 

df_titanic.drop_duplicates(inplace=True)  # Remove duplicate rows, inplace=True modifies the DataFrame directly without creating a new one
print("Data after removing duplicates:\n", df_titanic.shape) 

#--------------------------------------------------------------------------------------------------
