from os import name
from extractsql import extractsql
from parseSql import parseSql
# from lxml import etree

sourceFileDir = r"C:\Users\dodler\Desktop\CP\SourceFiles"
intermediateFileDir = r"C:\Users\dodler\Desktop\CP\IntermediateFiles"
resultFileDir = r"C:\Users\dodler\Desktop\CP\ResultFiles"


if __name__ == "__main__":
    extractsql(sourceFileDir)
    parseSql(intermediateFileDir, resultFileDir)


