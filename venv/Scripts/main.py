import telnetlib
import socket
import tftpy
import pyAesCrypt
import pysnmp
import serial
import paramiko
import os, sys, time, datetime
import extremeos, ciscoos, threecomos, huaweios, hpos, snmp
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
    if os.system =='nt':
        os.system("notepad.exe " + File_name + ".txt")
    else:
        os.system('vi '+ File_name + ".txt")
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
            IP.append(x[0])
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
        os.remove(File_name + ".txt")
    elif int(choice) == 2:
        IP = input("IP: ")
        login = input ("login: ")
        password = input("password: ")
        TFTP_IP = input ("TFTP Server IP: ")
        switch_os = input ("Enter switch OS (Extreme/3com/HP/Cisco/Huawei): ")
        if switch_os == "Extreme":
            extremeos.Backup_Telnet(IP, login, password, TFTP_IP)
        elif switch_os == "HP":
            hpos.Backup_Telnet(IP, login, password, TFTP_IP)
        elif switch_os == "3com":
            threecomos.Backup_Telnet(IP, login, password, TFTP_IP)
        elif switch_os == "Cisco":
            ciscoos.Backup_Telnet(IP, login, password, TFTP_IP)
        elif switch_os == "Huawei":
            huaweios.Backup_Telnet(IP, login, password, TFTP_IP)
    else:
        Backup_Telnet()
    Menu()
###################################### 4) Backup SSH Module  ###########################################################
def Backup_SSH():
    print("Backup_SSH")
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
            IP.append(x[0])
            login.append(x[1])
            password.append(x[2])
            switch_os.append(x[3])
            counter = counter + 1
        file.close()
        for i in range(counter):
            if switch_os[i] == "Extreme":
                extremeos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os[i] == "HP":
                hpos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os[i] == "3com":
                threecomos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os[i] == "Cisco":
                ciscoos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os[i] == "Huawei":
                huaweios.Backup_SSH(IP,login,password,TFTP_IP)
        os.remove(File_name + ".txt")
    elif int(choice) == 2:
        IP = input("IP: ")
        login = input ("login: ")
        password = input("password: ")
        TFTP_IP = input ("TFTP Server IP: ")
        switch_os = input ("Enter switch OS (Extreme/3com/HP/Cisco/Huawei): ")
        if switch_os == "Extreme":
            extremeos.Backup_SSH(IP, login, password, TFTP_IP)
        elif switch_os == "HP":
            hpos.Backup_SSH(IP, login, password, TFTP_IP)
        elif switch_os == "3com":
            threecomos.Backup_SSH(IP, login, password, TFTP_IP)
        elif switch_os == "Cisco":
            ciscoos.Backup_SSH(IP, login, password, TFTP_IP)
        elif switch_os == "Huawei":
            huaweios.Backup_SSH(IP, login, password, TFTP_IP)
    else:
        Backup_Telnet()

    Menu()
###################################### 6) SNMP Walk Module  ###########################################################
def SNMP_Walk():
    print("SNMP_Walk")
    community = input("Enter read community string: ")

    Menu()
###################################### 7) Execute custom command  ###########################################################
def Execute_Command():
    print('''Execute_Command
    It will be executed only on one OS and on the highest possibly priviliges
    ''')
    switch_os_choosen = input("Entry specify os: ")
    command = input("Entry command to execute: ")
    choosen_connection = input('''
    1) Telnet
    2) SSH
    ''')
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
        IP.append(x[0])
        login.append(x[1])
        password.append(x[2])
        switch_os.append(x[3])
        counter = counter + 1
    if int(choosen_connection) == 1:
        for i in range(counter):
            if switch_os_choosen == switch_os[i] and switch_os_choosen == "Extreme":
                extremeos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os[i] and switch_os_choosen == "HP":
                hpos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os[i] and switch_os_choosen == "3Com":
                threecomos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os[i] and switch_os_choosen == "Cisco":
                ciscoos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os[i] and switch_os_choosen == "Huawei":
                huaweios.Execute_Command_Telnet(IP,login,password,command)
    elif int(choosen_connection) == 2:
        if switch_os_choosen == switch_os[i] and switch_os_choosen == "Extreme":
            extremeos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os[i] and switch_os_choosen == "HP":
            hpos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os[i] and switch_os_choosen == "3Com":
            threecomos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os[i] and switch_os_choosen == "Cisco":
            ciscoos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os[i] and switch_os_choosen == "Huawei":
            huaweios.Execute_Command_SSH(IP, login, password, command)
    file.close()
    os.remove(File_name + ".txt")
    Menu()
