
import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

def CreateLog(FolderName, RecEmailId):
    Border = "-"*50
    Ret = False
    Ret = os.path.exists(FolderName)

    if(Ret):
        Ret = os.path.isdir(FolderName)
        if(not Ret):
            print("Unable to create folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"PlatformSurveillance_%s.log" %timestamp)
    # print("Log file gets creted with name : ", FileName)
    
    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous platform surveillance system ----\n")
    fobj.write("Log created at : "+ time.ctime() + "\n")
    fobj.write(Border+"\n\n")
    
    fobj.write("------------------ System Report -----------------\n")
    # print("CPU Usage : ", psutil.cpu_percent())
    fobj.write("CPU Usage :  %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    # print("RAM Usage : ", mem.percent)
    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisc usages report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            Usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} Used {Usage.percent}%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, Usage.percent))
        except:
            pass
    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process Log
    Data = ProcessScan()
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("UserName : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("StartTime : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write("RAM Used in MB : %s\n" %info.get("RAM_Used"))
        fobj.write("No. of Threade created by process : %s\n" %info.get("Thread_Count"))
        fobj.write("No. of Files open by process : %s\n" %info.get("Files_Open"))
        fobj.write("Vartual Memory Used in MB : %s\n" %info.get("Vartual_Memory"))
        fobj.write("Timestamp : %s\n" %time.strftime("%Y-%m-%d_%H-%M-%S"))
        fobj.write(Border+"\n")

    TopCPU_Use = sorted(Data, key = lambda x : x["cpu_percent"], reverse = True)[:1]
    fobj.write(Border+"\n")
    fobj.write("Top CPU usage process : \n")
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    for CPU_Use in TopCPU_Use:
        fobj.write("PID : %s\n" %CPU_Use.get("pid"))
        fobj.write("Name : %s\n" %CPU_Use.get("name"))
        fobj.write("UserName : %s\n" %CPU_Use.get("username"))
        fobj.write("Status : %s\n" %CPU_Use.get("status"))
        fobj.write("StartTime : %s\n" %CPU_Use.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %CPU_Use.get("cpu_percent"))
        fobj.write("Timestamp : %s\n" %time.strftime("%Y-%m-%d_%H-%M-%S"))
        fobj.write(Border+"\n")

    TopMemory_Use = sorted(Data, key = lambda x : x["memory_percent"], reverse = True)[:1]
    fobj.write(Border+"\n")
    fobj.write("Top Memory usage process : \n")
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    for Memory_Use in TopMemory_Use:
        fobj.write("PID : %s\n" %Memory_Use.get("pid"))
        fobj.write("Name : %s\n" %Memory_Use.get("name"))
        fobj.write("UserName : %s\n" %Memory_Use.get("username"))
        fobj.write("Status : %s\n" %Memory_Use.get("status"))
        fobj.write("StartTime : %s\n" %Memory_Use.get("create_time"))
        fobj.write("Memory %% : %.2f\n" %Memory_Use.get("memory_percent"))
        fobj.write("Timestamp : %s\n" %time.strftime("%Y-%m-%d_%H-%M-%S"))
        fobj.write(Border+"\n")

    TopThread_Use = sorted(Data, key = lambda x : x["Thread_Count"], reverse = True)[:1]
    fobj.write(Border+"\n")
    fobj.write("Top Thread count process : \n")
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    for Thread_Use in TopThread_Use:
        fobj.write("PID : %s\n" %Thread_Use.get("pid"))
        fobj.write("Name : %s\n" %Thread_Use.get("name"))
        fobj.write("UserName : %s\n" %Thread_Use.get("username"))
        fobj.write("Status : %s\n" %Thread_Use.get("status"))
        fobj.write("StartTime : %s\n" %Thread_Use.get("create_time"))
        fobj.write("No. of Threade created by process : %s\n" %Thread_Use.get("Thread_Count"))
        fobj.write("Timestamp : %s\n" %time.strftime("%Y-%m-%d_%H-%M-%S"))
        fobj.write(Border+"\n")

    TopFileOpen_Process = sorted(Data, key = lambda x : x["Files_Open"], reverse = True)[:1]
    fobj.write(Border+"\n")
    fobj.write("Top Open Files process : \n")
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    for FilesOpen_Count in TopFileOpen_Process:
        fobj.write("PID : %s\n" %FilesOpen_Count.get("pid"))
        fobj.write("Name : %s\n" %FilesOpen_Count.get("name"))
        fobj.write("UserName : %s\n" %FilesOpen_Count.get("username"))
        fobj.write("Status : %s\n" %FilesOpen_Count.get("status"))
        fobj.write("StartTime : %s\n" %FilesOpen_Count.get("create_time"))
        fobj.write("No. of Files open by process : %s\n" %info.get("Files_Open"))
        fobj.write("Timestamp : %s\n" %time.strftime("%Y-%m-%d_%H-%M-%S"))
        fobj.write(Border+"\n")


    fobj.write(Border+"\n")
    fobj.write("----------------- End of log file ----------------\n")
    fobj.write(Border+"\n")
    fobj.close()
    sendMail(FileName, RecEmailId)
        
def ProcessScan():
    ListProcess = []

    # Warm up for CPU percent

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name","username", "status", "create_time"])
            # Convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["RAM_Used"] = (proc.memory_info().rss / (1024 * 1024))
            info["Thread_Count"] = proc.num_threads()
            info["Files_Open"] = len(proc.open_files())
            info["Vartual_Memory"] = (proc.memory_info().vms / (1024 * 1024))

            ListProcess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return ListProcess

def Marvellous_send_mail(sender, app_password, receiver, subject, FileName):

    #Step 1 : Create Email object
    msg = EmailMessage()

    #Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    #Step 3 : Add mail headers
    msg.set_content("Please find attached Platform surveillance report file.")
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

def sendMail(FileName, EmailId = "mayurlondhe724@gmail.com"):
    #Always use separate temporary/testing account
    sender_email = "mayurlondhe106@gmail.com"

    #App password generated from Google account
    app_password = "banl paer jjoa djpz"

    #Your second account enamil for testing
    revceiver_email = EmailId

    subject = "Platform Surveillance System Scan Report."


    Marvellous_send_mail(sender_email, app_password, revceiver_email, subject, FileName)

    print("Marvellous Mail Sent Successfully.")

def main():
    Border = "-"*50
    
    print(Border)
    print("----- Marvellous platform surveillance system ----")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This script is use to : ")
            print("1 : Create automatic logs")
            print("2 : Executes peroidically")
            print("3 : Sends mail with log")
            print("4 : Store infomation abut processess")
            print("5 : Store information about CPU")
            print("6 : Store information about RAm usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--u"):

            print("Use automation script as")
            print(f"{sys.argv[0]} DirectoryName RecevierEmail_Id TimeInterval")
            print("DirectoryName : Name of directory to create auto logs")
            print("RecevierEmail_Id : Email Id for sending log files")
            print("TimeInterval : The time in minutes for periodic scheduling")

        else:
            print("Unable to proceed as there is no such option.")
            print("Please use --H or --U to get more information")

    elif(len(sys.argv) == 4):
        print("Inside projects logic")
        print("Directory name : ", sys.argv[1])
        print("Email_Id :", sys.argv[2])
        print("Time interval : ", sys.argv[3])

        #Appy the scheduler 

        schedule.every(int(sys.argv[3])).minutes.do(lambda : CreateLog(sys.argv[1], sys.argv[2]))

        print("Platform surveillance system started successfully.")
        print("Directory created with name : ", sys.argv[1])
        print("Time interval in minutes : ", sys.argv[3])
        print("Press Ctrl + C to stop the execution")
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
