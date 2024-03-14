#if statements
age = int(input("How old are you? "))

if age >= 40:
    print("Life begins at 40")
    print("Congratulations")
elif age >= 18:
    print("You are an adult")
elif age <= 0:
    print("Invalid age")
else:
    print("You are still a child")

    #logical operators in Python
    #they include (and,or,not)

Temperature = int(input("What is the temperature today? "))

if Temperature >= 30 and Temperature <=45:
        print("The temperature is awesome")
        print("A good day to go outside!")
elif Temperature < 30 or Temperature > 45:
        print("The temperature is bad today")
        print("You should probably stay inside!")

#using the not logical operator
Temperature = int(input("What is the temperature today? "))

if not(Temperature >= 30 and Temperature <=45):
        print("The temperature is bad today")
        print("You should probably stay inside!")
        
elif not(Temperature < 30 or Temperature > 45):
        print("The temperature is awesome")
        print("A good day to go outside!")
        

