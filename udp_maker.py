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

    print(f"Generated User Defined Phrases ({numLinesTotal}) as {fnOut}")
    print(f"(1): 在 Windows 中，請前往 系統設置 → 時間和語言 → 地區和語言 → 中文 → 首選項 → ")
    print(f"微軟拼音 → 首選項 → 詞庫和自學 → 添加或編輯用戶定義短語： 選擇添加上面生成的 {fnOut.name}。")
    print()
    print(f"注意：如果在運行 (1) 時 UI 發生卡住，這是因為之前添加的短語過多。您需要前往")
    print(f"  C:\\Users<YOUR_NAME>\\AppData\\Roaming\\Microsoft\\InputMethod\\Chs\\")
    print(f"文件夾（您可能需要在類似位置進行搜索），並刪除以下文件：")
    print(f"  ChsPinyinEUDPv1.lex")

main() 
