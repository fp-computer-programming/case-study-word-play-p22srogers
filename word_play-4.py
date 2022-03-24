# Author: SMR (AMDG) 03/23/22

# Opens the file and strips it
wordfile = open('words.txt')
l = wordfile.readline().strip()


# Function counting the uses
def uses_only(uses):
    count = 0
    
# function that checks for requirements

    for l in wordfile:
        if uses in l:
            count += 1
    return count
        

inclusion = input('Enter the string to include: ')

# Final print statement
print('{0} words found.'.format(uses_only(inclusion)))