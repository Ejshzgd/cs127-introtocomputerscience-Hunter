#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: October 21, 2024
#This program asks the user for the number of hours till weekend. Then, it takes the number and converts it to days and the remanining hours

hoursTillWeekend = int(input("Enter number of hours:  "))

days = int(hoursTillWeekend/24)
hours = hoursTillWeekend%24

print("Days: " , days)
print("Hours: ", hours)