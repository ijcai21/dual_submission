import os
import sys
import hashlib

f_input = open("input.txt","r")
f_output = open("output.txt","wt")

for line in f_input:

    hash_signature=hashlib.sha512(line.encode('utf-8')).hexdigest()
    f_output.write(hash_signature +"\n")

f_input.close()
f_output.close()