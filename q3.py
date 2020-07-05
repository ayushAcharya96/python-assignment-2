'''
3. Write code that will print out the anagrams ( words
 that use the same letters) from a paragraph of text.
'''
SPECIAL_CHARACTERS = {
  '`','!','@','#','$','%','^','&','*','(',')','-','+','=',
  '_','0','9','8','7','6','5','4','3','2','1','`','[',']',
  '\\','{','}','|',';',':','\'','"',',','<','.','>','?','/'
  }
def remove_punctuation(paragraph):
  result = ""
  for char in paragraph:
    if char not in SPECIAL_CHARACTERS:
      result += char
  return result
def find_anagrams(paragraph):
  paragraph = remove_punctuation(paragraph).lower()
  word_list = paragraph.split()
  result_dict = {}
  for word in word_list:
    temp_word = ''.join(sorted(word))
    if temp_word not in result_dict.keys():
      result_dict[temp_word] = [word]
    elif word not in result_dict[temp_word]:
      result_dict[temp_word].append(word)
  return result_dict

paragraph = '''it ti the ehe hee the you your rouy if fi the see ese'''

print(find_anagrams(paragraph))
