# Code Leak

The challenge can be run locally using the files in the `Docker` folder.

The files in the `Challenge` folder are given.

PoC in `solve.py`

## Description

We managed to get access to the source code but we got disconnected before being able to download all of it. There has to be a way to get it...

## Solution

If you play around with the application you'll get a few prompts

```
Enter your name: Bob
What would you like to do?
    1. Check balance
    2. Work
    3. Buy hint ($30)
    4. Buy flag ($1337)
    5. Exit
    
>>> [INPUT]
```
1. Shows your current balance
2. Work and get money. You can only work 6 times and each time you get between $5 and $10
3. Prints a useless string for $30
4. Prints the flag if you have $1337
5. Exits

After looking at `main.py`, one can see the lines
```py
if choice == "42":
    secret_debugger()
```
That use the following code
```py
def safe_eval(code):
  tree = compile(code, "<string>", 'exec', flags=ast.PyCF_ONLY_AST)
  for x in ast.walk(tree):
    if type(x) not in (ast.Module, ast.Expr, ast.Attribute, ast.Name, ast.Load):
      return "Invalid operation"

  return eval(code)

def secret_debugger():
  while True:
    try:
      code = input("DEBUG>>> ")
      print(safe_eval(code))
    except Exception as x:
      print(x)
      break
```
`safe_eval` is used to allow only reading variables, with a few more limitations.

Being able to read variables is enough to recreate the code.

First, get some information on `controller`. By reading `controller.__dict__` you get the class variables
```json
{
    "name": "Bob",
    "money": 0,
    "works": 0,
    "encrypted_flag": "ENCRYPTED_FLAG_HERE"
}
```
This can be used to reconstruct the class locally
```py
class Controller:
 def __init__(self):
  self.name = "ok"
  self.money = 9999
  self.works = 1
  self.encrypted_flag = 'ENCRYPTED_FLAG_HERE'

controller = Controller()
```
As you can see, the flag is encrypted and there has to be a way to get it. If you check `Controller.__dict__` (the class this time), you can see there is no decryption method, just the ones used in `main.py`

Making an educated guess, you should run the `buy_flag` method.

Python code can be recreated using data found in the `function.__code__`. You need to create a CodeType object with the data found. You can find the constructor parameters by running `function.__code__.__doc__` locally (Note: in Python 3.10 this will not give the constructor)
```
code(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize,
      flags, codestring, constants, names, varnames, filename, name,
      firstlineno, lnotab[, freevars[, cellvars]])

Create a code object.  Not for the faint of heart.
```
Another way to find the argument order is to check the python repository and find references like this [test](https://github.com/python/cpython/blob/3f2dd0a7c0b1a5112f2164dce78fcfaa0c4b39c7/Lib/test/test_code.py#L223).

The data needed can be found using `controller.buy_flag.__code__.co_ARGNAME`, where ARGNAME is the name of the argument. Exception is `codestring`, that one being `co_code`

After creating the CodeType, you can to create a function from it using `FunctionType(code_object, globals)`

And finally run the function with the controller created earlier as parameter (as `controller.buy_flag()` works like `Controller.buy_flag(controller)` ). This should return a string that can be printed.

## Notes
If the code doesn't work as expected locally (eg. gives the same string with any amount of money) use the same python version as the challenge. The Dockerfile is included as a hint to use Python 3.10 (or what is the latest version if run in the future)

I saw a more elegant solution by [Tzlils](https://github.com/tzlils) ([Solution](https://gist.github.com/tzlils/5779d03919d6873debd1e20baba6c84b)) that recreated the Controller class, skipping the assumption that the constructor is trivial.
