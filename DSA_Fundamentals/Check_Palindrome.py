#Check Palindrome
Str=input("Enter a String:")
if Str.lower()==Str.lower()[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")