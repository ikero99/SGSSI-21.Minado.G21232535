import hashlib
import random
import sys
import time
from multiprocessing import Process
from progress.bar import Bar


def progressbar(tiempo):
    with Bar('Processing...') as bar:
        for i in range(100):
            a = (int(tiempo)-1)/100
            time.sleep(a)
            bar.next()


def how_many_concurrent_zeros(sha):
    count = 0
    for i in range(0, len(sha)):
        if sha[i] == '0':
            count = count + 1
            continue
        else:
            return count
    return count


def minadotiempo(infilename, outfilename, tiempo):
    t_end = time.time() + tiempo
    mayorhashlength = 0
    with open(infilename, 'r') as block, open(outfilename, 'wb') as blockHash:
        content = block.read()
        while time.time() < t_end:
            content_with_hex = content + hex(random.getrandbits(32))[2:] + " G21232535"
            hashed = hashlib.sha256(content_with_hex.encode())
            hashlength = how_many_concurrent_zeros(hashed.hexdigest())
            if mayorhashlength < hashlength:
                mined_content = content_with_hex
                mayorhash = hashed
                mayorhashlength = hashlength
        blockHash.write(mined_content.encode("utf-8"))
        print("\n" + mayorhash.hexdigest())


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("ERROR: usage should be python hashminingTime.py <file> outfilename timeint")
        exit(-1)

    x = Process(target=minadotiempo, args=(sys.argv[1], sys.argv[2], int(sys.argv[3])))
    y = Process(target=progressbar, args=(sys.argv[3], ))
    x.start()
    y.start()
    x.join()
    y.join()
