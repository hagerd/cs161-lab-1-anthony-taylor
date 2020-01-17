'This program calculates how deep it would be if all the water in the Great Lakes was' 
'spread evenly across the 48 contiguouse U.S. States'


#print information about great lakes 
print("The Great Lakes are how big?")
print("The Great Lakes in the U.S. contain roughly 22% of the world's fresh water or 22,810 km3.")
print("According to wikipedia the area of the 48 contigous states including the District of Columbia is 8,080,464.3 km2.")

#equation to find depth
x = (22810/8080464.3)*1000

#print results
print("If the Great Lakes were spread across the U.S. they would be {:,.2f} meters deep." .format(x))