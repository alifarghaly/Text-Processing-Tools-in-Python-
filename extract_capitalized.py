#script to extract capilized words from a running text containing upper and lower case words

f = open('data1.txt', encoding='utf-8',errors='ignore').read().split()

capitalized = []


for word in f:
      if word[0].isupper():
            capitalized.append(word)
print(capitalized)
            

   
