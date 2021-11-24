## 
# Exercises 75 and 76 previously introduced the notion of a palindrome. Such palindromes
# examined the characters in a string, possibly ignoring spacing and punctuation
# marks, to see if the string was the same forwards and backwards. While
# palindromes are most commonly considered character by character, the notion of
# a palindrome can be extended to larger units. For example, while the sentence “Is
# it crazy how saying sentences backwards creates backwards sentences saying how
# crazy it is?” isn’t a character by character palindrome, it is a palindrome when examined
# a word at a time (and when capitalization and punctuation are ignored). Other
# examples of word by word palindromes include “Herb the sage eats sage, the herb”
# and “Information school graduate seeks graduate school information”.
# Create a program that reads a string from the user. Your program should report
# whether or not the entered string is a word by word palindrome. Ignore spacing and
# punctuation when determining the result.

from es117 import split_string

""" 
check if a sentence is a word by word palindrome: ignores punctuation marks and case sensitive letters
@param: a string
@return: bool
 """
def is_word_by_word_palindrome(s):

    # split string in list removing punctuation marks
    s = split_string(s)

    # lower all words in list
    for i in range(len(s)):
        
        s[i] = s[i].lower()
        
    """ if s == s[::-1]:
        return True
    else:
        return False """

    # check palindrome and return by ternary operator
    return True if s == s[::-1] else False

s = "Herb the sage eats sage, the herb"  
s2 = "Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?"
s3 = "Information school graduate! seeks; graduate school information"

print(is_word_by_word_palindrome(s3))