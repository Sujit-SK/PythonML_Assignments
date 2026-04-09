import sys
import os
import time

def directroyFileSearch(DirectoryName, Extension):
    Border = "-"*50
    timestamp = time.ctime()

    LogFileName = "DirectoryFileSearch_%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Mayur Londhe\n")
    fobj.write("This is Directroy File Search Automation\n")
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
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName,fname)

            if(fname.__contains__(Extension)):
                fobj.write(fname+"\n")
    
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")


    fobj.close()

    

def main():
    Border = "-"*40
    print(Border)
    print("---- DirectroyFileSearch Automation ----")
    print(Border)
    if(len(sys.argv) > 0):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform Display all files with that extention.")
            print("This is a automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print(f"{sys.argv[0]} Argument1 Argument2")
            print("Argument1 : Directory Name")
            print("Argument2 : Extension (.txt,.pdf etc)")

        else:

            DirectoryName = sys.argv[1]
            Extension = sys.argv[2]

            directroyFileSearch(DirectoryName, Extension)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")    
      
    print("All Files Are Search Successfully.")
    print(Border)
    print("-----Thank you for using our script-----")
    print("---- DirectroyFileSearch Automation ----")
    print(Border)

if(__name__ == "__main__"):
    main()