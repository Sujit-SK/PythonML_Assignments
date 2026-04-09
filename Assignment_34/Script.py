import zipfile
import sys
import os

def extractZipFile(ZipFileName, Destination):
    
    ret = False

    ret = os.path.isdir(Destination)

    if(not ret):
        os.mkdir(Destination)

    with zipfile.ZipFile(ZipFileName, "r") as zip_ref:
        zip_ref.extractall(Destination)

    print("Extraction completed!")

def hostoryOfZipFile(ZipFileName):
    
    size_bytes = os.path.getsize(ZipFileName)

    print("Zip size (MB) : ", round(size_bytes / (1024 * 1024), 2))

    counter = 0
    with zipfile.ZipFile(ZipFileName, "r") as zip_ref:
        for file in zip_ref.infolist():
            if (not file.is_dir()):
                counter = counter + 1
                

    print("Number of files : ", counter)

def main():
    Border = "-"*50
    print(Border)
    print(Border)
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This script is use to : ")
            print("Extract backup into given directory.")
            print("Displaying the history.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--u"):

            print("Use automation script as")
            print(f"{sys.argv[0]} --restore OR --history")
            print("--restore : Extract backup into given directory.")
            print("--history : Displaying the history.")

        else:
            print("Unable to proceed as there is no such option.")
            print("Please use --H or --U to get more information")
    elif(len(sys.argv) == 3):
        Zip_File = sys.argv[2]

        if(sys.argv[1] == "--history"):
            hostoryOfZipFile(Zip_File)

    elif(len(sys.argv) == 4):
        Zip_File = sys.argv[2]
        Destination = sys.argv[3]

        if(sys.argv[1] == "--restore"):
            extractZipFile(Zip_File, Destination)
            
    else:
        print("Invaild input parameters")
        print("Unable to proceed as there is no such option.")
        print("Please use --H or --U to get more information")

    print(Border)
    print("---------- Thank you for using our script --------")
    print(Border)

if(__name__ == "__main__"):
    main()