import sys
import os
import time
import hashlib

def getChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def directroyDuplicatesRemovel(DirectoryName):
    Border = "-"*50
    timestamp = time.ctime()
    StartTime = time.time()

    LogFileName = "Log1_%s.txt" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Mayur Londhe\n")
    fobj.write("This is Directroy Duplicates Files Delete Automation\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(not Ret):
        print("There is no such directory.")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(not Ret):
        print("It is not directory.")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            checkSum = getChecksum(fname)

            if(checkSum in Duplicate):
                Duplicate[checkSum].append(fname)
            else:
                Duplicate[checkSum] = [fname]

    fobj.write("Duplicate Deleted files are below.\n")

    Count = 0
    DeletedFileCount = 0

    for value in Duplicate:

        if(len(Duplicate[value]) > 1):

            for subValue in Duplicate[value]:

                Count = Count + 1
                if(Count > 1):
                    print(f"Deleted File : {subValue}")
                    os.remove(subValue)
                    fobj.write(subValue+"\n")

                    DeletedFileCount = DeletedFileCount + 1
        Count = 0

    EndTime = time.time()

    print("Total files are delete : ", DeletedFileCount)
    print(f"Total Time required for this process is : {EndTime - StartTime} seconds")

    fobj.write(f"Total files are delete :  {DeletedFileCount}\n")
    fobj.write(f"Total Time required for this process is : {EndTime - StartTime} seconds\n")
    fobj.write(Border+"\n")

    fobj.close()

    
def main():
    Border = "-"*40
    print(Border)
    print("Delete duplicate file from directroy Automation")
    print(Border)
    if(len(sys.argv) > 0):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform to delete all duplicate files from given directory.")
            print("This is a automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print(f"{sys.argv[0]} Argument1 Argument2")
            print("Argument1 : Directory Name")

        else:

            DirectoryName = sys.argv[1]

            directroyDuplicatesRemovel(DirectoryName)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")    
      
    print(Border)
    print("---------Thank you for using our script--------")
    print("Delete duplicate file from directroy Automation")
    print(Border)

if(__name__ == "__main__"):
    main()