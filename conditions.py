# CS104
# First name Last name
# conditions.py

# Prompting user to enter the current temperature
temp = int(input("Please enter the current temperature"))

# Checking temperature conditions and providing appropriate advice
if temp > 90:
    print("Wear Shorts")
elif temp > 70:
    print("Short sleeves are fine")
elif temp > 50:
    print("Wear a jacket")
elif temp > 32:
    print("Wear a heavy coat")
else:
    print("Stay Inside")
