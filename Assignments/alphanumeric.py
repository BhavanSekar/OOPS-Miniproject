import re
import math
str=input()
fh = open(r"test_emails.txt", "r").read()
for line in fh.split("n"):
    if str in line:
        print(line)