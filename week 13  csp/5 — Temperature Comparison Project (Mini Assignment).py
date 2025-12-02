# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperature = float(input("Enter today's temperature in F: "))

if temperature < -10 or temperature > 110: 
    print ("Freezing Cold Warning!")
elif temperature < 50: 
    print("Little chilly, bring a sweater.")
elif temperature < 85: 
    print("Its warm.")
else:
    print("Its hot outside.")