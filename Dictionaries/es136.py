# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value to
# search for as its only parameters. It will return a (possibly empty) list of keys from
# the dictionary that map to the provided value.
# Include a main program that demonstrates the reverseLookup function as part
# of your solution to this exercise. Your program should create a dictionary and then
# show that the reverseLookup function works correctly when it returns multiple
# keys, a single key, and no keys. Ensure that your main program only runs when
# the file containing your solution to this exercise has not been imported into another
# program.

""" 
find all keys in dictionary arg that maps to a given value
@param dict: dictionary to search in
@param value to search in dict
@return list: list of keys that maps to that value
"""
def reverseLookup(dic, value):

    # set final variable
    result_keys = list()

    # loop on dict's keys
    for key in dic:

        # if key's value is same as the param, add to result list
        if dic[key] == value:
            result_keys.append(key)

    return result_keys


def main():
    test = {"sti":"stoca", 2:"stoca", 3:"stace"}
    print(reverseLookup(test, "stoca"))

    test2 = {1:"sta"}
    print(reverseLookup(test2, "sta"))

    test3 = {}
    print(reverseLookup(test3, "sta"))

if __name__ == "__main__":
    main()