###################################### 9) Ping check  ###########################################################
def Ping_Check():
    print("Ping_check")
    choice = input('''
    1) Use hosts from database
    2) Use host IP
    3) Use scope of IP
    ''')
    if int(choice) == 1:
        File_name = input("Entry database name: ")
        f = open(File_name + ".txt")
        IP = []
        for line in file:
            x = line.split(",")
            IP.append(x[0])
        for i in IP:
            if os.name == 'nt':
                response = os.system("ping -n 1 " + i)
            else:
                response = os.system("ping -c 1 " + i )
            time.sleep(1)

    elif int(choice) == 2:
        IP = input("Entry host IP: ")
        if os.name == 'nt':
            response = os.system("ping -n 1 " + IP )
        else:
            response = os.system("ping -c 1 " + IP )
        time.sleep(3)
    elif int(choice) == 3:
        network = input("Entry netowrk to ping: ")
        mask = input("Entry mask (24-32): ")
        mask = 32 - int(mask)
        for i in range (2**mask-1):
            if os.name == 'nt':
                response = os.system("ping -n 1 " + network + 1 + i)
            else:
                response = os.system("ping -c 1 " + network + 1 + i)
            time.sleep(1)
    else:
        Ping_Check()
    Menu()
###################################### 10) Restor configuration  ###########################################################
def Restore_Configuration():
    print("Restore_Configuration")

    Menu()
###################################### 11) Configuration Template  ###########################################################
def Configuration_Template():
    print("Configuration Template - console connection")
    switch_os = input("Entry os to configuration: ")
    com = input("Entry COMX name: ")
    ser = serial.Serial(
        port=str(com),  # COM is on windows, linux is different
        baudrate=9600,  # many different baudrates are available
        parity='N',  # no idea
        stopbits=1,
        bytesize=8,
        timeout=8  # 8 seconds seems to be a good timeout, may need to be increased
    )
    ser.isOpen()
    ser.flushInput()
    if switch_os == "Extreme":
        extremeos.Configuration_Template()
    elif switch_os == "HP":
        hpos.Configuration_Template()
    elif switch_os == "3com":
        threecomos.Configuration_Template()
    elif switch_os == "Cisco":
        ciscoos.Configuration_Template()
    elif switch_os == "Huawei":
        huaweios.Configuration_Template()
    Menu()

###################################### 12) SNMP Get Module  ###########################################################
def SNMP_Get():
    print("SNMP_Get")
    community = input("Enter read community string: ")
    IP = input("Entry IP adrress: ")
    OID = input("Entry OID to get e.g. '1,3,6,1,4,1,1916,1,4,14,1,1':")
    Menu()
###################################### 13) SNMP Get Bulk Module  ###########################################################
def SNMP_Get_Bulk():
    print("SNMP_Get_Bulk")
    community = input("Enter read community string: ")

    Menu()
############################################    MENU    #######################################################
def Menu():
    choice  = input('''
    Welcome to automatization tool for network device, supported os: Extreme, HP, 3com, Huawei, Cisco
    1) Create new Database
    2) Edit existing Database
    3) Do backup using telnet
    4) Do backup using SSH
    5) Start simple FTP server
    *6) SNMP walk
    7) Execute custom command
    8) Encrypt Database 
    9) Ping check
    *10) Restor configuration from backup
    *11) Basic configuration template - console
    *12) SNMP get
    *13) SNMP get bulk
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
    elif int(choice) == 9:
        Ping_Check()
    elif int(choice) == 10:
        Restore_Configuration()
    elif int(choice) == 11:
        Configuration_Template()
    else:
        Menu()
############################################    MAIN    #######################################################
Menu()

