# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
#
# print "The numbers: "
#
# for num in numbers:
#     print num

def integer(arg):
    i = 0
    numbers = []

    while i < arg:
        numbers.append(i)
        i += 1

    return numbers

m = raw_input()
numbers = integer(int(m))
if numbers == range(int(m)):
    print "1"
else:
    print "0"
