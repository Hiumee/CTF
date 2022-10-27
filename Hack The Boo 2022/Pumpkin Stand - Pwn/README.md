# Pumpkin Stand

## Description

This time of the year, we host our big festival and the one who craves the pumpkin faster and make it as scary as possible, gets an amazing prize! Be fast and try to crave this hard pumpkin!

## Solution

We are given an IP address and an executable file that is running on it.
Checking the file in Ghidra we can see a few checks that need to be passed for the program to print the flag.

While manually messing around with the challenge prompt I found out that sending 4 then 4 again will print the flag sometimes but not always.

We have 2 input prompts. I'll call them INPUT_1 and INPUT_2 from now on.

Analyzing the Ghidra decompilation, to get to the print file method we have to pass the following checks:
- INPUT_2 > 0
- pumpcoins > -1 `pumpcoins = pumpcoins - INPUT_2 * (short)*(int *)((long)&values + (long)INPUT1 * 4);`
- INPUT_1 != 1
- pumpcoins > 9998

`values` has the following bytes `00 00 00 00 39 05 00 00 39 05` - the last `39 05` is overflow to `pumpcoins`. Due to the overflow, sending 2 will use the current sum.

We can underflow the `pumpcoins` number by paying 1337 (the current sum) repeatedly by sending 2 then 40 (or any other number such that -1337\*(N-1) will underflow). Now we will have 13393 pumpcoins and pass all the checks.

`HTB{1nt3g3R_0v3rfl0w_101_0r_0v3R_9000!}`