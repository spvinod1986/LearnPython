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
- Range object (eg: range(0, 1000)) does not return list instead return a range object with minimum memory foot print and the object can be enumerated for the range.
- In python we have concept of for else and while else. The else block will hit only if the for and while loop gets completed without hitting a break statement.
- If an argument to function is decorated with * then the argument is considered as tuple and if it is decorated with ** then the argument is considered as dictionary of key value pair(similar to javascript object).
- Python has 2 kind of variables. 1) Local variables with function scope and 2) Global variables with file scope. Python do not have block level scope similar to C# or Java, hence if a variable is declared inside a if block, then the variable should still be accessible within the function.
