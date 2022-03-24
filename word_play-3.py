# Author: SMR (AMDG) 03/23/22

wordfile = open('words.txt')
l = wordfile.readline().strip()


# defined the function
def avoid(text):
    count = 0
    # checks if the line meets the requirements
    for l in wordfile:
        if text not in l:
            count += 1
    return count
            

exclusion = input('Please enter the string to exclude: ')

# Final print statement
print('{0} words found excluding the string'.format(avoid(exclusion)))