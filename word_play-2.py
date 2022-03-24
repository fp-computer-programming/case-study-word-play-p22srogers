# Author: SMR (AMDG) 03/23/22

# began by setting up the 2 files we are using and the two methods for getting a line
wordfile = open('words.txt')
noefile = open('words_without_e.txt', 'r+')
wline = wordfile.readline().strip()
eline = noefile.readline().strip()

# counters for the later percentage
noecount = 0
totalcount = 0

# going through each word in the file and checking if it meets this condition
def no_e(word):
    if 'e' not in word:
        # writing to this file
        noefile.write(word)
        return True

# adding each line to the counters

for wline in wordfile:
    totalcount += 1
    no_e(wline)

for eline in noefile:
    noecount += 1

# printing out the percentage of no e's
print("{0}% of words have no e".format((totalcount/noecount)))