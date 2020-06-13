# Learn Python

## Introduction
- Python is the fastest growing and world's famous programming language (as of 2020).
- Helps to solve complex problems in less time and fewer lines of code.
- Multi purpose language, High Level (No memory management required), Cross platform, Huge community and ecosystem.
- 2 versions of Python - 1) Python 2 is legacy version 2) Python 3 is the future.
- Famous Editors - VSCode, Atom, Sublime. Famous IDE - PyCharm (Jetbrains product).
- IDE provides following which may or may not be available in Editors. Linting: Analysing code for potential errors Debugging: Finding and fixing errors. AutoCompletion: Type code faster. CodeFormatting: Makes code clean and readable. UnitTesting: To test the code. CodeSnippets: Reusable code blocks.
- Famous Linter for Python: PyLint.
- Python community has bunch of documents called PEPs: Python Enhancement Proposals. Each PEP has a number and title and is available on Python.Org website. PEP8 is popular among python developers which is the style guide for Python code. This document details bunch of rules for formatting Python code. Various tools and extensions available for formatting Python code to PEP8. Famous Tool: AutoPEP8.
- Default implementation of Python is CPython. Reason it is called CPython is becuase it is built using C language. Other implementations: Jython(written in Java), IronPython(written in C#) and PyPy(subset of python).
- Python code is executed similar to how Java or C# code is executed. Python code is compiled by default Cpython implementation to Python Bytecode. This Python Bytecode is then converted to machine code by Python virtual machine during runtime. Where as in case of Jython, IronPython implementation, the code is compiled to JavaBytecode(Java) or IL(C#) which then converted to machine code by JVM(Java) or JIT(C#).

## Basics
- Python is object oriented language.
- Static languages: C++, C#, Java. Dynamic Languages: Javascript, Ruby, Python.
- In Dynamic languages, the type of a variable is determined during runtime.
- Integers, string, float, bool are immutable. if value of int variable is changed, new value is stored in new address.
- Lists are mutable. Adding new objects to list will not copy/create new memory.
- backslash can be used as escape character similar to other programming language.
- Python do not have increment or decrement operators like in other programming languages.
- Python do not have concept of constants like in other programming languages.
- Python is strongly typed and does not do any implicit type conversion.
- Python has only 2 types of loops: for/while.
- Range object (eg: range(0, 1000)) does not return list instead return a range object with minimum memory foot print and the object can be enumerated for the range min and max. It is an iterable object.
- In python we have concept of for else and while else. The else block will hit only if the for and while loop gets completed without hitting a break statement.
- If an argument to function is decorated with * then the argument is considered as tuple and if it is decorated with ** then the argument is considered as dictionary of key value pair(similar to javascript object).
- Python has 2 kind of variables. 1) Local variables with function scope and 2) Global variables with file scope. Python do not have block level scope similar to C# or Java, hence if a variable is declared inside a if block, then the variable should still be accessible within the function.
- Falsy values in Python: 0, ", [], none (similar to null in other programming languages)

## Data Structures
- In Python, every object in a list can be of different type. We can also combine list of strings to list of numbers or booleans etc.
- Lambda functions or anonymous functions are supported in Python similar to other programming languages like C#, Java
- Comprehensions is a new concept in Python which is not available in other programming languages. Comprehensions enable to write cleaner code and it is also more performant.
- Stacks and Queues can be implemented using list. Using list for queue may be not performant as all the items in the memory need to be moved after removal of first item. Deque module is performant.
- Python supports tuple which is just read only list which contains sequence of objects. Tuples are immutable. That is the reason for no add or remove methods in tuple object. Tuples will be useful when you are dealing with sequence of objects and you dont want to accidentally modify the original sequence. Common braces are used for tuple.
- Large sequence of numbers can be dealt using more efficient data structure in python called Array. They take less memory and perform little bit faster. If you are running a query in list and you see performance problem then you can use Array. Arrays are available in array module.
- Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character. https://docs.python.org/3/library/array.html.
- Python also support Set which is an unordered collection of unique items with no duplicates. Curly braces are used for Set. Set supports rich set of operations like union, intersection, difference etc. Set does not support retrieval of elements using index. If you want to index then list is best choice.
- Python also supports dictionary which is just a collection of key value pairs. Only immutable types can be used as keys. Value have no restrictions.
- If you want to work with infinite stream of data, then we may not need to store all those values in memory. It is memory inefficient. Python provides generator objects for that purpose. You can use generator expressions to create generator objects. They are iterable and in each iteration they generate or create new value. Unlike lists they don't store these values in memory. You cannot find length of these generator objects.
- Unpacking operator can be used to unpack any iterables

## Exceptions
- Python program will crash if exceptions are not handled
- Exceptions can be handled by using try, except, finally block
- Python also has concept of try, except, else, finally where the else block will be called if try completes without any exception.
- Python provides "with" statement which can be used to automatically release external resources. The "with" statement is similar to "using" statement in other programming languages. Any object that supports context management protocol (or has __enter__ and __exit__ magic methods) then those objects can be used with "with" statement.
- Python 3 built in exceptions can be found in python website: https://docs.python.org/3/library/exceptions.html
- You can throw exception using "raise" keyword and you can define your own exception types as well.

