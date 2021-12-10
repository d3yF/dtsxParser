# dtsxParser
parses sql code from dtsx elements

All you need to set up is the SourceFiles folder, which should contain the .dtsx packages from SSIS,
then the main method needs to be set up in the following manner:
    sourceFileDir - is the folder containing the dtsx files
    intermediateFileDir - the folder, which should output the dtsx files to text
    resultFileDir - the folder, which should contain the output of this procedure