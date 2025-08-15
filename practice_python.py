
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