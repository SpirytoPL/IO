import telnetlib
import socket
import tftpy
import pyAesCrypt
import pysnmp
import os
import sys
import time
import datetime
import extremeos, ciscoos, threecomos, huaweios, hpos
######################################  Global Variable  ###########################################################
bufferSize = 64 * 1024 #for AES

###################################### 5) TFTP  Server  ###########################################################
def TFTP():
    server = tftpy.TftpServer('')
    ip_address = input("Enter server IP adrress: ")
    server.listen(ip_address, 69)


######################################  Crypto Module  ###########################################################
def Crypto():
    print("Crypto")
    db_passord = input("Database password: ")
    db_plain = pyAesCrypt.decryptFile(r"PATH", r"PATH", main_password, bufferSize)
    db_read = open(r"PATH_TO_DEVICE_LIST", "r")
    db_cipher = pyAesCrypt.encryptFile(r"PATH", r"PATH", main_password, bufferSize)

    for line in file:
        x = line.split(",")
        ip.append(x[0])
        login.append(x[1])
        password.append(x[2])
        switch_os.append(x[3])
        counter = counter + 1
    file.close()

    Menu()
###################################### 1) Create New DB  ###########################################################
def Create_DB():
    print("Create_DB")
    print('''
    Database structure: "IP_Address,Login,Password,OS"
    192.168.1.1,admin,admin,(Extreme/HP/3com/Cisco/Huawei)
    ''')
    File_name = input ("Entry name for new DB: ")
    f = open (str(File_name) + ".txt","a+")
    connection = input("Add first connection: ")
    f.write(connection + "\n")

    flag = ""
    while True:
        flag = input ("Do you wanna add another connection? (Y/N): ")
        if flag == "Y":
            connection = input("Enter new parameters:")
            f.write(connection + "\n")
        else:
            break
    f.close()
    print("Your data base will be encrypted with AES-256")
    password = input("Enter password for database: ")
    pyAesCrypt.encryptFile(File_name + ".txt", File_name + ".txt.aes", password, bufferSize)
    os.remove(File_name + ".txt")
    Menu()
###################################### 2) Edit Existing DB  ###########################################################
def Edit_DB():
    print("Edit_DB")
    File_name = input("Entry DB name: ")
    password = input("Entry DB password: ")
    pyAesCrypt.decryptFile(File_name + ".txt.aes", File_name + ".txt", password, bufferSize)
    os.system("notepad.exe " + File_name + ".txt")
    os.remove(File_name + ".txt.aes")
    print("Don't forget to encrypt database after you finish!")
    Menu()

###################################### 8) Encrypt DB  ###########################################################
def Encrypt_DB():
    print("Encrypt_DB")
    File_name = input("Entry DB name: ")
    password = input("Entry DB password: ")
    pyAesCrypt.encryptFile(File_name + ".txt", File_name + ".txt.aes", password, bufferSize)
    os.remove(File_name + ".txt")
    print("Database is encrypted")
    Menu()
###################################### 3)  Backup Telnet Module  ###########################################################
def Backup_Telnet():
    print("Backup_Telnet")
    choice  = input ('''
    1) Use existing database
    2) Custom host 
    ''')
    if int(choice) == 1:
        TFTP_IP = input("Enter TFTP Server IP: ")
        File_name = input("Entry DB name: ")
        password = input("Entry DB password: ")
        pyAesCrypt.decryptFile(File_name + ".txt.aes", File_name + ".txt", password, bufferSize)
        file = open(File_name + ".txt")
        counter = 0
        IP = []
        login = []
        password = []
        switch_os = []
        for line in file:
            x = line.split(",")
            ip.append(x[0])
            login.append(x[1])
            password.append(x[2])
            switch_os.append(x[3])
            counter = counter + 1
        file.close()
        for i in range(counter):
            if switch_os[i] == "Extreme":
                extremeos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os[i] == "HP":
                hpos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os[i] == "3com":
                threecomos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os[i] == "Cisco":
                ciscoos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os[i] == "Huawei":
                huaweios.Backup_Telnet(IP,login,password,TFTP_IP)

    elif int(choice) == 2:
        IP = input("IP: ")
        login = input ("login: ")
        password = input("password: ")
        TFTP_IP = input ("TFTP Server IP: ")
        switch_os = input ("Enter switch OS (Extreme/3com/HP/Cisco/Huawei): ")
        extremeos.Backup_EXOS_Telnet(IP, login, password, TFTP_IP)
    Menu()
###################################### 4) Backup SSH Module  ###########################################################
def Backup_SSH():
    print("Backup_SSH")

    Menu()
###################################### 6) SNMP Walk Module  ###########################################################
def SNMP_Walk():
    print("SNMP_Walk")

    Menu()
###################################### 7) Execute custom command  ###########################################################
def Execute_Command():
    print("Execute_Command")

    Menu()
############################################    MENU    #######################################################
def Menu():
    choice  = input('''
    1) Create new Database
    2) Edit existing Database
    3) Do backup using telnet
    4) Do backup using SSH
    5) Start simple FTP server
    6) SNMP walk
    7) Execute custom command
    8) Encrypt Database 
    9) Ping check
    10) Restor configuration from backup
    11) Basic configuration template - console
    Choose option:
    ''')
    if int(choice) == 1:
        Create_DB()
    elif int(choice) == 2:
        Edit_DB()
    elif int(choice) == 3:
        Backup_Telnet()
    elif int(choice) == 4:
        Backup_SSH()
    elif int(choice) == 5:
        TFTP()
    elif int(choice) == 6:
        SNMP_Walk()
    elif int(choice) == 7:
        Execute_Command()
    elif int(choice) == 8:
        Encrypt_DB()
    else:
        Menu()
############################################    MAIN    #######################################################
Menu()


if __name__ == "__main__":
	TFTP()