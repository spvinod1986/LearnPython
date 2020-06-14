from timeit import timeit

# handling exceptions
try:
    numbers = [1, 2]
    print(numbers[3])
except IndexError as ex:
    print("Do not try to access number not available in the list")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("The number cannot be zero")
except (ValueError, SyntaxError):
    print("This may be due to value error or syntax error")
else:  # this else clause will be executed if there are no exceptions. Similar to for else loop
    print("No exceptions were thrown")
finally:
    print("This is final block which will be executed always.")

# with
try:
    with open("Readme.md") as file:
        print("File opened")
except:
    print("This will hit for any exception")

# throwing exceptions


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
# better approach than throwing exceptions

code1 = """
def calculate_xfactor_bad_option(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age


try:
    calculate_xfactor_bad_option(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor_better_option(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor_better_option(-1)
if xfactor == None:
    pass
"""

print("First Code = ", timeit(code1, number=10000))
print("Second Code = ", timeit(code2, number=10000))
