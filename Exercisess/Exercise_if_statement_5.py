# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai 
# and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter city name: ").lower()
if city in india:
    print(f"{city} is in country: india")
elif city in pakistan:
    print(f"{city} is in country: pakistan")
elif city in bangladesh:
    print(f"{city} is in coutry: bangladesh")
else:
    print(f"Sorry, I couldn't find to which country {city} belongs.😢")

cities=input("Enter two cities: ")
city1,city2=cities.split()
if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")


#Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal
sugar_level = int(input("Enter your fasting sugar level: "))
if sugar_level<80:
    print("Sugar level is low")
elif sugar_level>100:
    print("Sugar level is high")
else:
    print(f"{sugar_level} is normal sugar level range.")
