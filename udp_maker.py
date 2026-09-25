#!/usr/bin/python3 

import os
import sys
import pathlib

from msphraser import MschxudpBuilder

USAGE="usage: %s txt_file1_glob txt_file2_glob ... dat_file\n"%(sys.argv[0]) \
+ "A program to convert text files into \"user defined phrases\" .dat file\n" \
+ "(used for Microsoft Pinyin IME.)\n" \
+ "The text files should be in the format of:\n" \
+ "english chinese (separate with space)\n" \
+ "Example usage:\n" \
+ "%s ciyu.dic ciyu.dat\n"%(sys.argv[0]) \
+ "%s eng_chi_?.txt eng_misc.txt mspinyin.dat"%(sys.argv[0])

def main():
    if len(sys.argv)<3:
        print(USAGE)
        sys.exit()

    fnOut=pathlib.Path(sys.argv[-1])
    mfb = MschxudpBuilder()

    # now we must find all the input files and read them one by one
    inputFileList=[]
    for arg in sys.argv[1:-1]:
        inputFileList.extend(pathlib.Path().glob(arg))

    if len(inputFileList)==0:
        print("No input files found!")
        sys.exit()

    maxFnLen = max(len(fp.name) for fp in inputFileList)
    print("Number of input files: %d"%(len(inputFileList)))

    idx=0
    numLinesTotal=0
    while idx<len(inputFileList):
        fp=open(inputFileList[idx], "r", encoding="utf-8")
        numLinesThisFile=0
        while True:
            ln = fp.readline()
       
            if ln == "":
                break
        
            ln = ln.rstrip("\n")
        
            strs = ln.split(" ", 1)
            if len(strs)!=2:
                continue
        
            mfb.add_phrase(shortcut=strs[0], phrase=strs[1])
            numLinesThisFile+=1
            #print("%s %s"%(key, data))
        
        fp.close()
        numLinesTotal+=numLinesThisFile
        print(f"{(idx+1):2d}/{len(inputFileList)}: {inputFileList[idx].name:<{maxFnLen}} ({numLinesThisFile:4d} lines)")
        idx+=1
    
    mfb.save(fnOut)

    print("Generated User Defined Phrases (%d) as %s"%(numLinesTotal, fnOut))

main() 
