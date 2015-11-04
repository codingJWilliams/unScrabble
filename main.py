#select file location
flocation = 'words.txt'
# start code





thelist = [line.rstrip('\n') for line in open(flocation)]
print("Scrabble helper.")
letters = str(input("Please enter the letters you have to work with.\n>"))
wordsdone = 0
while wordsdone == len(thelist):

