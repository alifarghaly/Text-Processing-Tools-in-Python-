#detect  duplicate letters  in a string and disply their frequencies

def remident (word):
    my_dict={}
    for letter in (word):
        letter_count = word.count(letter)
        if letter_count > 1:
            my_dict[letter]= letter_count
    print(my_dict)
            
