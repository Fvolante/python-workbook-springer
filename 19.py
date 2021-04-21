##
# Create a program that determines how quickly an object is travelling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
# due to gravity is 9.8 m/s**2. You can use the formula 
# vf = #  # v2 # i# + 2ad  
# to compute the
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
#             
import math

d = float(input("Inserisci l'altezza da cui viene lanciato l'oggetto in metri: "))

# speed costants in m/s**2
INITIAL_SPEED = 0
ACCELERATION = 9.8

# compute final speed
final_speed = math.sqrt(INITIAL_SPEED + 2 * (ACCELERATION * d))

print("L'oggetto tocca il suolo ad una velocità di %.2f metri al sec. quadrato" %final_speed)