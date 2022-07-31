# Adding in Parts

The file in the `Challenge` folder is given
PoC in `solve.py`

## Description
I stored my data in multiple files for extra security. But they all got corrupted somehow.

## Solution
After extracting the provided zip archive, there are 22 zip files, named 0 1 ... 21.

Attempting to extract any of those should throw an error because the CRC is incorrect. If you fix/ignore this, you get files that make up the string `eRr0r_1n_c0mpresS1oN00`. As many found out, this is not the flag.

Fixing the CRC error doesn't work. This might lead someone to think that the 'corruption' isn't at CRC but somewhere else. If the CRC correct, then the file data is wrong.

CRC stands for Cyclic Redundancy Check and is a checksum algorithm ("Adding" from the title was a hint in this direction). This means that we can get the original data by computing all the CRC32 values for the character set of the flag. As each file has only one character this can be done without collisions.

After getting the CRC - character mapping, the flag is aquired by joining the characters together in the order given by the file names.

## Note
`eRr0r_1n_c0mpresS1oN00` was not meant as a red herring, just as a clue that it is not that easy.
