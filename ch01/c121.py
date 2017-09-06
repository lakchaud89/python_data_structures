# Write a Python program that repeatedly reads lines from standard input until an EOFError is raised,
# and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).

import sys
lines = []
try:
    for line in sys.stdin:
        lines.append(line)
    for x in reversed(lines):
        print x
except EOFError:
    print "End of File reached"
