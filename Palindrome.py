str = input ("Enter the word: ")
l = len(str)
p = l - 1
index = 0
while index < p:
    if str[index]== str [p]:
        index = index + 1
        p = p - 1
        print("The entered word is a palindrome")
    else:
        print ("The entered word is not a palindrome")
        break

