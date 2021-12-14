from os import name
from extractsql import extractsql
from parseSql import parseSql
# from lxml import etree

sourceFileDir = r"C:\devGIT\dtsxParser\SourceFiles"
intermediateFileDir = r"C:\devGIT\dtsxParser\IntermediateFiles"
resultFileDir = r"C:\devGIT\dtsxParser\ResultFiles"


if __name__ == "__main__":
    extractsql(sourceFileDir, intermediateFileDir)
    parseSql(intermediateFileDir, resultFileDir)