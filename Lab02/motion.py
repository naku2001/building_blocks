# Author: Perfect Makuwerere
# Date: 02/04/2026
# Description: Given a duration of time, this program computes  the velocity, average velocity, and displacement of an object.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Initialize the radius:
time = 10.0

# Calculate the properties of the object:

velocity = initialVelocity + (acceleration*time)
average_velocity = initialVelocity + (0.5 * (acceleration*time))
displacement = initialVelocity*time + (0.5*(acceleration * (time)**2))


# Print the results:

print(f"time = {time}\n\n\nvelocity\t\t= {velocity}\naverage velocity\t= {average_velocity}\ndisplacement\t\t= {displacement}")

 

 
