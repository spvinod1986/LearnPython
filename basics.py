# BASICS
# int variable
test_count = 1000
# float variable
test_rating = 4.99
# bool variable
is_available = True
# string variable
my_name = "David"
# string variable multiple lines
my_comments = """
This is 
my comment about
you.
"""
# multiple variable declaration
x, y, z = 1, 2, 3
x = y = z = 5
# you can also change type of variable
x = "ChangedtoString"
# type can specified using type annotation
age: int = 20
# integer is immutable
a = 1
print(id(a))
a = a + 1
print(id(a))
# list is mutable
b = [1, 2, 3]
print(id(b))
b.append(4)
print(id(b))
# string manipulation
doing_what = "I am learning python"
print(len(doing_what))
doing_that = 'with single quote'
print(doing_that)
doing_escape = "This quote \"God is Great\" is a very good quote"
print(doing_escape)
print(doing_what[0])
print(doing_what[-1])
print(doing_what[0:4])
print(doing_what[:4])
print(doing_what[0:])
print(doing_what[:])
print(doing_what.upper())
print(doing_what.lower())
print(doing_what.title())
print(doing_what.strip())
print(doing_what.find("python"))
print("python" in doing_what)
# formatted strings
first = "David"
last = "Henry"
full = f"{first} {last}"
print(full)
# numbers
xxx = 10
print(bin(xxx))
print(hex(xxx))
# binary number
xxx = 0b10
# hexadecimal number
xxx = 0x12c
# complex number
yyy = 1 + 2j
print(yyy)
# arithmetic operators
aaa = 10 + 5
aaa = 10 - 5
aaa = 10 * 5
aaa = 10 / 3
print(aaa)
aaa = 10 // 3
print(aaa)
aaa = 10 % 3
aaa = 10 ** 3
aaa += 1
# number functions
PI = -3.14
print(round(PI))
print(abs(PI))
# type conversions
x = "1"
print(int(x))
print(float(x))
print(bool(x))
print(str(x))
# conditional statements
age = 18
if age >= 18:
    print("adult")
    print("second adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
print("All done")
# logical operators
name = ""
if not name:
    print("Name is empty")
age = 22
if age >= 18 and age < 65:
    print("Eligible")
# chaining comparison operators
if 18 <= age < 65:
    print("Eligible")
# Ternary operator
message = "Eligible" if age < 18 else "Not Eligible"
print(message)
# loops
for x in "python":
    print(x)
for x in range(5):
    print(x)
names = ["John", "David"]
for name in names:
    if name.startswith("a"):
        print("Found")
        break
else:
    print("Not Found")
guess = 0
answer = 5
while answer != guess:
    guess = guess + 1
    print(guess)
# functions


def increment(number, by):
    return number + by


def increment_and_return_tuple(number, by=2):
    return (number, number + by)


def increment_with_datatype(number: int, by: int) -> int:
    return number + by


def add_tuples(*list):
    total = 0
    for number in list:
        total = total + number
    return total


def save_user(**user):
    print(user)


print(increment(4, 4))
print(increment_and_return_tuple(4))
print(increment_with_datatype(4, 4))
print(add_tuples(1, 2, 3, 4))
save_user(id=1, name="David")

global_message = "a"


def greet():
    global global_message
    global_message = "b"


greet()
print(global_message)


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
