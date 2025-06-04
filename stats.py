# Open a file and output the raw text; close the file
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


# This function takes a string and outputs the number of words (integer) of that string
def word_count(text):
    splitted_text = text.split() #note: list
    return len(splitted_text)

# The input is a string, the function outputs a dictionary with the count of each character in that string.
# Characters can be special like spaces and characters are turned into lower cases.
def each_character_count(text):
    #we look at each and every character one by one? Then we either add it to a dict or +1 it
    solution = dict()
    for character in text:
        character = character.lower()
        if character in solution:
            solution[character] += 1
        else:
            solution[character] = 1
    return solution

def char_dic_into_char_list(char_dic):
    solution = []
    for i in char_dic:
        solution.append({"character":i, "num":char_dic[i]})
    return solution

def sort_on(input_dic):
    return input_dic["num"]

def sort_character_count(char_dic):
    char_list = char_dic_into_char_list(char_dic)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def report_character_count(path):
    # Get the text of the book
    text_book = get_book_text(path)
    # Get a dictionary of the characters in the text
    characters_book = each_character_count(text_book)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text_book)} total words")
    print("--------- Character Count -------")

    # Now, the dictionary gets sorted, using a series of new functions
    sorted_list = sort_character_count(characters_book)
    # Now we go over that sorted list, reporting every character thats .isalpha()
    for i in sorted_list:
        if i["character"].isalpha():
            print(f"{i["character"]}: {i["num"]}")
    print("============= END ===============")
    return None