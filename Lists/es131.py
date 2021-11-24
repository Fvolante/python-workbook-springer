## 
# Mathematical expressions are often written in infix form, where operators appear
# between the operands on which they act. While this is a common form, it is also
# possible to express mathematical expressions in postfix form, where the operator
# appears after all of its operands. For example, the infix expression3 + 4is written
# as3 4 +in postfix form. One can convert an infix expression to postfix form using
# the following algorithm:
#
# Create a new empty list, o perators
# Create a new empty list, postfix
# For each token in the infix expression
# If the token is an integer then
# Append the token to postfix
# If the token is an operator then
# While operators is not empty and
# the last item in operators is not an open parenthesis and
# precedence(token) < precedence(last item in operators) do
# Remove the last item from operators and append it to postfix
# Append the token to operators
# If the token is an open parenthesis then
# Append the token to operators
# If the token is a close parenthesis then
# While the last item in operators is not an open parenthesis do
# Remove the last item from operators and append it to postfix
# Remove the open parenthesis from operators
# While operators is not the empty list do
# Remove the last item from operators and append it to postfix
# Return postfix as the result of the algorithm
#
# Use your solutions to Exercises 129 and 130 to tokenize amathematical expression
# and identify any unary operators in it. Then use the algorithm above to transform the
# expression from infix form to postfix form. Your code that implements the preceding
# algorithm should reside in a function that takes a list of tokens representing an
# infix expression (with the unary operators marked) as its only parameter. It should
# return a list of tokens representing the equivalent postfix expression as its only result.
# Include a main program that demonstrates your infix to postfix function by reading
# an expression from the user in infix form and displaying it in postfix form.
# The purpose of converting from infix form to postfix form will become apparent
# when you read Exercise 132. You may find your solutions to Exercises 96 and 97
# helpful when completing this problem. While you should be able to use your solution
# to Exercise 96 without any modifications, your solution to Exercise 97 will need to
# be extended so that it returns the correct precedence for the unary operators. The
# unary operators should have higher precedence than multiplication and division, but
# lower precedence than exponentiation.

import sys
sys.path.append('C:/Users/volan/wa/learn_pyhton/workbook')

from Functions.es96 import isInteger
from es129 import tokenize
from es130 import unary_tokens

""" 
(modified version from ex.97)represent math operator precedence
@param string which is a math operator
@return int for precedence 
"""
def precedence(s):

    if s == "+" or s == "-":
        return 1
    
    elif s == "*" or s == "/":
        return 2

    elif s == "u+" or s == "u-":
        return 3 

    elif s == "^":
        return 4

    else:
        return -1

""" 
convert a math expression from infix to postfix form
@param: list: a list of tokens representing the infix expression to evaluate
@return: list: a list of tokens representing the param list in postfix form
"""
def infix_to_postfix(tokens_expression):

    # set initial variables
    OPERATORS = ["+", "-", "u-", "u+", "/", "*", "^"]
    operators = []
    postfix = []

    for token in tokens_expression:
        #print("current token----> ", token)
        if isInteger(token):
            postfix.append(token)
        
        elif token in OPERATORS:

            """ if operators:
                print(f"operators: {operators}")
                print(f"la precedenza del token:{token} è {precedence(token)}\nla precedenza dell'ultimo operatore {operators[-1]} è {precedence(operators[-1])}") """
                

            while operators and \
                  operators[-1] != "(" and \
                  precedence(token) < precedence(operators[-1]):

                """ print("stoc")
                print("last:", operators[-1]) """
                postfix.append( operators.pop() )

            operators.append(token)
            """ print(f"operators: {operators}")
            print("") """

        elif token == "(":
            operators.append(token)

        elif token == ")":

            while operators[-1] != "(":
                postfix.append( operators.pop() )

            operators.remove("(")


    while operators:
        postfix.append( operators.pop() )


    return postfix

def main():

    expression = input("Scrivi un'espressione matematica con soli numeri interi:\n")

    print("L'espressione:", expression.replace(" ", ""), "è cosi tokenizzata:\n", tokenize(expression))
    print("")
    print("Gli operatori unari sono qui evidenziati:\n", unary_tokens(tokenize(expression)))
    print("")
    print("La forma postfix dell'espressione è:\n", infix_to_postfix(unary_tokens(tokenize(expression))))

    

if __name__ == "__main__":
    main()
