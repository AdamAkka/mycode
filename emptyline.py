#!/usr/bin/env python3

newfile = open("mytestfile.txt", "r")
lines = newfile.readlines()
for line in lines:
   if line == "\n":
       print("This line is Empty")
   else:
        print("This line not Empty")
