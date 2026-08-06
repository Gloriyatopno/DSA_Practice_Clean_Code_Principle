#Count Vowels
Str=input("Enter a String:")
count=0
for i in Str.lower():
    if i in "aeiou":
        count+=1
print("The number of vowels in the string is:", count)