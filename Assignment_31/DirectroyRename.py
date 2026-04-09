import sys
import os
import time

def directroyFilesRename(DirectoryName, Extension, UpdatedExtension):
    Border = "-"*50
    timestamp = time.ctime()

    LogFileName = "DirectoryFilesRename_%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Mayur Londhe\n")
    fobj.write("This is Directroy File Rename Automation\n")
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
    
    FileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName,fname)

            if(fname.__contains__(Extension)):

                FileCount = FileCount + 1
                name, ext = os.path.splitext(fname)
                newExtensionName = name + UpdatedExtension

                os.rename(fname,newExtensionName)
                fobj.write(f"From {fname} To {newExtensionName}\n")
    
    if(FileCount == 0):
        fobj.write(f"There is no file with {Extension} extension\n")

    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

    

def main():
    Border = "-"*40
    print(Border)
    print("--- Directroy File Rename Automation ---")
    print(Border)
    if(len(sys.argv) > 1):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to update new extension to all old extension files.")
            print("This is a automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print(f"{sys.argv[0]} Argument1 Argument2")
            print("Argument1 : Directory Name")
            print("Argument2 : Old Extension (.txt,.pdf etc)")
            print("Argument3 : Updated Extension (.txt,.pdf etc)")

        else:

            DirectoryName = sys.argv[1]
            Extension = sys.argv[2]
            UpdateExtension = sys.argv[3]

            directroyFilesRename(DirectoryName, Extension, UpdateExtension)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")      
    print("Files Rename Successfully.")
    print(Border)
    print("-----Thank you for using our script-----")
    print("--- Directroy File Rename Automation ---")
    print(Border)

if(__name__ == "__main__"):
    main()