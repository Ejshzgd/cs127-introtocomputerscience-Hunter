#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: September 30, 2024
#This program asks the user for a message then prints out that message in reverse.

# ogWord = input("Enter a message: ")

# for i in range(1 , len(ogWord)):
#     print(ogWord[-i-1 : -i] , end=" ")

ogWord = input("Enter a message:")

for i in range(len(ogWord) , 0 , -1):
    revWord = ogWord[i-1:i]
    print(revWord + " " + revWord)
