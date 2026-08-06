# Count the Number of Vowels in a String

user_input = input("Enter a string: ")

vowel_count = 0

for character in user_input.lower():
    if character in "aeiou":
        vowel_count += 1

print("The number of vowels in the string is:", vowel_count)
