
import sys
import os
import time

def directroyCopyAllFilesIntoNewDirectroy(DirectoryName, NewDirectoryName):
    Border = "-"*50
    timestamp = time.ctime()

    LogFileName = "DirectoryCopy_%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Mayur Londhe\n")
    fobj.write("This is Directroy Copy Automation\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(not Ret):
        print(f"There is no such directory ({DirectoryName}).")
        return Ret
    
    Ret = os.path.isdir(DirectoryName)

    if(not Ret):
        print("It is not directory.")
        return Ret
    
    Ret = os.path.exists(NewDirectoryName)

    if(Ret):
        print(f"Directory alredy exists ({NewDirectoryName}).")
        return Ret

    Ret = True

    os.mkdir(NewDirectoryName)

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:

            OldFileName = os.path.join(FolderName,fname)
            fobj1 = open(OldFileName,"r")

            Data = fobj1.read()

            CopyFileName = os.path.join(NewDirectoryName,fname)

            fobj1 = open(CopyFileName,"w")
            fobj1.write(Data)

            fobj.write(f"{OldFileName} File copied successfully into {CopyFileName} \n")
    
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()
    fobj1.close()

    return Ret

    

def main():
    Border = "-"*40
    print(Border)
    print("------ Directroy Copy Automation -------")
    print(Border)
    if(len(sys.argv) > 0):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform copy all files from first directory into secon directory.")
            print("This is a automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print(f"{sys.argv[0]} Argument1 Argument2")
            print("Argument1 : Directory Name")
            print("Argument2 : New Directory Name")

        else:

            DirectoryName = sys.argv[1]
            NewDirectoryName = sys.argv[2]

            Ret = directroyCopyAllFilesIntoNewDirectroy(DirectoryName, NewDirectoryName)

            if(Ret):
                print("All Files Are Copied Successfully.")
            else:
                print("Somthing went wrong.")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")    
      
    print(Border)
    print("-----Thank you for using our script-----")
    print("------ Directroy Copy Automation -------")
    print(Border)

if(__name__ == "__main__"):
    main()
