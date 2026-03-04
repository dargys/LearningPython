# #y = "dargys"
# # print(x)
# # def my_capitalize(my_string):
# #     x = my_string.capitalize()
# #     return x

# #print( my_capitalize(y))

# # 1

# temperature = 25

# if temperature > 25:
#     print ("HOT")
# else : print ("COLD")

# # 2 

# Number = 5

# if Number % 2 == 1:
#     print("Odd")
# else : print ("Even")

# # 3 

# Salary = 20000

# if Salary >= 50000 :
#     print("High")
# elif Salary >= 30000:
#     print("Medium")
# else : print("Low")

# # 4 




# def check_ticket_price(age, is_student):
#     if age < 18:
#         return "Child ticket"
#     elif age >= 18 and is_student:
#         return "Student discount"
#     else:
#         return "Full price"


# age = int(input("What is your age? "))
# is_student = input("Are you student? (y/n): ") == "y"

# print(check_ticket_price(age, is_student))



#phone_number = "+46 (176) 123-6788"

#print(phone_number.replace("+","00").replace(" ","").replace("-","").replace("(","").replace(")",""))

#strip

#print(phone_number[-3:])

# Lista är en behållare som innehåller flera saker

# number = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10,
#     "Kimmo",
#     "Ahola",
#     None,
#     True,
# ]  # kan stoppa in vad som helst

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# print(number)

# number.append(11)
# number.append(12)

# number.insert(0, 0)

# print(number)

# print(number[1:10])

# print(number)

# counter = 0
# while counter < len(number):
#     print(number[counter])
#     counter = counter + 1

# for n in number:  # Pythonic
#     print(n)

# for index, n in enumerate(number):  # enumerate gives position for index
#     if n % 2 == 0:
#         print(f"pos: {index}, value: {n}")

# print(number)
# number.remove(2)
# print(number)

# country = "USA"
# print(country.isalpha())

# phone = "123456789"
# print (phone.isnumeric())

# import math

# price = 35.543435
# print(round(price,2))
# print(math.floor(price))
# print(math.ceil(price))

email = ""
phone = "123456789"
username = ""
print (any([email,phone,username]))

print (all([email,phone,username]))