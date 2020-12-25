first_name = str(input("First Name: "))
last_name = str(input("Last Name: "))
age = int(input("Your Age: "))
date_of_birth = int((input("Date of birth(Just Year): ")))
a=list([first_name , last_name , age , date_of_birth])
for i in a:
    print(i)
if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")
