# Palindrome
# Create a function is_palindrome(word) that returns True if a given word is a palindrome (reads the same backward)
# and False otherwise

def is_palidrome(word):
    return word==word[::-1]
word=input("Enter a word: ")
answer=is_palidrome(word)
if answer:
    print(True)
else:
    print(False)
