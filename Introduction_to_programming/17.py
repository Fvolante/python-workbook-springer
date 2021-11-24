##
# The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
# computed using the formula:
#               q = mCΔT
# Write a program that reads the mass of some water and the temperature change from
# the user. Your program should display the total amount of energy that must be added
# or removed to achieve the desired temperature change.
#  
#       Hint: The specific heat capacity of water is 4.186 J
#       g◦C. Because water has a
#       density of 1.0 grams per milliliter, you can use grams and milliliters interchangeably
#       in this exercise.
# 
# Extend your program so that it also computes the cost of heating the water. Electricity
# is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
# your program to compute the cost of boiling the water needed for a cup of coffee.
#
#       Hint: You will need to look up the factor for converting between Joules and
#       kilowatt hours to complete the last part of this exercise.
#
# Altro modo per calcolare la capacità termica dell'acqua:
# C = m * 4.18 dove m = massa del materiale
#

# user's input
m = float(input("Inserisci il peso dell'acqua in grammi: "))
delta_t = float(input("Inserisci la variazione di temperatura in gradi che vuoi ottenere: "))

# water heat capacity
C = m * 4.18

# compute energy needed in joule
q = m * C * delta_t

# conversion joule to KWh 1j = 2.778 * 10^-7 KWh 
kwh = q * (2.778 * (10**-7) )

#cost in cents of needed KWh
KWH_COST = 8.9

# 0.29 is costo to raise 50 ml of water from 0 C° to 100 C°. Computed with this script
cost_to_boil_cup_of_cofee = KWH_COST * 0.29

print("Per modificare una massa d'acqua di %.2f grammi di %.2f gradi occorrono %.2f joule, ovvero %.2f KWh" % (m, delta_t, q, kwh))

print("Per far bollire una tazzina di caffè da 50 ml con acqua partendo da 0 c° occorrono %.2f centesimi" %cost_to_boil_cup_of_cofee)
