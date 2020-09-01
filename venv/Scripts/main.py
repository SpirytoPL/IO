import telnetlib
import socket
import tftpy
import pyAesCrypt
import pysnmp
import os
import sys
import time
import datetime
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
######################################  Create New DB  ###########################################################
def Create_DB():
    print("Create_DB")
    print('''
    Database structure: "IP_Address,Login,Password,OS"
    192.168.1.1,admin,admin,HP
    ''')
    File_name = input ("Entry name for new DB: ")
    f = open (str("Filename")+".txt","w+")
    flag = ""
    connection = input("Add first connection: ")
    f.write(connection + "\n")
    while True:
        flag = input ("Do you wanna add another connection? (Y/N): ")
        if flag == "Y":
            connection = input("Enter new parameters:")
            f.write(connection + "\n")
        else:
            continue
    print("Your data base will be encrypted with AES-256")
    password = input("Enter password for database: ")


######################################  Backup Telnet Module  ###########################################################
def Backup_Telnet():
    print("Backup_Telnet")

######################################  Backup SSH Module  ###########################################################
def Backup_SSH():
    print("Backup_SSH")

######################################  SNMP Walk Module  ###########################################################
def SNMP_Walk():
    print("SNMP_Walk")
############################################    MENU    #######################################################
def Menu():
    print('''
    1) Create new Database
    2) Edit existing Database
    2) Do backup using telnet
    3) Do backup using SSH
    4) Set simple FTP server
    5) SNMP walk
    6) Execute custom command 
    ''')
############################################    MAIN    #######################################################
Menu()


if __name__ == "__main__":
	TFTP()