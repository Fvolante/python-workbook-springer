## 
# Using the definition of a sublist from Exercise 133, write a function that returns a
# list containing every possible sublist of a list. For example, the sublists of [1, 2,
# 3] are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your
# function will always return a list containing at least the empty list because the empty
# list is a sublist of every list. Include a main program that demonstrate your function
# by displaying all of the sublists of several different lists.

"""
generate all passible sublists of a given list
@param: a list
@return: a list of all param's sublists 
"""
def allSublists(values_list):

    # set final list
    result = []

    # loop on each element as a starting point
    for i in range( len(values_list) ):
        
        # loop setting j as a limit to splicing list
        j = i
        while j < len(values_list) + 1:
            
            sublist = values_list[i:j]
            
            # avoid duplicates
            if sublist not in result:
                result.append(sublist)

            j+=1
        
    return result

def main():

    t = [1, 2, 3, 4]
    t2 = [2, 6.45, 7, 2.1, 77, 23423, 0]

    def display_sublists(list):

        for el in allSublists(list):
            print(el)

        print("")

    print("Le sottoliste di {} sono:".format(t))
    display_sublists(t)

    print("Le sottoliste di", t2, "sono:")
    display_sublists(t2)

main()