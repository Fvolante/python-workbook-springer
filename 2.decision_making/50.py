##
# The following table contains earthquake magnitude ranges on the Richter scale and
# their descriptors:
#
#   Magnitude               Descriptor
#   -----------------------------------
#   Less than 2.0           Micro
#   2.0 to less than 3.0    Very Minor
#   3.0 to less than 4.0    Minor
#   4.0 to less than 5.0    Light
#   5.0 to less than 6.0    Moderate
#   6.0 to less than 7.0    Strong
#   7.0 to less than 8.0    Major
#   8.0 to less than 10.0   Great
#   10.0 or more            Meteoric
#
# Write a program that reads a magnitude from the user and displays the appropriate
# descriptor as part of a meaningful message. For example, if the user enters 5.5 then
# your program should indicate that a magnitude 5.5 earthquake is considered to be a
# moderate earthquake.
#

# input
magnitude = float(input("Inserisci la magnito in gradi Richter: "))

# assign descriptor
if magnitude < 2.0:
    desc = "Micro"
elif 2.0 <= magnitude < 3.0:
    desc = "Molto piccola"
elif 3.0 <= magnitude < 4.0:
    desc = "Piccola"
elif 4.0 <= magnitude < 5.0:
    desc = "Leggera"    
elif 5.0 <= magnitude < 6.0:
    desc = "Moderata"    
elif 6.0 <= magnitude < 7.0:
    desc = "Forte"
elif 7.0 <= magnitude < 8.0:
    desc = "Grande"        
elif 8.0 <= magnitude < 10.0:
    desc = "Enorme"            
elif 10.0 <= magnitude :
    desc = "Meteoritica"

# print result 
print("La magnitudo di grado %.2f corrisponde al valore: %s" % (magnitude, desc))

 