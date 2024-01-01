# Puzzle: The Jumping Characters

# You've discovered a strange message encoded using jumping characters. The message consists of a string of characters, and the jumping characters follow a specific pattern:

# Starting from the first character, you jump forward by a certain number of positions to find the next character in the message.
# The jumping distance remains constant throughout the message.
# Your task is to write a Python program to decode the secret message hidden in the jumping characters. Create a function called decode_jumping_characters that takes a string message and an integer jump as inputs and returns the decoded message.

# Here's an example to illustrate the pattern:

# For the message "H!e@l#l$o%" and jump = 2, the decoded message should be "Hello" because you jump two positions to decode each character.
# Your task is to implement the decode_jumping_characters function and use it to find the secret message for a given input message and jumping distance. Good luck!
def decode_jumping_characters(s):
    st=""
    for i in range(0,len(s),2):
        st+=s[i]
    return st

def puzzle():
    s=(input("Enter String s => "))
    print(f"For the Given value of s = {s} output is:",decode_jumping_characters(s))
# __int__=puzzle()  or
puzzle()
