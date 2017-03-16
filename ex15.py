# import argv from sys module
from sys import argv

# unpack argv to script and filename
script, filename = argv

# define object txt by using open function to relate file filename
txt = open(filename)

# print the file name
print "Here's your file %s:" % filename
# print the content of the file
print txt.read()

# ask to type the filename again
print "Type the filename again:"
file_again = raw_input(">")

# attach the file to object txt_again
txt_again = open(file_again)

# print the content of the file
print txt_again.read()
