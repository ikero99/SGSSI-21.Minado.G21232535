import hashlib
import sys

if len(sys.argv) != 2:
    print("ERROR: usage should be python hashchecker.py <file>")
    exit(-1)
infilename = sys.argv[1]
with open(infilename, "r") as bloque:
    print("Hash: " + hashlib.sha256(bloque.read().encode()).hexdigest())
