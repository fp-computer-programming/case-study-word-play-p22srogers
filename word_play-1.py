# Author: SMR (AMDG) 03/23/22

# Open text and strip it
wordfile = open('words.txt')
line = wordfile.readline().strip()
greaterfile = open('greater_than_20.txt', 'w')

# Reads words and adds if it meets condition
for line in wordfile:
    if len(line) > 20:
        # adds this word to the file if it does
        greaterfile.write(line)