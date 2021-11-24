## 
# Pig Latin is a language constructed by transforming English words. While the origins
# of the language are unknown, it is mentioned in at least two documents from
# the nineteenth century, suggesting that it has existed for more than 100 years. The
# following rules are used to translate English into Pig Latin:
# • If theword begins with a consonant (including y), then all letters at the beginning of
# theword, up to the first vowel (excluding y), are removed and then added to the end
# of the word, followed by ay. For example, computer becomes omputercay
# and think becomes inkthay.
# • If the word begins with a vowel (not including y), then way is added to the end
# of the word. For example, algorithm becomes algorithmway and office
# becomes officeway.
# Write a program that reads a line of text from the user. Then your program should
# translate the line into Pig Latin and display the result. You may assume that the string
# entered by the user only contains lowercase letters and spaces.

""" 
Format text line in Pig Latin
@param: a string of text
@return: a string
 """
def pig_latin(s):

    # list of vowels to compare text
    VOWELS = ["a", "e", "i", "o", "u"]

    # set result string
    result = []

    # split param string in single words
    words = s.split()

    for word in words:

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

            word = word + "way"

            result.append(word)

        # if word start by consonant:
        else:

            fragment = word[0:first_vovel]
            word = word[first_vovel:] + fragment + "ay"

            result.append(word)

    result = " ".join(result)
    return result

def main():
    s = input("Inserisci una frase:\n")

    print(pig_latin(s))

main()