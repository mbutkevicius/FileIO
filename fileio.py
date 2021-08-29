# Okay little note to self. You can find the file path in properties of the document.
# Or in the command line using "   dir "\sample.txt*" /s   " (Type exactly what's inside spaced "")
# You have to then change the \ to / for it to work properly.
# Or You can just do double \\
# Or, and this is probably the easiest way to do this, put the file in your python project (in the C: drive)
# and it'll automatically open with just the file name. This is the method I use here.

# jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')     # end makes it so a new line won't be printed in between
#     # print(line)
# jabber.close()

# Using builtin 'with' is much better because it will close it automatically and prevent more errors.
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='\n')

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')

# readline reads only one line at a time and is better for not using up memory
# readlines reads whole thing and will use up a lot of mem in a big file

