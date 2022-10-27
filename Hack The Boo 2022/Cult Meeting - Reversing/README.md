# Cult Meeting

## Description

After months of research, you're ready to attempt to infiltrate the meeting of a shadowy cult. Unfortunately, it looks like they've changed their password!

## Solution

A server and the executable running on are provided. Running the file locally I get
```
You knock on the door and a panel slides back
|/👁️ 👁️ \|   A hooded figure looks out at you
"What is the password for this week's meeting?" Password
   \/
|/👁️ 👁️ \| "That's not our password - call the guards!"
```
Where "Password" is the user input. I suspect there is a string comparison for the password and run the program again using ltrace to see the library calls `ltrace ./meeting`
The result has line `strcmp("Password", "sup3r_s3cr3t_p455w0rd_f0r_u!")`

Checked locally that the password is the only thing needed and sent it to the server. After the password is sent, the server gives a shell. Running `cat flag.txt` now will get the flag

`HTB{1nf1ltr4t1ng_4_cul7_0f_str1ng5}`