\*This script uses Counter and created a dictioary from a text file where the keys in the dictionary are
tokens in the fle and he values are the frequencies of these tokens in the file. Then using Counter from 
collections to get the most common words in the file
*/ 

from collections import Counter

f = open('my_file.txt',encoding='utf-8',errors='ignore').read().lower().split()
#create an empty dictionary

dict = {}
for word in f:
    dict.setdefault(word,0)
    dict[word] = dict[word] + 1
a= Counter(dict)
print(a.most_common(10))
