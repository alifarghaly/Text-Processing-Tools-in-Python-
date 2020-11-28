# This script reverses a word or a running text

def Reverse ():
    txt = input("Please write down the word or the sentence you want to reverse.\n")
    txt = txt.split()
    if len(txt) != 1:
      print(txt[::-1])
    else:      
       print(txt[0][::-1])

Reverse()
         
  
 
