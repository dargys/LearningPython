#y = "dargys"
# print(x)
# def my_capitalize(my_string):
#     x = my_string.capitalize()
#     return x

#print( my_capitalize(y))

# 1

temperature = 25

if temperature > 25:
    print ("HOT")
else : print ("COLD")

# 2 

Number = 5

if Number % 2 == 1:
    print("Odd")
else : print ("Even")

# 3 

Salary = 20000

if Salary >= 50000 :
    print("High")
elif Salary >= 30000:
    print("Medium")
else : print("Low")

# 4 

age = int(input("What is your age?"))
is_student = input ("Are you student?(y/n)")

if age < 18 :
    print("Child ticket")
elif age >= 18 and is_student == "y":
    print ("Student discount")
else :
    print("Full price")