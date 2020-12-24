#find if there an repeated letters in  a string

def unique(word):
    word=word.lower()
    uniqletters = len(set(word))
    wordlength = len(word)
    if uniqletters == wordlength:
            print("This word does not have suplicate letters")
    else:
            print("This word has duplicates")





