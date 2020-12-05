# This scrip extracts the longest word from a list of words, if these is more than one, it extracts the first one in the list

def find_longest_word(words):
      longest_word = words[0]
      i = 1
      n = len(words)

      for i  in range(1, n):
            if len(words[i]) >  len(longest_word):
                  longest_word= words[i]
      print(longest_word)

find_longest_word(['LOCAL', 'INSPIRATION', 'of', 'the', 'day'])
