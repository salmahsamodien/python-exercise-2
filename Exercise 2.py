# Question 1: Arithmetic and Assignment Operators
x = 5
x += 3
y = 10
y *= 2
result = x/y 
print(result)

# Question 2: Comparison and Logical Operators
a = 10
b = 4
c = 7 
condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a
final_condition = (a > b) or (b % 2 == 0  and c <= a) 
print(final_condition) 

# Question 3: Conditional Statements
score = int(input("enter the test score (0-100):"))
if score > 90:
  print("A")
elif score >=80:
  print("B")  
elif score >=70:
  print("C")
elif score >=60:
  print ("D") 
else:
  print ("F")

# Question 4: Combining Operators and Conditionals
num1 = float(input("give a number: ")) 
num2 = float(input("give a number: "))
operation = input("put the operation, and store it in (+, -, *, ):") 
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
    result = num1 / num2
    print("Invalid operation")

# TODO: Print the result of the operation
num1 = float(input("10:"))
num2 = float(input("5:"))
operation = input(" (+, -, *, ):")
