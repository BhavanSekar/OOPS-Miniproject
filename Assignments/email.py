import re
import math
str=input()
fh = open(r"test_emails.xlx", "r").read()
for line in fh.split("n"):
    if str in line:
        print("valid")
    else
        print("invalid")