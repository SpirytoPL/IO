import telnetlib
import socket
import tftpy
import pyAesCrypt
import pysnmp
import os
import sys
import time
import datetime
######################################  Global Variable  ###########################################################
bufferSize = 64 * 1024 #for AES

######################################  TFTP  Server  ###########################################################
MAXSIZE = 500
PORT = 69

def TFTP():
    print("TFTP")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = input("Enter server IP adrress: ")     #get data from user
    s.bind((ip_address, PORT))
    print ("listening on {}".format(PORT))

    while True:
    	data, addr = s.recvfrom(MAXSIZE)
    	print( "{} from {}".format(data, addr))
    	s.sendto("Hello, {}".format(addr), addr)
    Menu()
'''       
def tftp():
    server = tftpy.TftpServer('/tftpboot')
    ip_address = input("Enter server IP adrress: ")
    server.listen(ip_address, 69)'''


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
######################################  Create New DB  ###########################################################
def Create_DB():
    print("Create_DB")
    print('''
    Database structure: "IP_Address,Login,Password,OS"
    192.168.1.1,admin,admin,HP
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
######################################  Edit Existing DB  ###########################################################
def Edit_DB():
    print("Edit_DB")
    File_name = input("Entry DB name: ")
    password = input("Entry DB password: ")
    pyAesCrypt.decryptFile(File_name + ".txt.aes", File_name + ".txt", password, bufferSize)
    os.system("notepad.exe " + File_name + ".txt")
    os.remove(File_name + ".txt.aes")
    print("Don't forget to encrypt database after you finish!")
    Menu()

######################################  Encrypt DB  ###########################################################
def Encrypt_DB():
    print("Encrypt_DB")
    File_name = input("Entry DB name: ")
    password = input("Entry DB password: ")
    pyAesCrypt.encryptFile(File_name + ".txt", File_name + ".txt.aes", password, bufferSize)
    os.remove(File_name + ".txt")
    print("Database is encrypted")
    Menu()
######################################  Backup Telnet Module  ###########################################################
def Backup_Telnet():
    print("Backup_Telnet")

    Menu()
######################################  Backup SSH Module  ###########################################################
def Backup_SSH():
    print("Backup_SSH")

    Menu()
######################################  SNMP Walk Module  ###########################################################
def SNMP_Walk():
    print("SNMP_Walk")

    Menu()
######################################  Execute custom command  ###########################################################
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
    elif int(choice) == 7:
        Encrypt_DB()
############################################    MAIN    #######################################################
Menu()


if __name__ == "__main__":
	TFTP()