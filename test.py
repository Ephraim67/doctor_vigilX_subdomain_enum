#!/usr/bin/python3
"""Function that read a text file"""

def read_file(filename=""):
    """read the file"""
    with open("my_file_0.txt", encoding="utf-8") as f:
        #read_file = f.read()
        for line in f:
            print(line, end='')

read_file("my_file_0.txt")
