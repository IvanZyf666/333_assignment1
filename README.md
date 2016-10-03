# Group uc05


## PART 1

Instructions for using part 1:
* navigate to directory containing ctext1hexdump.txt, part1.py
* in the terminal enter 'python3 part1.py'
* a plaintext file named 'plaintext1.txt' will be generated containing the plaintext of ciphertext1.


Explanation: we determined the gaps between high frequency of bytes used in the ciphertext and found out that there was a significantly higher spike in word frequency every 7th byte. We thus deduce that the key length is 7. 

We then processed every 7th character since the key length is 7 and that would mean every 7th character would be encrypted using the same key value. Once we have this frequency analysis of every 7th byte, we assign the highest occuring byte to be equal to the plain ascii value of a space, '0x20'. We do this to find our key. 

We then use this key to decrypt the ciphertext to produce 'plaintext1.txt'

We automated finding the key by assuming that the highest occuring byte will be the space ascii character. 


## Part 2

Instructions for using part 2:
* navigate to directory containing ctext2hexdump.txt, part2.py (same dir as in part1)
* in the terminal enter 'python3 part2.py'
* a binary file named 'plaintext2' will be generated containing the plaintext of ciphertext2.

Similarly to Part 1 approach, we found the key length to be 23.

We then processed every 23rd character since the key length is 23 and that would mean every 23rd character would be encrypted using the same key value. 

However, in addition to Part 1 approach, we analyzed byte frequency of various differrent file types and determined that '0x00' is the most frequent byte for most non-text file

Once we have this frequency analysis of every 23rd byte, we assign the highest occuring byte to be equal to '0x00'. We do this to find our key. 

We then use this key to decrypt the ciphertext and produce resulting file 'plaintext2'

We ensured that the key was correct by trying to decrypt gven file with the right key. The process of finding the key is automated, but its verification is not.

## Part 3 Discussion