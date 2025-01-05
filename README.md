# English Dictionary (User defined phrases) for Microsoft Pinyin input method
## Reference
- [UserDefinedPhraser](https://github.com/kyan001/UserDefinedPhraser): Code snippet used from
[UserDefinedPhraser](https://github.com/kyan001/UserDefinedPhraser/blob/master/phrasers/msphraser.py): A portion of the `msphraser`
file was utilized in this project.

## Introduction
This is Python code to allow you to add a large number of "User defined phrases" into the Microsoft Pinyin method.  

## Text file format
The text file format is:
```txt
(code)(space)(phrase)
```
As an example of text file is:
```txt
apple 蘋果
banana 香蕉
```

An example English → Chinese dictionary [eng_chi_dict.txt](eng_chi_dict.txt) is added.  
The dictionary is in Traditional Chinese. 

## Making the *.dat file from the text file
To generate .dat file from the text file (use eng_chi_dict.txt as example, other user-defined file can be used as long as 
the text file is in UTF-8 and without BOM)

1) Install Python
2) Open cmd windows and run the following:
   ```sh
   python udp_make.py eng_chi_dict.txt eng_chi_dict.dat
   ```
3) the eng_chi_dict.dat is generated.

## How to import into the Microsoft Pinyin Method

