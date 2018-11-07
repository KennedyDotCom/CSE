print("Hello World!")
print()
# This is a comment . I can write whatever I want
# Here and it won't do anything about it.
# It has no effect on the code.
print()  # This adds extra spaces spaces on the terminal
print("This will print here. Notice the spacing")

a = 4
b = 3
print(a + b)
print(5 - 3)
print(6 / 5)  # Results in a float
print(a * 5)

print("Figure thus out")
print(6 // 4)
print(12 // 3)  # Results in a integer
print(9 // 4)

car_name = "Thanos Car"
car_type = "Tesla"
car_cylinders = 4
car_miles_per_gallon = 0.01
print("I have a car called %s. Its pretty nice." % car_name)

# MORE MATH STUFF
print("Figure this stuff out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)


#  This is a multi-line comment
#  I can type anywhere here


# f(x) = 2x + 3
def f(x):
    print(2 * x + 3)


f(1)


#  Random Numbers
import random  # This should always be on line 1
print(random.randint(0, 100))

# Control Statements
 def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return 'D'
    else:
        return "F"


print(grade_calc(82))


#  Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)

"""
a = 3 # A is set to 3
a == 3 # Is a equal to 3?
"""