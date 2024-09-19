#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: September 19, 2024
#This program prints the message based on the ASCII table

askMessage = input("Enter a phrase: ")
print("In ASCII:")
for i in range(len(askMessage)):
    print(ord(askMessage[i:i+1]))


