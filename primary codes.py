name = "saman"
age = 23
is_active = True

print(name + "is a IT student, who is" + str(age) + "years old, and he is :"+ str(is_active))

#simple login command - if/else
user_name = str(input("Enter User name: "))
pass_word = str(input("Enter Password: "))

if user_name == "User name" and pass_word == "1234":
    print("Login Sucessfully")
else:
    print("Loagin fail")