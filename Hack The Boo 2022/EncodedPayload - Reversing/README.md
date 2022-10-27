# EncodedPayload

## Description

Buried in your basement you've discovered an ancient tome. The pages are full of what look like warnings, but luckily you can't read the language! What will happen if you invoke the ancient spells here?

## Solution

We are given just an executable file. Running it with strace will show an attempt to print the flag

`write(1, "HTB{PLz_strace_M333}\n", 21)  = -1 EPIPE (Broken pipe)`