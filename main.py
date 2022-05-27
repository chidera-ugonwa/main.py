# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word)== sorted(anagram)):
        return True
    else:
        return False
    
# driver code 
word = input('Enter a Word:  ').lower()
anagram = input('Enter the Anagram of that Word: ').lower()
find_anagram(word, anagram)
