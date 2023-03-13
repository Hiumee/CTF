# Randrevenge & Randrevengerevenge

## Overview

Both can be solved with this solution. The servers sends a timestamp and a few random numbers. The goal is to send back the next number in the sequence.

## Idea

The sequence starts with the very first number after a random seed is set, so we can narrow the search space to seeds that start with it. After getting a few candidates, it is possible to check if the other numbers match by using the provided algorithm. The server doesn't have rate limiting, so we can check just a subset of random seeds and request another batch of numbers if none fit.

## Solution

Step 1: Dump a few pairs of (seed, first_random_number) in a file
```php
<?php

$fp = fopen('data2.csv', 'a')or die("Unable to open file!");

$lines = "";
for($i=0;$i<20796091;$i++){
    mt_srand($i);

    if ($i % 1000000 == 0) {
        // percent complete
        fwrite(STDERR, ($i / 20796091) * 100 . "%\n");
        fwrite($fp, $lines);
        $lines = "";
    }

    $x1 = mt_rand();

    $lines .= "$x1,$i\n";
}
```
Step 2:  Create the file `a.php` that checks if the solution is in the list of candidates
```php
<?php

$number_of_candidates = $argv[1];

$candidates = array();

for ($i = 0; $i < $number_of_candidates; $i++) {
    $candidates[] = intval($argv[$i + 2]);
}


$t = intval($argv[$number_of_candidates + 2]);
$x = intval($argv[$number_of_candidates + 3]);
$hints = array();

// request 5 hints
for ($i = 0; $i < 5; $i++) {
    $hints[] = intval($argv[$number_of_candidates + 4 + $i]);
}

//iterate over candidates
foreach ($candidates as $candidate) {
    mt_srand($candidate);
    mt_rand();
    $current_hint = 0;
    for ($i = 0; $i < 300; $i++) {
        if (($i % 60) == ($t % 60)) {
            $next = mt_rand();
            if ($current_hint < 6 && $next == $hints[$current_hint]) {
                $current_hint++;
            } else {
                continue 2;
            }
        } else {
            mt_rand();
        }
    }
    $next = mt_rand();
    echo "$next";
}
```
Step 3: Run the solving script. It loads the generated csv in a dictionary for lookups and passes possible candidates to `a.php`
```python
# Make a post request to the server with the data "next=2"
import os
import requests
import csv

url = "http://52.59.124.14:10019/"

d = {}

i = 0

with open('data.csv') as csvfile:

    spamreader = csv.reader(csvfile)

    for row in spamreader:
        i+=1
        # check if in dict
        if i == 20796091:
            break
        if row[0] in d:
            d[row[0]].append(row[1])
        else:
            d[row[0]] = [row[1]]
            z = row[0]

print(f"Loaded {i} lines")

while True:
    r = requests.post(url)
    data = r.text.split("\n")

    data[0] # time
    leak = data[1]

    if leak in d:
        number = os.popen(f"php a.php {len(d[leak])} {' '.join(d[leak])} {' '.join(data[:-2])}").read()

        print(f"Number: {number}")

        cookies = r.cookies

        r = requests.post(url+"submit", data={"next": number}, cookies=cookies)
        print(r.text)
        if "ENO" in r.text:
            exit()
```

## Flags
`ENO{M4sT3r_0f_R4nd0n0m1c5}` - randrevenge
`ENO{PHD_1N_TrU3_R4nd0n0m1c5_516189}` - randrevengerevenge