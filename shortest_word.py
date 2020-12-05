#find  the shotrest word from a listof words

#lst = ('Covid-19 was present in America BEFORE being officially confirmed in Chlstina, study by US health protection agency says')
#lst = lst.split()


def shortest_word (lst):
      if len(lst) == 0:
                return "empty string"
      i = 0
      shortest = lst[0]
      n = len(lst)
      for i in range(1, n):
            if len(lst[i]) < len(shortest) :
                  shortest = lst[i]
            
      print(shortest)                 

shortest_word(['elizabeth', 'Mary', 'Zizi', 'ali', 'Karine']) 
