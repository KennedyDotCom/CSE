#  Lists
shopping_list = ["whole milk", "Xbox One", "Trash"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))
# Lopping through lists
for item in shopping_list:
    print(item)

'''

1. Make a List
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''
new_list = ["eggs", "cheese", "oranges", "raspberries"]
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list) - 1])
print(new_list)

# Getting part of a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:2])

# Adding things to a List
christmas_list = []  # Always use square brackets
christmas_list.append("Tacos")
christmas_list.append("Bumblebee")
christmas_list.append("Red Dead Redemption 2")
print(christmas_list)

# Notice this is "object.method(Parameter)"

# Removing Things from a list
christmas_list.remove("Tacos")
print(christmas_list)

bo4_list = []
bo4_list.append("Prestige Master")
bo4_list.append("Dark Matter")
bo4_list.append("Level 80")
print(bo4_list)

bo4_list.remove("Level 80")
print(bo4_list)

# ALSO removing things from a list
bo4_list.pop(0)
print(bo4_list)

# Tuple
brands = ("Apple", "Samsung", "HTC")  # Notice the parentheses


colors = ["blue", "red", "green", "brown", "gold", "pink", "cyan", "purple", "teal", "white"]
print(len(colors))

# Find the Index
print(colors.index("gold"))

# Changing things into list
string1 = "white"
list1 = list(string1)
print(list1)

for character in list1:
    if character == "w":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")


# Changing list into strings
print("".join(list1))