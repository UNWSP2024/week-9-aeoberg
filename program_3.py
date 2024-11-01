# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
try:
    def sum_numbers_from_file():
        totalSum = 0
        n = open("numbers.txt","r")
        for line in n:
            totalSum += int(line)
        print(f'The total sum is: {totalSum}')
        print('In the sum_numbers_from_file function')

except IOError:
    print("Unable to read or write the file (IOERROR)")

except ValueError:
    print("Not an integer, try putting in a integer.")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()