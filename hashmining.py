import hashlib
import random
import sys
import time
from multiprocessing import Process
from itertools import cycle



def minado(infilename, outfilename, numberofzero):
    encontrado = True
    with open(infilename, 'r') as block, open(outfilename, 'wb') as blockHash:
        content = block.read()
        while encontrado:
            file_with_hex = content + hex(random.getrandbits(32))[2:] + " G21"
            hashed = hashlib.sha256(file_with_hex.encode())
            if how_many_concurrent_zeros(hashed.hexdigest()) >= numberofzero:
                print("\n" + hashed.hexdigest())
                blockHash.write(file_with_hex.encode("utf-8"))
                encontrado = False


def ruedita():
    for frame in cycle(r'-\|/-\|/'):
        print('\r', frame, sep='', end='', flush=True)
        time.sleep(0.2)


def how_many_concurrent_zeros(sha):
    count = 0
    for i in range(0, len(sha)):
        if sha[i] == '0':
            count = count + 1
            continue
        else:
            return count
    return count


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("ERROR: usage should be python hashmining.py <file> outfilename int")
        exit(-1)
    x = Process(target=minado, args=(sys.argv[1], sys.argv[2], int(sys.argv[3])))
    y = Process(target=ruedita)
    x.start()
    y.start()
    x.join()
    y.terminate()

