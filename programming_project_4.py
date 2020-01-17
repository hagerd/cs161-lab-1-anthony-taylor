'This program takes years as input then prints the estimates for death, birth, and immigration'
'per year based upon current population'

#These are the rates of change for a whole year
birth = 4505142.8
death = 2425846.1
immigrant = 901028.5
population = 307357870 

#User inputs amount of years
years = input("Input a number for the amount of years in the future to find the estimated popluation of the US: \n")

#make input an integer
int_year = int(years)

#Equation to find the popluation based on the amount years
estimate = (birth + immigrant + - death) * int_year + population

#print the resultds
print("The population in",years,"years would be {:,.2f}" .format(estimate))