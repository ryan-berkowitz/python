word = input("Enter a word: ")
i=0
g=0
while i < len(word):
    f = -i-1
    if word[i] == word[f]:
        i = i+1
    else:
        g=1
        i = len(word)+1

if g == 0:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")