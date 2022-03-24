# Author: SMR (AMDG) 03/23/22
# OPEN TEXT 
word_file = open('words.txt')
l = word_file.readline().strip()
# start with counter 0
count = 0
# Function sorting
def is_abecedarian(l):
    if l == ''.join(sorted(l)) in l:
        return True
    else:
        return False
        
# For each line in the file add to counter
for l in word_file:
    if is_abecedarian(l):
        count += 1

# final print statement
print('{0} words found.'.format(count))