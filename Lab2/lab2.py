import math
# Task 1:

word = input("Enter a word: ")
def remove_vowels(word):
    new_word = ""
    for char in word:
        if char.lower() not in "aeiou":
            new_word += char
    return new_word
result = remove_vowels(word)
print("Word without vowels:", result)


# Task 2:

text = input("Enter a string: ")
letter = input("Enter a letter: ")
positions = []
for i in range(len(text)):
    if text[i] == letter:
        positions.append(i)

print("Positions:", positions)

# Task 3:

number = int(input("Enter a number: ")) #4
def multiplication_table(number):  #4
    table = []  
    for i in range(1, number + 1): #1 ,2,3,4
        row = []  
        for j in range(1, i + 1):  
            row.append(i * j)  
        table.append(row)  
    return table

print(multiplication_table(number)) #[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]]

# Task 4:

def calculate_area(shape, num1, num2=None):
    if shape == "t":
        return 0.5 * num1 * num2      
    elif shape == "r":
        if num2 is not None:
            return num1 * num2           
        else:
            return num1 * num1          
    return math.pi * num1 ** 2     

print(calculate_area("t", 10, 7))  
print(calculate_area("r", 10, 7))    # rectangle

print(calculate_area("r", 10))      # square
print(calculate_area("c", 10))      


# Task 5:

def the_dictionary(**kwargs):
    result = {}
    for name in kwargs.values():
        key = name[0].lower()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return dict(sorted(result.items()))

print(the_dictionary(n1="ahmed", n2="amena", n3="Ibrahim"))

# Task 6:
def Stars(number):
    for i in range(1, number + 1):
        print("*" * i)

number = int(input("Enter a number: "))
Stars(number)



# def Stars(number):
#     shape = []
#     for i in range(1, number + 1):
#         shape.append("*" * i)
#     return "\n".join(shape)