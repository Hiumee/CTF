# Remote uses Python 3.10, use 3.10 on local. Given as hint by the Dockerfile's `python:latest`

import random
# random import is for dependencies from the buy_flag function

from types import CodeType, FunctionType

# read using `controller.__dict__`
# edit the money amount
class Controller:
 def __init__(self):
  self.name = "ok"
  self.money = 9999
  self.works = 1
  self.encrypted_flag = 'ENCRYPTED_FLAG_HERE'

# `function_name.__code__.__doc__` for info. Python 3.10 gives less info
# read using `controller.buy_flag.__code__.co_` + arg name
argcount = 1
posonlyargcount = 0
kwonlyargcount = 0
nlocals = 5
stacksize = 8
flags = 67
# codestring = co_code
codestring = b'|\x00j\x00d\x01k\x00r\x0b|\x00j\x01\x9b\x00d\x02\x9d\x02S\x00g\x00}\x01|\x00j\x02D\x00]\t}\x02|\x01\xa0\x03t\x04|\x02\x83\x01\xa1\x01\x01\x00q\x10t\x05\xa0\x06d\x03\xa1\x01\x01\x00t\x07t\x08|\x01\x83\x01\x83\x01D\x00]\x0e}\x03|\x01|\x03\x05\x00\x19\x00t\x05\xa0\td\x04d\x05\xa1\x02N\x00\x03\x00<\x00q%g\x00}\x04|\x01D\x00]\t}\x02|\x04\xa0\x03t\n|\x02\x83\x01\xa1\x01\x01\x00q8d\x06\xa0\x0b|\x04\xa1\x01S\x00'
consts = (None, 1337, ' does not have enough money', 133773211629381620483, 0, 256, '')
names = ('money', 'name', 'encrypted_flag', 'append', 'ord', 'random', 'seed', 'range', 'len', 'randint', 'chr', 'join')
varnames = ('self', 'flag', 'x', 'i', 'flag_ascii')
filename = "anything"
name = "anything"
firstlineno = 0 # anything
lnotab = b'\x00\x01\n\x01\x0c\x02\x04\x02\n\x01\x10\x02\n\x02\x10\x01\x1a\x02\x04\x02\x08\x01\x10\x02'
freevars = ()
cellvars = ()

# create code object
code = CodeType(
        argcount,             #   integer
        posonlyargcount,      #   integer
        kwonlyargcount,       #   integer
        nlocals,              #   integer
        stacksize,            #   integer
        flags,                #   integer
        codestring,           #   bytes
        consts,               #   tuple
        names,                #   tuple
        varnames,             #   tuple
        filename,             #   string
        name,                 #   string
        firstlineno,          #   integer
        lnotab,               #   bytes
        freevars,             #   tuple
        cellvars              #   tuple
        )

# create function object
# add things in the __globals__ dictionary until the program stops complaining about undefined variables
buy_flag = FunctionType(code, {'random': random})

# call function and print result
cont = Controller()
print(buy_flag(cont))
