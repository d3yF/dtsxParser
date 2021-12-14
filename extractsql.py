import os
from lxml import etree

def extractsql(sourceFileDir, intermediateFileDir):
    
    if not os.path.isdir(intermediateFileDir):
      os.makedirs(intermediateFileDir)
    
    for file in os.listdir(sourceFileDir):
        fileName = os.path.basename(file) 
        tree = etree.parse(f"{sourceFileDir}\{fileName}") 
        root = tree.getroot()
    
        ele_set = set()
        for ele in root.xpath(".//*"):
            ele_set.add(ele.tag)    
        print(ele_set)
        print(len(ele_set))
    

        total_bytes = 0
        package_name = root.attrib['{www.microsoft.com/SqlServer/Dts}ObjectName'].replace(" ","")
        for cnt, ele in enumerate(root.xpath(".//*")):
          if ele.tag == "{www.microsoft.com/SqlServer/Dts}Executable":
            attr = ele.attrib
            for child0 in ele:
              if child0.tag == "{www.microsoft.com/SqlServer/Dts}ObjectData":
                for child1 in child0:
                  sql_comment = attr["{www.microsoft.com/SqlServer/Dts}ObjectName"].strip()
                  if child1.tag == "{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlTaskData":
                    dtsx_sql = child1.attrib["{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource"]
                    dtsx_sql = "-- " + sql_comment + "\n" + dtsx_sql
                    sql_file = intermediateFileDir + f"\{fileName}_objects.txt"
                    total_bytes += len(dtsx_sql)
                    print((len(dtsx_sql), sql_comment, sql_file))
                    with open(sql_file, "a") as file:
                        file.write(dtsx_sql)


