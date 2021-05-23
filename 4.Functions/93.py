##
# Write a function that takes a string, s, as its first parameter, and the width of the
# window in characters, w, as its second parameter. Your function will return a new
# string that includes whatever leading spaces are needed so that s will be centered in
# the window when the new string is printed. The new string should be constructed in
# the following manner:
# • If the length of s is greater than or equal to the width of the window then s should
# be returned.
# • If the length of s is less than the width of the window then a string containing
# (len(s) - w) // 2 spaces followed by s should be returned.
# Write a main program that demonstrates your function by displaying multiple
# strings centered in the window.
#

def centered_string(s, w):
    
    if len(s) >= w:
        return "*" + s + "*"
    else:
        w = w - 2
        return "*" + ((w - len(s)) // 2) * " " + s + ((w - len(s)) // 2) * " " + "*"

def main():
    s1 = "Ciao a tutti"
    s2 = "Tanti cari saluti"
    print(centered_string(s1, 60))
    print(centered_string(s2, 5))

main() 