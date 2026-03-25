def reverse_string(s: str) -> str:
    """Returns the reversed version of the input string."""
    return s[::-1]

user_str1 = input("Enter a string to reverse: ")
print(reverse_string(user_str1))  

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

user_str2 = input("\nEnter a string to check if it's a palindrome: ")
print(is_palindrome(user_str2))  

def count_vowels(s: str) -> int:
    """Counts the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

user_str3 = input("\nEnter a string to count its vowels: ")
print(count_vowels(user_str3))  

def capitalize_words(s: str) -> str:
    """Capitalizes the first letter of each word in the input string."""
    return s.title()

user_str4 = input("\nEnter a string to capitalize the first letter of each word: ")
print(capitalize_words(user_str4))  

def count_words(s: str) -> int:
    """Counts the number of words in the input string."""
    return len(s.split())

user_str5 = input("\nEnter a string to count the number of words: ")
print(count_words(user_str5))        



even_range = int(input("\nEnter the maximum number for the even squares list (e.g., 10): "))
even_squares = [x**2 for x in range(1, even_range + 1) if x % 2 == 0]

print(even_squares) 


cubes_range = int(input("\nEnter the maximum number for the cubes dictionary (e.g., 5): "))
cubes_dict = {x: x**3 for x in range(1, cubes_range + 1)}

print(cubes_dict) 

sentence = input("\nEnter a sentence to extract its unique vowels: ")

unique_vowels = {char for char in sentence.lower() if char in "aeiou"}

print(unique_vowels) 
