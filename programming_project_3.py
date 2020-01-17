'This program prompts the user for a floating-point number that statnds for gallons'
'of gasoline then reprints that value along with other information about gasoline.'


#user input for gallons
gallon = input("How manys gallons?\n")

#convert input to float
g = float(gallon)

#equations for each conversion
liters = g * 3.78541 
barrel = g / 19.5 
co2 = g * 20
gasoline = g * 115000
enthanol = g * 75700
price = g * 3.00

#print the input with the conversion for each item
print("{:,.2f} liters of gasoline\n" .format(liters),
    "{:,.2f} Number of barrels of oil to make.\n".format(barrel),
    "{:,.2f} pounds of Co2 produced.\n" .format(co2),
    "{:,.2f} BTUs of gasoline energy.\n" .format(gasoline),
    "{:,.2f} BTUs of ehanol energy.\n" .format(enthanol),
    "${:,.2f} is the cost" .format(price))
    