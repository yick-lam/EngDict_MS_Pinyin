#!/usr/bin/python3 

import os
import sys
import pathlib

from msphraser import MschxudpBuilder

USAGE="usage: %s txt_file1 txt_file2 ... dat_file\n"%(sys.argv[0]) \
+ "A program to convert phrase text file into \"user defined phrases\" .dat file" \
+ "Example usage:\n" \
+ "%s ciyu.dic ciyu.dat\n"%(sys.argv[0]) \
+ "%s ciyu.dic ylam.dic ciyu.dat"%(sys.argv[0])

def main():
    if len(sys.argv)<3:
        print(USAGE)
        sys.exit()

    fnOut=pathlib.Path(sys.argv[-1])

    mfb = MschxudpBuilder()

    n=0
    idx=1

    while idx<(len(sys.argv)-1):
        print(sys.argv[idx])
        fp=open(sys.argv[idx], "r")

        while True:
            ln = fp.readline()
        
            if ln == "":
                break
        
            ln = ln.rstrip("\n")
        
            strs = ln.split(" ", 1)
            if len(strs)!=2:
                continue
        
            mfb.add_phrase(shortcut=strs[0], phrase=strs[1])
            n+=1
        
            #print("%s %s"%(key, data))
        
        fp.close()
        idx+=1

    mfb.save(fnOut)

    print("Generated User Defined Phrases (%d) as %s"%(n, fnOut))

main() 
