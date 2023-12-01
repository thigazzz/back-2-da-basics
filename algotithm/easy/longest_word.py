"""
Faça com que a função LongestWord(sen) pegue o parâmetro sen que está sendo passado e retorne a palavra mais longa na cadeia de caracteres.
Se houver duas ou mais palavras com o mesmo comprimento, retorne a primeira palavra da cadeia de caracteres com esse comprimento.
Ignore a pontuação e assuma que sen não estará vazio. As palavras também podem conter números, por exemplo "Hello world123 567"
"""

import string

valid_char = string.ascii_letters + '0123456789'

def is_a_word(word):
  for letter in word:
    if letter not in valid_char:
      return False
    
  return True

def LongestWord(sen):

  # code goes here
  sen_as_list = sen.split(' ')
  
  long_word = ''
  for word in sen_as_list:
    if is_a_word(word):
      if len(long_word) < len(word):
        long_word = word

  return long_word

# keep this function call here 
print(LongestWord(input()))