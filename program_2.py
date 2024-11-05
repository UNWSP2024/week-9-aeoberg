# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

if __name__ == '__main__':
    numberOfRandomNumbers = int(input("How many random numbers do you want in the file? "))

    if numberOfRandomNumbers > 1000:
        print("We are experiencing an error, please select a different number")
    else:
        n = open("randomNumbers.txt","w")
        for b in range(numberOfRandomNumbers):
            randomNumber = (random.randint(1,500))
            # print(randomNumber)
            turnIntoAString = str(randomNumber)
            n.write(f'{turnIntoAString}\n')
