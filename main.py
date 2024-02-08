num1 = int(input("Enter your first number: "))
op = input("Enter an operator: ")
num2 = int(input("Enter your second number: "))

if op == "+":
  print(f"{num1} + {num2} = {num1+num2}")
elif op == "-":
  print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
  print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
  if num2 ==0:
    print("Cannot divide by 0.")
  else:
    print(f"{num1}/{num2} = {num1 / num2}")
elif op == "**":
  print(f"{num1} ** {num2} = {num1 ** num2}")
elif op == "//":
  if num2 ==0:
    print("Cannot divide by 0.")
  else:
    print(f"{num1} // {num2} = {num1 // num2}")
elif op == "%":
  if num2 ==0:
    print("Cannot divide by 0.")
  else:
    print(f"{num1}%{num2} = {num1 % num2}")
else:
  print("User input invalid, try again.")
  print("Valid operators: +, -, *, /, **, %, //.")

 


