import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def make_zip(Folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = Folder + "_" + timestamp + ".zip"

    # open the zip file

    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(Folder):
        for file in files:
            full_path = os.path.join(root, file)

            relative = os.path.relpath(full_path, Folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path, "rb")

    while(True):
        Data = fobj.read(1024)

        if(not Data):
            break
        else:
            hobj.update(Data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    Copied_files = []
    print("Creating the backup folder for backup process")

    os.makedirs(Destination, exist_ok= True)

    for root, dire, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok= True)

            # copy the files if its new
            if((not os.path.exists(dest_path) or calculate_hash(src_path) != calculate_hash(dest_path))):

                shutil.copy2(src_path, dest_path)
                Copied_files.append(relative)
            else:
                pass
    
    return Copied_files


def MarvellousDataSchieldStart(Source = "Data"):
    Border = "-"*50
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = "DataShield_%s.log" %timestamp
    BackupName = "MarvellousBackup"

    fobj = open(FileName,"w")
    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Data shield system ----\n")
    fobj.write("Log created at : "+ time.ctime() + "\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write(f"Backup process started successfully at : {time.ctime()} \n")
    fobj.write(Border+"\n")

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    fobj.write(Border+"\n")
    fobj.write("Backup completed successfully\n")
    fobj.write(f"Files copied : {len(files)} \n")
    fobj.write(f"Zip file gets created : {zip_file} \n")
    fobj.write(Border+"\n")

    fobj.close()
    sendMail(FileName, zip_file)

def Marvellous_send_mail(sender, app_password, receiver, subject, FileName, Zip_File_Name):

    #Step 1 : Create Email object
    msg = EmailMessage()

    #Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    #Step 3 : Add mail headers
    msg.set_content(f"Please find attached DataShield Log file \n and Backup zip file is created {Zip_File_Name}.")
    filename = os.path.basename(FileName)

    with open(FileName, "rb") as f:
        msg.add_attachment(f.read(),
                        maintype="text",
                        subtype="plain",
                        filename=filename)

    #Step 4 : Create SMPT SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    #Step 5 : Login Using Gmail + App Password
    smtp.login(sender, app_password)

    #Step 6 : Send the email
    smtp.send_message(msg)

    #Step 7 : Close connection manually

    smtp.quit()

def sendMail(FileName, Zip_File_Name, EmailId = "mayurlondhe724@gmail.com"):
    #Always use separate temporary/testing account
    sender_email = "mayurlondhe106@gmail.com"

    #App password generated from Google account
    app_password = "banl paer jjoa djpz"

    #Your second account enamil for testing
    revceiver_email = EmailId

    subject = "Data Schield System Log File."


    Marvellous_send_mail(sender_email, app_password, revceiver_email, subject, FileName, Zip_File_Name)

    print("Marvellous Mail Sent Successfully.")


def main():
    Border = "-"*50
    
    print(Border)
    print("--------- Marvellous Data Shield System ---------")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This script is use to : ")
            print("1 : Tekes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create and achive of backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--u"):

            print("Use automation script as")
            print(f"{sys.argv[0]} TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directroy to backed up")

        else:
            print("Unable to proceed as there is no such option.")
            print("Please use --H or --U to get more information")

    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])

        #Appy the scheduler 

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataSchieldStart, sys.argv[2])
        
        print(Border)
        print("Data schiled system started successfully.")
        print("Time interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        #Wait till abort
        while(True):
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invaild input parameters")
        print("Unable to proceed as there is no such option.")
        print("Please use --H or --U to get more information")

    print(Border)
    print("---------- Thank you for using our script --------")
    print(Border)

if(__name__ == "__main__"):
    main()
