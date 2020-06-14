from collections import deque
from array import array
from sys import getsizeof
from pprint import pprint

# lists
letters = ["a", "b", "c", "d", "e"]
two_dimensional_matrix_lists = [[0, 1], [2, 3], [4, 5]]
list_of_zeros = [0] * 10
print(list_of_zeros)
combined = letters + list_of_zeros
print(combined)
print(list(range(10, 15)))
print(list("Hello World"))
print(len(list("Hello World")))
print(letters[0])
print(letters[-1])
letters[0] = "A"
print(letters[0:3])
print(letters[::2])  # splicing a specific element off the list - like odd/even
print(letters[::-1])  # reverse order
# list unpacking
numbers = ["1", "2", "3", "4", "5"]
first, *other, last = numbers
print(first)
print(other)
print(last)
for number in numbers:
    print(number)
# You can also get index
for index, number in enumerate(numbers):
    print(index, number)
# adding/removing items from list
numbers.append("6")
print(numbers)
numbers.insert(0, "0")
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(0)
print(numbers)
numbers.remove("5")
print(numbers)
del numbers[0:2]
print(numbers)
numbers.clear()
print(numbers)
# finding items
letters = ["a", "b", "c", "b"]
print(letters.index("b"))
if "b" in letters:
    print("Found")
print(letters.count("b"))
# sorting lists
numbers = [4, 76, 450, 123, 8, 3]
# will return new sorted list without modifying existing lists
print(sorted(numbers))
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# sorting non primitive types or complex objects we need to create a function that python can use to sort the lists
items = [
    ("Item1", 10.00),
    ("Item2", 1.00),
    ("Item3", 16.00),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# anonymous or lambda function
items = [
    ("Item1", 10.00),
    ("Item2", 1.00),
    ("Item3", 16.00),
]

items.sort(key=lambda item: item[1])
print(items)
# map function
# to create new list of item prices
item_prices = list(map(lambda item: item[1], items))
print(item_prices)
# filter function
# to create new list if items which meets some condition
item_more_than_eight_dollars = list(filter(lambda item: item[1] >= 8, items))
print(item_more_than_eight_dollars)
# comprehensions
item_prices_comprehension = [item[1] for item in items]
print(item_prices_comprehension)
item_more_than_eight_dollars_with_comprehension = [
    item for item in items if item[1] >= 8]
print(item_more_than_eight_dollars_with_comprehension)
# zip function
# to combine 2 lists in to single list of tuples
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))
# stacks
session = [1, 2, 3]
session.append(4)
last = session.pop()
print(last)
print(session)
# queues
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
first = queue.popleft()
print(first)
print(queue)
# tuples
point = (1, 2) + (3, 4)
print(type(point))
print(point)
point = (1, 2) * 4
print(point)
point = tuple("Hello World")  # convert string to tuple
print(point)
print(point[0])
x, y, z, *other = point
print(x)
print(other)
# swapping variables
x = 10
y = 11
x, y = y, x  # this is tuple unpacking
print(x)
print(y)
# arrays
numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(4, 5)
print(numbers)
# sets
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4]
firstset = set(numbers)
secondset = {2, 3, 4, 4}  # duplicate will be automatically removed
print(firstset)
print(secondset)
print(firstset | secondset)  # union of 2 sets
print(firstset & secondset)  # intersection of 2 sets
print(firstset - secondset)  # difference between 2 sets
print(firstset ^ secondset)  # Either in first or second but not both
if 1 in firstset:  # check for existence of an item
    print("Yes")
# dictionaries
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 5
print(point["x"])
if "a" in point:
    print(point["a"])
print(point.get("a"))  # this returns none
print(point.get("a", 0))
del point["x"]
print(point.get("x"))
for key, value in point.items():
    print(key, value)
# dictionary comprehensions
values = {x * 2 for x in range(5)}  # set comprehension
keyvalues = {x: x * 2 for x in range(5)}  # dictionary comprehension
lists = [x * 2 for x in range(5)]  # list comprehension
# generator objects and expressions
generator_objects = (x * 2 for x in range(5))
print("gen for range 5:", getsizeof(generator_objects))
generator_objects = (x * 2 for x in range(100000))
print("gen for range 100000:", getsizeof(generator_objects))
lists = [x * 2 for x in range(100000)]
print("gen for lists 100000:", getsizeof(lists))
# unpacking operator
numbers = [1, 2, 3]
print(*numbers)
values = [*range(5), *"Hello"]
print(values)
first = [1, 2, 3]
second = [4, 5]
values = [*first, *second]
print(values)
firstdict = {"x": 1}
seconddict = {"y": 10, "x": 15}
combined = {**firstdict, **seconddict, "z": 1}
print(combined)
# find most repeated character
sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1], reverse=True)
print(char_frequency_sorted[0])
