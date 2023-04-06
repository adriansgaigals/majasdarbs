list = []

while True:

user_input = input("Enter a '(' or ')' character (or multiple characters): ")

for char in user_input:

if char == '(':

list.append(char)

elif char == ')':

if len(list) > 0:

list.pop()

else:

print("Error: Nav atrastas verošās iekavas.")

else:

print("Error: Invalid input.")

continue

iekavas1 = list.count('(')

iekavas0 = len(list) - iekavas1

if iekavas1 > iekavas0:

print("There are", iekavas1 - iekavas0, "more '(' characters than ')' characters.")

elif iekavas0 > iekavas1:

print("There are", iekavas0 - iekavas1, "more ')' characters than '(' characters.")

else:

print("The number of '(' and ')' characters is equal.")