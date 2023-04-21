#Write a program in Python to reverse a word
word=input()
reverse=""
for i in word:
    reverse=i+reverse
print(reverse)