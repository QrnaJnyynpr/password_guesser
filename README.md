# Password Guesser
###### Simple tool to guess a password using a dictionary attack, followed by a brute-force attack

**Not intended for use as an actual password cracker. Please consult Wheaton's Rule for further reference.**

This program takes a user-provided plain-text password, then tries to guess it by first running it through a dictionary of the most common passwords. If this fails, it then begins a randomised alphanumeric brute-force attack.

Due to the sheer number of possible alphanumeric combinations, the brute force method is not recommended due to how long it takes. For example, in using this program's character sample, there would be 43,595,145,594 possible combinations just for an 8-digit password.

This program was written purely as a learning exercise, and is not intended for use other than for fun. I used it as a fun little beginner project to learn about using Python to read data from other files, as well as using the 'string' and 'time' libraries.