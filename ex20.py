# import argv from sys module
from sys import argv

# unpack argv to script and input_file
script, input_file = argv

# define function to print the whole file
def print_all(f):
    print f.read()

# define function: go back to the top of the file
def rewind(f):
    f.seek(0)

# function: print file by lines
def print_a_line(line_count, f):
    print line_count, f.readline()

# open file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
print_all(current_file)
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
print_all(current_file)
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
print_all(current_file)
# i=1
# while(i<10):
#     print i
#     i += 1
