# Trick or Breach

## Description

Our company has been working on a secret project for almost a year. None knows about the subject, although rumor is that it is about an old Halloween legend where an old witch in the woods invented a potion to bring pumpkins to life, but in a more up-to-date approach. Unfortunately, we learned that malicious actors accessed our network in a massive cyber attack. Our security team found that the hack had occurred when a group of children came into the office's security external room for trick or treat. One of the children was found to be a paid actor and managed to insert a USB into one of the security personnel's computers, which allowed the hackers to gain access to the company's systems. We only have a network capture during the time of the incident. Can you find out if they stole the secret project?

## Solution

A pcap file is given. Analyzing it, it has only a lot of DNS requests like `4b01021400140008080800a52c4755d09a438a5b0100006a03.pumpkincorp.com`
I wrote a script to get the urls and write the hex-encoded data to a file
```python
data = open("capture.pcap",'rb').read()

found = []
while (p := data.find(b"pumpkincorp")) != -1:
    found.append(data[p-51:p-1])
    data = data[p+1:]

found = found[:-2] # Last 2 are not from DNS requests

d = b""
i = 0
for x in found:
    i += 1
    if i % 2 == 0:
        continue # Skip response
    try:
        d += (bytes.fromhex(x.decode()))
    except Exception as e:
        pass

open("data",'wb').write(d)
```

Checked the file type of the result and I got 
```
$ file data
data: Microsoft Excel 2007+
```

Seeing this, I assumed there are multiple files inside and used binwalk to extract them. Checking the output files, in `sharedStrings.xml`, I found the flag.
`HTB{M4g1c_c4nn0t_pr3v3nt_d4t4_br34ch}`
