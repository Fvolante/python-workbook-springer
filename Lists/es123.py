## 
# Extend your solution to Exercise 122 so that it correctly handles uppercase letters and
# punctuation marks such as commas, periods, question marks and exclamation marks.
# If an English word begins with an uppercase letter then its Pig Latin representation
# should also begin with an uppercase letter and the uppercase lettermoved to the end of
# the word should be changed to lowercase. For example, Computer should become
# Omputercay. If a word ends in a punctuation mark then the punctuation mark
# should remain at the end of the word after the transformation has been performed.
# For example, Science! should become Iencescay!.

""" 
Format text line in Pig Latin with punctuation marks
@param: a string of text
@return: a string
"""
def pig_latin_ext(s):

    # list of vowels and marks to compare text
    VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    PUNCTUATION_MARKS = ["'", "!", ":", ",", ";", "?", ".", "-"]

    # set result string
    result = []

    # split param string in single words
    words = s.split()

    for word in words:

        # save possibly punctuation mark and if there is a mark cut him from word
        mark = False
        if word[-1] in PUNCTUATION_MARKS:
            mark = word[-1]
            word = word[:-1]

        # check if word is capitalize
        is_upper = False
        if word[0].isupper():
            is_upper = True

        """ 
        function to properly append capitalized word or not to result variable
        @params: is_upper:bool, word:str to evaluate
        @return none 
        """
        def compose_result_by_word(is_upper, word):

            if is_upper:
                word = word.capitalize()
                result.append(word)
            else:
                result.append(word)
        
        # lower word for manipulate purposes
        word = word.lower()

        # find first vowel in word
        first_vovel = ""
        counter = 0

        while first_vovel == "":
            
            if word[counter] in VOWELS:
                first_vovel = counter

            counter += 1

        # manipulate single words to convert to pig latin
        # if word start by vowel:
        if first_vovel == 0:

            if mark:
                word = word + "way" + mark
            else:
                word = word + "way"

            # append to result by function
            compose_result_by_word(is_upper, word)

        # if word start by consonant:
        else:

            fragment = word[0:first_vovel]

            if mark:
                word = word[first_vovel:] + fragment + "ay" + mark
            else:
                word = word[first_vovel:] + fragment + "ay"
            
            # append to result by function
            compose_result_by_word(is_upper, word)
            

    result = " ".join(result)
    return result

def main():
    s = input("Inserisci una frase:\n")

    print(pig_latin_ext(s))

main()