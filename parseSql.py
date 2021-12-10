import os
import re


def parseSql(intermediateFileDir, resultFileDir):
    
    pattern = ['from','exec' ,'insert into','delete from', 'into']
    #resultFiledir = r"C:\\Users\\dodler\\Desktop\\CP\\ResultFiles\\"
    if not os.path.isdir(resultFileDir):
        os.makedirs(resultFileDir)

    for file in os.listdir(intermediateFileDir):
        fileName = os.path.basename(file) 
        outputFile = f"{fileName.split('.')[0]}_resultFile.txt" 

        lines = set()

        with open(f"{intermediateFileDir}\{fileName}" , 'r') as source:
            for sourceline in source.readlines():             
                sourceline = sourceline.lower()                
                lines.add(sourceline)

        for elem in pattern:
            for line in lines:
                if (line.__contains__(elem)) and (not line.__contains__("fetch next")):
                    with open(f"{resultFileDir}\{outputFile}", mode= 'a' ) as rsltfl:
                        rsltfl.writelines(line)



    
