# This function takes a string and outputs the number of words (integer) of that string
def word_count(text):
    splitted_text = text.split() #note: list
    return len(splitted_text)