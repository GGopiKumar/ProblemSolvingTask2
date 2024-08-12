
'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.1 : Write a Python program to calculate the total number of Vowels and 
Count of each Individual vowel A,E,L,O,U in the string "Guvi Geeks Network Private Limited" ?

Logic : Using For Loop iterating the given string and with if comdition counting the vowels and 
also included Logic to Count the Capital Letter Vowels if any 
'''
givenString = "Guvi Geeks Network Private Limited"
vowel_count = 0

# iterate over the string
for data in givenString:
    if data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        vowel_count = vowel_count + 1
    if data == 'A' or data == 'E' or data == 'I' or data == 'O' or data == 'U':
        vowel_count = vowel_count + 1    


# print the total vowels in a string
print("Number of vowels in the string : ", vowel_count)

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.2 : Create a Pyramid of Numbers from 1 to 20 using For loop?

Logic : using nested for loop created the Pyramid
'''
for a in range(0, 21):
    # This For Loop for creating spaces
    for b in range(20 -a):
        print(" ", end="")
    
    # This For Loop for Print numbers,increasing order
    for c in range(1, a +1 ):
        print(c, end=" ")
    
    # This For Loop for Moving to  next line for next row
    print()

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.3 : Write a program that takes a string and returns a new string with all the vowels removed

Logic : Using For Loop iterating the given string and with if condition on the vowels replacing in the string 
'''
takeStringInput = input("Enter a string : ")

# iterate over the string
for data in takeStringInput:
    if data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        takeStringInput=takeStringInput.replace(data,"")
    if data == 'A' or data == 'E' or data == 'I' or data == 'O' or data == 'U':
        takeStringInput=takeStringInput.replace(data,"")   
        

print("Removed the Vowels in your String and the Output String Value is  " + takeStringInput)

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.4 : Write a program that takes a string and returns the number of unique characters in it

Logic : Using For Loop iterating the given string and with if condition if duplicate character breaking the Loop 
anf from inner loop counting the unique character
'''

takeStringInputTwo = input("Enter a string: ")
unique_characters_count = 0

for i in range(len(takeStringInputTwo)):
    is_unique = True
    for j in range(i):
        if takeStringInputTwo[i] == takeStringInputTwo[j]:
            is_unique = False
            break

    if is_unique == True:
        unique_characters_count += 1

print("Length of the string:", len(takeStringInputTwo))
print("Number of unique characters:", unique_characters_count)

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.5 :  Write a program that takes a string and returns True if it is a palindrome, False otherwise.

Logic : Using For Loop iterating the given string and with if condition if duplicate character breaking the Loop 
anf from inner loop counting the unique characterwith if c
'''

takeStringInputThree = input("Enter a string: ")

is_palindrome = True
length = len(takeStringInputThree)

for i in range(0, length // 2):
    if takeStringInputThree[i] != takeStringInputThree[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("True : Given String is a palindrome")
else:
    print("False : Given String is not a palindrome")

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.6 :  Write a program that takes two strings and returns the longest common substring between them

Logic : Using For Loop iterating the given string and comparing both the strings and find out the comman one and store in one string variable
'''

takeStringInputFour = input("Enter a string: ")
takeStringInputFive = input("Enter a string: ")

max_substr = ""

# Loop through each character in takeStringInputFour
for i in range(len(takeStringInputFour)):
        # Loop through each character in takeStringInputFive
        for j in range(len(takeStringInputFive)):
            current_substr = ""
            # Compare characters in both strings
            for k in range(min(len(takeStringInputFour) - i, len(takeStringInputFive) - j)):
                if takeStringInputFour[i + k] == takeStringInputFive[j + k]:
                    current_substr  += takeStringInputFour[i + k]
                else:
                    break
            
            # If the current matching substring is longer, update max_substr
            if len(current_substr) > len(max_substr):
                max_substr = current_substr
print("Longest common substring:", max_substr)

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.7 :  Write a program that takes a string and returns the most frequent character in it.

Logic : Using For Loop iterating the given string and comparing between the characters in the given string and increasing the count value if found duplicates 
'''
takeStringInputSix = input("Enter a string: ")
most_frequent = ''
max_count = 0

for char in takeStringInputSix:
        count = 0  # Reset the count for each character
        
        # Count how many times this character appears in the string
        for compareChar in takeStringInputSix:
            if char == compareChar:
                count += 1  # Increase the count if they match
        
        # If this character's count is greater than the max_count found so far
        if count > max_count:
            max_count = count  # Update max_count
            most_frequent = char  # Update the most frequent character
print("The most frequent character is:", most_frequent)

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.8 :  Write a program that takes a string and returns True if it is an anagram of another string. False otherwise

Logic : Using sorted function sorted both the strings and with if condition compared it 
'''
takeStringInputSeven = input("Enter a string: ")
takeStringInputEight = input("Enter a string: ")

takeStringInputSeven = takeStringInputSeven.replace(" ", "").lower()
takeStringInputEight = takeStringInputEight.replace(" ", "").lower()

if sorted(takeStringInputSeven) == sorted(takeStringInputEight):
    print("True : Given Strings are anagrams")
else:
    print("False : Given Strings are not anagrams")

'''
Author : G Gopi Kumar
Date : 12/08/2024

Program No.9 :  Write a program that takes a string and returns the number of words in it

Logic : using split function
'''

takeStringInputNine = input("Enter a string: ")

words = takeStringInputNine.split()
no_of_words=len(words)
print("Number of words in the string:", no_of_words)
  



           