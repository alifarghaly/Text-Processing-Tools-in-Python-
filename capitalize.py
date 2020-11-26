#capitalize each word in s string except for prepositions
from timeit import default_timer as timer
start = timer()
my_string=('word of advice to everyone')
lst=[]
my_string = my_string.split()
for i in my_string:
    if len(i) > 2:
        i = i.capitalize()
#store the words in list instead of each word on a separate line        
    lst.append(i)
#to change the list into a string with a space between words
    
newlst = ' '.join(lst)    
print(newlst)
stop = timer()
print(stop-start)



