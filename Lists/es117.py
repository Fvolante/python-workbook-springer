## 
# In this exercise you will create a program that identifies all of the words in a
# string entered by the user. Begin by writing a function that takes a string as
# its only parameter. Your function should return a list of the words in the string
# with the punctuation marks at the edges of the words removed. The punctuation
# marks that you must consider include commas, periods, question marks,
# hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove
# punctuation marks that appear in the middle of a word, such as the apostrophes
# used to form a contraction. For example, if your function is provided with the
# string "Contractions include: don’t, isn’t, and wouldn’t."
# then your function s  hould return the list ["Contractions", "include",
# "don’t", "isn’t", "and", "wouldn’t"].
# Write amain program that demonstrates your function. It should read a string from
# the user and then display all of the words in the string with the punctuation marks
# removed. You will need to import your solution to this exercise when completing
# Exercises 118 and 167. As a result, you should ensure that your main program only
# runs when your file has not been imported into another program.

s = "Contractions include: don’t, isn’t, and wouldn’t."

""" 
split a string in a list of words, removing punctuation marks in costant
@param: a string
@return: list
"""
def split_string(s):

    # set mark to remove from words
    PUNCTUATION_MARKS = "'!:,;?.-,"

    # set result list
    result = []

    # split argument string in single words
    s = s.split()
    
    # remove punctuation marks from single words and add to result list
    for word in s:
        
        word = word.strip(PUNCTUATION_MARKS)

        result.append(word)
    
    return result

# define and run main program
def main():
    s = input("Inserisci una frase:\n")

    print("La frase suddivisa nelle sue singole parole è la seguente:")
    print(split_string(s))    
        
if __name__ == "__main__":
    main()