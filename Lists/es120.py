## 
# When writing out a list of items in English, one normally separates the items with
# commas. In addition, theword “and” is normally included before the last item, unless
# the list only contains one item. Consider the following four lists:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function
# should return a string that contains all of the items in the list, formatted in the manner
# described previously, as its only result. While the examples shown previously only
# include lists containing four elements or less, your function should behave correctly
# for lists of any length. Include a main program that reads several items from the user,
# formats them by calling your function, and then displays the result returned by the
# function.

""" 
create a string of words formatted with comma and "and" conjiunction
@param: a list of words
@returm: a string formatted
 """
def list_words(some_words):
    
    final_string = ""

    # manage only 1 element in list
    if len(some_words) == 1:
        final_string += some_words[0]

        return final_string

    # more than 1 element in list
    count = 0
    LIMIT = len(some_words) -1
    
    while count <= LIMIT:

        word = some_words[count]

        # penultimate word
        if count == LIMIT - 1:
            word = word + " and "

        # last word
        elif count == LIMIT:
            pass
        
        # other word
        else:
            word = word + ", "

        # compose final string
        final_string += word
        count += 1    
        
    return final_string

def main():
    word = input("Inserisci una parola. lascia vuoto per uscire:\n")

    words = []

    while word != "":
        words.append(word)

        word = input("Inserisci una parola. lascia vuoto per uscire:\n")

    if bool(words) == False:
        print("Nessuna parola inserita")

    else:
        print("le parole inserite sono:")
        print(list_words(words))

main()