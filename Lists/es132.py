## 
# Evaluating a postfix expression is easier than evaluating an infix expression because
# it does not contain any parentheses and there are no operator precedence rules to
# consider. A postfix expression can be evaluated using the following algorithm:
#
# Create a new empty list, values
# For each token in the postfix expression
# If the token is a number then
# Convert it to an integer and append it to values
# Else if the token is a unary minus then
# Remove an item from the end of values
# Negate the item and append the result of the negation to values
# Else if the token is a binary operator then
# Remove an item from the end of values and call it right
# Remove an item from the end of values and call it left
# Compute the result of applying the operator to left and right
# Append the result to values
# Return the first item in values as the value of the expression
#
# Write a program that reads a mathematical expression in infix form from the user,
# converts it to postfix form, evaluates it, and displays its value. Use your solutions
# to Exercises 129, 130 and 131, along with the algorithm shown above, to solve this
# problem.

import sys
sys.path.append('C:/Users/volan/wa/learn_pyhton/workbook')

from Functions.es96 import isInteger
from es129 import tokenize
from es130 import unary_tokens
from es131 import infix_to_postfix
""" 
evaluata a postfix math expression
@param: a list of postif tokens
@return: number:resulto of expression
"""
def evaluate_postfix(postifix_list):

    OPERATORS = ["+", "-", "/", "*", "^"]
    values = []

    for token in postifix_list:

        if isInteger(token):
            values.append( int(token) )
        
        elif token == "u-":
            item = values.pop()
            values.append(- abs(item))

        elif token in OPERATORS:
            right = str(values.pop())
            left = str(values.pop())

            result = eval(left + token + right)
            values.append(result)

    return values[0]

def main():

    expression = input("Scrivi un'espressione matematica con soli numeri interi:\n")

    expression_tokens = unary_tokens(tokenize(expression))
    postfix_expression = infix_to_postfix(expression_tokens)

    print("L'espressione:", expression, "è cosi tokenizzata:\n", expression_tokens)
    print("")
    print("La forma postfix dell'espressione è:\n", postfix_expression)
    print("")
    print("Il risultato dell'espressione in forma postfix è:", evaluate_postfix(postfix_expression))

main()

