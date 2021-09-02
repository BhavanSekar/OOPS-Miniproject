#!/usr/bin/env python3

def run_stuff():

    # pylint wants 'file_handler'
    fileHandler = open("afile.txt") # <-- pylint sees normal variable

    for line in fileHandler:
        Token = line.split("\t")
        Part_1 = Token[0]
        print(Part_1)

if __name__ == '__main__':
    run_stuff()
