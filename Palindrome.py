str = input ("Enter the word: ")
c = len(str)
p = c - 1
index = 0
while index < p:
    if str[index]== str [p]:
        index = index + 1
        p = p - 1
        print("The entered word is a palindrome")
    else:
        print ("The entered word is not a palindrome")
        break

