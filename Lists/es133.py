## 
# A sublist is a list that is part of a larger list. A sublist may be a list containing a
# single element, multiple elements, or even no elements at all. For example, [1],
# [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
# sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
# the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
# any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
# meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].
# In this exercise you will create a function, isSublist, that determines whether
# or not one list is a sublist of another. Your function should take two lists, larger
# and smaller, as its only parameters. It should return True if and only if smaller
# is a sublist of larger. Write a main program that demonstrates your function.
""" 
check if a list is a sublist of another
@param: list: a list to search in
@param: list: a list to check
@return: bool: true if the list is sublist of the other, false if not
"""
def isSublist(larger, smaller):

    # set result for special cases  
    if smaller == [] or smaller == larger:

        return True
        
    else:

        # loop on smaller list and perform checking for each element if it is present in larger list
        for el in smaller:

            if el in larger:

                # set starting and ending position to slice larger list in smaller one
                start_pos = larger.index(el)
                end_pos = start_pos + (len(smaller))

                # return true if sliced larger is same as smaller list
                if smaller == larger[start_pos:end_pos]:
                    return True

        return False

def main():

    t = [1, 23, -4, 3.45, 908]
    t2 = [23, -4, 3.45, 23]
    t3 = [-4, 3.45]
    t4 = [1, 23]
    t5 = [23, 3.45]

    print("La lista {} {} sottolista di {}".format( t2 ,"È" if isSublist(t, t2) else "NON È", t ))
    print("La lista {} {} sottolista di {}".format( t3 ,"È" if isSublist(t, t3) else "NON È", t ))
    print("La lista {} {} sottolista di {}".format( t4 ,"È" if isSublist(t, t4) else "NON È", t ))
    print("La lista {} {} sottolista di {}".format( t5 ,"È" if isSublist(t, t5) else "NON È", t ))
    print("La lista {} {} sottolista di {}".format( [] ,"È" if isSublist(t, []) else "NON È", t ))

main()