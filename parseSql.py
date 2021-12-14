import os
import re


def parseSql(intermediateFileDir, resultFileDir):
    
    keywords = ['from','exec' ,'insert into','delete from', 'into', 'drop table', 'select * into']

    if not os.path.isdir(resultFileDir):
        os.makedirs(resultFileDir)

    for file in os.listdir(intermediateFileDir):
        fileName = os.path.basename(file) 
        outputFile = f"{fileName.split('.')[0]}_resultFile.txt" 

        lines = set()

        with open(f"{intermediateFileDir}\{fileName}" , 'r') as source:
            for sourceline in source.readlines():             
                sourceline = sourceline.lower().rstrip()                
                lines.add(sourceline)

        for pattern in keywords:
            for line in lines:
                if (line.__contains__(pattern)) and (not line.__contains__("fetch next")):
                    reg = '[^\s|^-]+'
                    newline = line[line.index(pattern) + len(pattern):].strip()
                    if (len(newline) > 0):
                        result = re.search(reg, newline)
                        with open(f"{resultFileDir}\{outputFile}", mode= 'a' ) as rsltfl:
                            rsltfl.writelines(result.group() + '\n')



    
