'''
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
'''

def is_palindrome(word):
  word = word.lower()
  for i in range((len(word) // 2)):
    if word[i] != word[-(i+1)]:
      return False
  return True

print(is_palindrome('anna'))
print(is_palindrome('Civic'))
print(is_palindrome('house'))
print(is_palindrome('Racecar'))