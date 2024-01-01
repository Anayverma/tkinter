# Puzzle: The Secret Code

# You've stumbled upon a mysterious note with a series of numbers. It appears to be a secret code. After some investigation, you notice a pattern:

# Each number in the code is the sum of the previous two numbers.
# The code starts with two initial numbers: 0 and 1.
# Your task is to write a Python program to decode the secret message hidden in the code. Create a function called decode_secret_code that takes an integer n as input and returns the nth number in the secret code.

# Here's an example to illustrate the pattern:

# For n = 0, the output should be 0.
# For n = 1, the output should be 1.
# For n = 2, the output should be 1 (0 + 1).
# For n = 3, the output should be 2 (1 + 1).
# For n = 4, the output should be 3 (1 + 2).
# And so on.
# Your task is to implement the decode_secret_code function and use it to find the secret message for a given n. Good luck!
def decode_secret_code(n):
    if n<0:
        return -1
    elif n==0 or n==1:
        return n
    else:
        return decode_secret_code(n-1)+decode_secret_code(n-2)

def puzzle():
    n=int(input("Enter value of n => "))
    print(f"For the Goiven value of n = {n} output is:",decode_secret_code(n))
# __int__=puzzle()  or
puzzle()
