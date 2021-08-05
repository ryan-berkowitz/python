word = input("Enter a word: ")
i = 0
g = 0
while i <= len(word)//2:
    f = -i-1
    if word[i] == word[f]:
        i = i+1
    else:
        g = 1
        i = len(word)+1

if g == 0:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")

#Andrew's solution
word = input("Enter a word: ")

m = [x for i, x in enumerate(word[:len(word)//2]) if word[i] != word[-i - 1]]

if len(m) == 0:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")
