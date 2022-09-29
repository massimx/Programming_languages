import re

print("Enter the line")
words = str(input())

print("Enter the letter you want to find:")
letter = str(input())
count = 0

for word in words.split(" "):
    if word.strip()[0] == letter:
        count += 1

print(f"Number of words beginning with the letter '{letter}': ", count)