## Classes
- Class is blue print for creating new objects.
- Object is the instance of a class.
- Naming convention for variables and functions - all lower case letters and seperate multiple words using underscore.
- Naming convention for classes - Pascal naming convention. No use of underscore to seperate multiple words.
- All functions in a class should have atleast one parameter and by convention it is called "self". "self" is the reference to current object.
- __init__ is the magic method used to create constructor.
- Objects in phyton are dynamic similar to javascript.
- There are 2 kinds of attributes. 1) Class Attributes 2) Instance Attributes.
- Instance attributes are the ones defined in constructor. They belong to instance or object of the class. Different objects can have different value for these attributes.
- Class attributes are the ones defined in class level and they are shared or same between all instances of the class. We can read this through class reference or object reference.
- There are 2 kinds of methods. 1) Class Methods 2) Instance Methods.
- Instance Methods can be called only using instance of a class or object.
- Class Method can be called directly from the class. These methods sometimes serves as factory method.
- Magic Methods: These methods have 2 underscores in beginning and end of the name and these are called automatically by python interpreter as and when required. You can check the list of magic methods in this website https://rszalski.github.io/magicmethods/. You can override these magic methods as required. __int__ is the magic method called when you try create instance of class or otherwise called constructor. __str__ is the magic method called when you try convert object to string.
- By default, equality operator in Python compares addresses or references between 2 objects.
- An iterator object is an object that walks a container and gets one item at a time.
- To make a attribute private or inaccessible from outside class, you need to prefix the attribute with double underscore __. Please note that you can still access this attribute from outside but this is just a convention to make it private or make it little bit harder for accessing it from outside. Python do not have concept of private members like in other programming languages like C#, Java.
- Object is the base class for all classes in python.
- Python supports multi level inheritance. It means a class can inherit from one class which can inherit from another class.
- Python supports multiple inheritance which means a class can have multiple base classes.
- Python provides Abstract Base Class which can declare common behavior method and contract for derived class to implement. 
- We can implement polymorphism without even using abstract class or contract in Python. This is called duck typing. If it walks like a duck and quacks like a duck then it is a duck. No need of any contract or base class to prove that it is a duck. Because Python is a dynamically typed language.
- If you have classes that have only data and no method or behavior then you can use namedtuple instead of class. They are called data classes. The equality operator on data classes check for equal values in data instead of memory address or references. The namedtuples are immutable.

## Modules
- You can split code to different files and each file is called a module. Module is a logically related objects like functions, classes, variables etc.
- Compiled version of python files or modules are called pycache. These pycache files end with .pyc and will be placed under __pycache__ folder. Python compiles these modules to speed up the process of module loading. If compiled version is available, python will skip compilation step and use the compiled files. Python compares the date time of source file and cached compile file and if the source file datetime is lesser than compile file then it will use compile file. The compiled files contains python byte code.
- Predefined directories where python will look at to find the module can be found using sys.path.
- A package is a container for one or more modules. Package is mapped to a directory and module is mapped to a file.
- dir() is powerfukl built in function. With this function we can get list of attributes and methods defined in an object.
- In python, you can execute module as script similar to immediately invoked function expressions in javascript.

## Python Standard Library
- Python comes with comprehensive packages and libraries which helps in building applications.
- Paths/Directories: https://docs.python.org/3.4/library/pathlib.html
- Path class from pathlib is the base class for working with paths. PosixPath is for mac/linux and WindowsPath is for windows.
- Path library is useful for building path, create/remove/rename directories or files, read from file or write to file etc.
- ZipFile class in zipfile module helps with methods to work with zip files(write, create)
- csv module provides writer method to write to csv file and reader method to read all rows.
- json module provides dumps methods to convert object to json and loads method to convert json to object.
- time and datetime module provides with methods to work with timestamps and datetime respectively. timedelta module provides with methods to work with duration or time difference between 2 dates.
- random module provides methods to generate random numbers.

## Python Package Index
- Python Standard Library is comprehensive but it does not have everything that we need. Sometimes we may need features that are not implemented in Python Standard library. Pypi or Python Package Index is like npm(javascript) or nuget(microsoft) repository. It is repository of Python packages.
- To install package from Pypi we should use a tool called pip(windows) or pip3(mac).
- pip3 install xyz ~= 1.1.0
- pip3 install xyz == 1.1.*
- pip3 install xyz == 1.*
- pip3 unisntall xyz
- Virtual Environments: Pip installs packages globally which can be shared between projects. But different projects may have different versions of dependenciies. In that case we need to create isolated virtual environments for each application and install these dependencies inside those virtual isolated environments.
- Pipenv: It is a tool which combines Pip and Virtual environment in to a single tool called Pipenv. It is a dependency manager for Python projects. It is equivalent to npm(javascript).
- pipenv shell command will activate virtual environment for a project. To deactivate the virtual environment , type exit.
- In your project, run pipenv install xyz
- Pipenv will install virtual environment packages in a shared local folder outside the project to maintain the size of the project. This path can be found using the command pipenv --venv.
- When you install a package using pipenv, 2 files will get automatically created. 1) Pipfile and 2) Pipfile.lock. These 2 projects are used to keep track of dependencies of our project and their versions.
- PipFile includes 4 sections. 1) source is the address of the package repository from which packages are downloaded from. 2) dev-packages are the packages specific for development like automated testing. 3) packages which the application depend on. 4) requires specifies the version of python we need to run this application. If you don't specify version number , then pipfile will list the package with * version which means latest version.
- PipFile.lock is the Json file which lists the dependencies of the application and their exact version. This helps in lift and shift scenario where you can take your application and put in another machine and the exact version of dependencies will be installed there. You can just move the application and run command "pipenv install" which will just look at dependencies in pipfile and install exact version of dependencies. Some case the packages in pipfile will specify latest version for packages with * if you do not specify the exact version during installation. In those cases if you want same version number in all machines then you can use command pipenv install --ignore-pipfile to ignore the pipfile and consider exact version in pipfile.lock.
- We can use the command pipenv graph to view the list of all installed dependencies
