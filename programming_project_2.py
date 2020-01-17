'This program asks a user to indiicate the number of days after the launch of the Voyager 1'
'then the program calculates the distance from the sun in miles, kilometers, astronomical units'
'and round trip time for radio communication'






#print some information for user
print("The Voyager 1 space craft, launched September 15, 1977, it is the farthest traveling earth-made object. \n" \
    "On September 25,2009, it was reported of being approximately 16,637,000,000 miles from the Sun. traveling away \n" \
    "from the Sun at 38,241 miles/hour.")

#user input for days
time = input("Enter a number for the amount of days since 9/25/09 to calculate the distances of Voyager 1 from the sun: \n")

#make input an integer
int_time = int(time)

#conversion for days to different speeds
mi = 16637000000 + int_time * (38241 * 24)
km = 26774656128 + int_time * (61542.924 * 24)
au = 178.97752155639 + int_time * (0.00041138904 * 24)
rw = 2 * (mi / 670616629.3844)

#print conversions
print("{:,.2f} miles from the sun. \n" .format(mi),
    "{:,.2f} Kilometers from the sun. \n" .format(km),
    "{:,.2f} Astronomical Units from the sun. \n" .format(au),
    "{:,.2f} round trip time for radios waves to the voyager 1" .format(rw))
