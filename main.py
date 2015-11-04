#select file location
flocation = 'words.txt'
thelist = [line.rstrip('\n') for line in open(flocation)]
print("Scrabble helper.")
letters = str(input("Please enter the letters you have to work with.\n>"))

