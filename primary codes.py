name = "saman"
age = 23
is_active = True

print(name + "is a IT student, who is" + str(age) + "years old, and he is :"+ str(is_active))

#simple login command - if/else
user = str(input("Enter User name: "))
password = str(input("Enter Password: "))

if user == "User name" and password == "1234":
    print("Login Sucessfully")
else:
    print("Log in fail")


#function - reusable 
def login(user, password):
    if user == "user" and password == "1234":
        return True
    return False

user = input("Enter username: ")
password = input("Enter password: ")

if login(user, password):
    print("Login successful")
else:
    print("Invalid username or password")

#function - method
def add(a, b):
    return a + b

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

result = add(a, b)
print(result)

#Mini Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


print("Mini Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose operation (1/2/3/4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(a, b))
elif choice == "2":
    print("Result:", subtract(a, b))
elif choice == "3":
    print("Result:", multiply(a, b))
elif choice == "4":
    print("Result:", divide(a, b))
else:
    print("Invalid choice")
