#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: October 9, 2024
#This program asks the user for a word and then encrypts it in Caesar Cipher


startTerm = input("Enter a word: ")
endTerm = ""

for i in range(len(startTerm)):
    oneLetter = startTerm[i:i+1]
    digLetter = ord(oneLetter)+13

    if(digLetter > 122):
        digLetter -= 26
    
    endTerm += chr(digLetter)

print(endTerm)