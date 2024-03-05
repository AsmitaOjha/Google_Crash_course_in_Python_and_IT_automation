#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
length=92
width=48.8
area=length*width
print(f'The area is {area: .3f} meter square')

# You bought 9 packets of potato chips from a store. 
# Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?
total_potato_chips=9
cost_of_one=1.49
total_cost=total_potato_chips*cost_of_one
Shopkeeper_going_to_give_back=20-total_cost
print("Shopkeer is going to give me:" + str(Shopkeeper_going_to_give_back))

# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
area_of_tile= 5.5**2
Cost_per_square_feet = 500
total_cost=Cost_per_square_feet*area_of_tile
print(total_cost)

#Print binary representation of number 17
num=17
print('Binary of number 17 is:',format(num,'b')) # Ans: 10001



