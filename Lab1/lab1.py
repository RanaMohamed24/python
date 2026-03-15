#task 1 :

number = 15
start = 10
end = 20

if number >= start and number <= end:
    print(True)
else:
    print(False)


#task 2 :

age = 20
coupon = True

if age < 18 or age > 65 or coupon == True:
    print(True)
else:
    print(False)

#task 3 :

name = "Rana"

Hello = "Hello, " + name + "!"
print(Hello)

#task 4 :

full_name = "Rana Mohamed"

first_name = full_name[0]
last_name = full_name[5]

initials = first_name + last_name
print(initials)  

# full_name = "Rana Mohamed"

# first_name = full_name[0]
# last_name = full_name.split()[1][0]  

# initials = first_name + last_name
# print(initials)  


#task 5 :
name = "Rana"
age = 22

sentence = "{} is {} years old.".format(name, age)
sentence2 = "{name} is {age} years old.".format(name=name, age=age)


print(sentence)
print(sentence2)