import telnetlib
import socket
import tftpy
import pyAesCrypt
import pysnmp
import serial
import paramiko
import os, sys, time, datetime, subprocess
import extremeos, ciscoos, threecomos, huaweios, hpos, snmp, console
import PySimpleGUI as sg

######################################  Global Variable  ###########################################################
bufferSize = 64 * 1024 #for AES

###################################### 5) TFTP  Server  ###########################################################
def TFTP():
    server = tftpy.TftpServer('')
    ip_address = input("Enter server IP adrress: ")
    print("Sever is listining...")
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
    print("Don't forget to encrypt your database!")
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
    repassword = input("Rentry DB password: ")
    if password == repassword:
        pyAesCrypt.encryptFile(File_name + ".txt", File_name + ".txt.aes", password, bufferSize)
        os.remove(File_name + ".txt")
        print("Database is encrypted")
    else:
        print("Password are not the same!")
        Encrypt_DB()
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
        for line in file:
            x = line.split(",")
            IP = x[0]
            login = x[1]
            password = x[2]
            switch_os = x[3]
            counter = counter + 1
        file.close()
        for i in range(counter):
            if switch_os == "Extreme":
                extremeos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os == "HP":
                hpos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os == "3com":
                threecomos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os == "Cisco":
                ciscoos.Backup_Telnet(IP,login,password,TFTP_IP)
            elif switch_os == "Huawei":
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
        for line in file:
            x = line.split(",")
            IP = x[0]
            login = x[1]
            password = x[2]
            switch_os = x[3]
            counter = counter + 1
        file.close()
        for i in range(counter):
            if switch_os == "Extreme":
                extremeos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os == "HP":
                hpos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os == "3com":
                threecomos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os == "Cisco":
                ciscoos.Backup_SSH(IP,login,password,TFTP_IP)
            elif switch_os == "Huawei":
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
        Backup_SSH()

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
    for line in file:
        x = line.split(",")
        IP = x[0]
        login = x[1]
        password = x[2]
        switch_os = x[3]
        counter = counter + 1
    if int(choosen_connection) == 1:
        for i in range(counter):
            if switch_os_choosen == switch_os and switch_os_choosen == "Extreme":
                extremeos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os and switch_os_choosen == "HP":
                hpos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os and switch_os_choosen == "3Com":
                threecomos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os and switch_os_choosen == "Cisco":
                ciscoos.Execute_Command_Telnet(IP,login,password,command)
            elif switch_os_choosen == switch_os and switch_os_choosen == "Huawei":
                huaweios.Execute_Command_Telnet(IP,login,password,command)
    elif int(choosen_connection) == 2:
        if switch_os_choosen == switch_os and switch_os_choosen == "Extreme":
            extremeos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os and switch_os_choosen == "HP":
            hpos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os and switch_os_choosen == "3Com":
            threecomos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os and switch_os_choosen == "Cisco":
            ciscoos.Execute_Command_SSH(IP, login, password, command)
        elif switch_os_choosen == switch_os and switch_os_choosen == "Huawei":
            huaweios.Execute_Command_SSH(IP, login, password, command)
    else:
        Execute_Command()
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
        netowrk_last = network.split('.')
        mask = input("Entry mask (24-32): ")
        mask = 32 - int(mask)
        for i in range (2**mask-1):
            if os.name == 'nt':
                response = os.system("ping -n 1 " + str(netowrk_last[0]) + '.' + str(netowrk_last[1]) + '.' + str(netowrk_last[2]) + '.' + str((int(netowrk_last[3]) + 1 + i)))
            else:
                response = os.system("ping -c 1 " +  str(netowrk_last[0]) + '.' + str(netowrk_last[1]) + '.' + str(netowrk_last[2]) + '.' + str((int(netowrk_last[3]) + 1 + i)))
            time.sleep(1)
    else:
        Ping_Check()
    Menu()
###################################### 10) Restor configuration telnet  ###########################################################
def Restore_Configuration_Telnet():
    print("Restore_Configuration")
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
        for line in file:
            x = line.split(",")
            IP = x[0]
            login = x[1]
            password = x[2]
            switch_os = x[3]
            counter = counter + 1
        file.close()
        for i in range(counter):
            config = input("Entry config file name: ")
            if switch_os == "Extreme":
                extremeos.Restore_Telnet(IP,login,password,TFTP_IP, config)
            elif switch_os == "HP":
                hpos.Restore_Telnet(IP,login,password,TFTP_IP, config)
            elif switch_os == "3com":
                threecomos.Restore_Telnet(IP,login,password,TFTP_IP, config)
            elif switch_os == "Cisco":
                ciscoos.Restore_Telnet(IP,login,password,TFTP_IP, config)
            elif switch_os == "Huawei":
                huaweios.Restore_Telnet(IP,login,password,TFTP_IP, config)
        os.remove(File_name + ".txt")
    elif int(choice) == 2:
        IP = input("IP: ")
        login = input ("login: ")
        password = input("password: ")
        TFTP_IP = input ("TFTP Server IP: ")
        switch_os = input ("Enter switch OS (Extreme/3com/HP/Cisco/Huawei): ")
        config = input("Entry config file name: ")
        if switch_os == "Extreme":
            extremeos.Restore_Telnet(IP, login, password, TFTP_IP, config)
        elif switch_os == "HP":
            hpos.Restore_Telnet(IP, login, password, TFTP_IP, config)
        elif switch_os == "3com":
            threecomos.Restore_Telnet(IP, login, password, TFTP_IP, config)
        elif switch_os == "Cisco":
            ciscoos.Restore_Telnet(IP, login, password, TFTP_IP, config)
        elif switch_os == "Huawei":
            huaweios.Restore_Telnet(IP, login, password, TFTP_IP, config)
    else:
        Restore_Telnet()

    Menu()
###################################### 11) Configuration Template  ###########################################################
def Configuration_Template_Switch():
    print("Configuration Template - console connection")
    switch_os = input("Entry os to configuration: ")

    if switch_os == "Extreme":
        extremeos.Configuration_Template_Switch()
    elif switch_os == "HP":
        hpos.Configuration_Template_Switch()
    elif switch_os == "3com":
        threecomos.Configuration_Template_Switch()
    elif switch_os == "Cisco":
        ciscoos.Configuration_Template_Switch()
    elif switch_os == "Huawei":
        huaweios.Configuration_Template_Switch()
    else:
        Configuration_Template_Switch()
    Menu()
###################################### 12) SNMP Get Module  ###########################################################
def SNMP_Get_Next():
    print("SNMP_Get")
    community = input("Enter read community string: ")
    IP = input("Entry IP adrress: ")
    OID = ""
    OID = input("Entry OID to get e.g. '1.3.6.1.2.1.2.2.1.5':")
    snmp.SNMP_Get(IP, OID, community)
    Menu()
###################################### 13) SNMP Get Bulk Module  ###########################################################
def SNMP_Get_Bulk():
    print("SNMP_Get_Bulk")
    community = input("Enter read community string: ")
    IP = input("Entry IP adrress: ")
    OID = ""
    OID = input("Entry OID to get e.g. '1.3.6.1.4.1.1916.1.4.14.1.1':")
    snmp.SNMP_Get_Bulk(IP, OID, community)
    Menu()
###################################### 14) Print database  ###########################################################
def Print_Database():
    print("Print_Database")
    File_name = input("Entry DB name: ")
    password = input("Entry DB password: ")
    pyAesCrypt.decryptFile(File_name + ".txt.aes", File_name + ".txt", password, bufferSize)
    File_name = File_name + ".txt"
    file = open(File_name)
    for line in file:
        print(line)
    file.close()
    os.remove(File_name)
    Menu()
###################################### 15) Telnet connection  ###########################################################
def Telnet_Connection():
    print("Telnet_connection")


    Menu()
###################################### 16) SSH connection  ###########################################################
def SSH_Connection():
    print("SSH_Connection")

    Menu()
###################################### 17) Restore SSH Module  ###########################################################
def Restore_SSH():
    print("Restore_SSH")
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
        for line in file:
            x = line.split(",")
            IP = x[0]
            login = x[1]
            password = x[2]
            switch_os = x[3]
            counter = counter + 1
        file.close()
        for i in range(counter):
            config = input("Entry config file name: ")
            if switch_os == "Extreme":
                extremeos.Restore_SSH(IP,login,password,TFTP_IP, config)
            elif switch_os == "HP":
                hpos.Restore_SSH(IP,login,password,TFTP_IP, config)
            elif switch_os == "3com":
                threecomos.Restore_SSH(IP,login,password,TFTP_IP, config)
            elif switch_os == "Cisco":
                ciscoos.Restore_SSH(IP,login,password,TFTP_IP, config)
            elif switch_os == "Huawei":
                huaweios.Restore_SSH(IP,login,password,TFTP_IP, config)
        os.remove(File_name + ".txt")
    elif int(choice) == 2:
        IP = input("IP: ")
        login = input ("login: ")
        password = input("password: ")
        TFTP_IP = input ("TFTP Server IP: ")
        switch_os = input ("Enter switch OS (Extreme/3com/HP/Cisco/Huawei): ")
        config = input("Entry config file name: ")
        if switch_os == "Extreme":
            extremeos.Restore_SSH(IP, login, password, TFTP_IP, config)
        elif switch_os == "HP":
            hpos.Restore_SSH(IP, login, password, TFTP_IP, config)
        elif switch_os == "3com":
            threecomos.Restore_SSH(IP, login, password, TFTP_IP, config)
        elif switch_os == "Cisco":
            ciscoos.Restore_SSH(IP, login, password, TFTP_IP, config)
        elif switch_os == "Huawei":
            huaweios.Restore_SSH(IP, login, password, TFTP_IP, config)
    else:
        Restore_SSH()

    Menu()
###################################### 18) Get DNS record  ###########################################################
def Get_DNS():
    print("Get DNS")
    print("Befor first you need to execute 'Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser' in Powershell running as administrator")
    print("Entry domain to check: ")
    p = subprocess.Popen(["powershell.exe",
                          "DNS.ps1"],
                         stdout=sys.stdout)
    try:
        p.communicate(timeout=10)
    except:
        p.kill()
    Menu()
###################################### 19) Print Netstat  ###########################################################
def Print_Netstat():
    print("Print Netstat")
    print(os.system("netstat"))
    Menu()
###################################### 20) Print tracert  ###########################################################
def Print_Tracert():
    print("Print tracert")
    IP = input("Entry IP: ")
    if os.name == 'nt':
        response = os.system("tracert " + IP)
    else:
        response = os.system("traceroute " + IP)
    Menu()
############################################    MENU    #######################################################
def Menu():
    choice  = input('''
    Welcome to automatization tool for network device, supported os: Extreme, HP, 3com, Huawei, Cisco
    * => in development    ✓ => ready to use
    1) Create new Database ✓
    2) Edit existing Database ✓
    3) Do backup using telnet ✓
    4) Do backup using SSH ✓
    5) Start simple TFTP server ✓
    *6) SNMP walk
    7) Execute custom command ✓
    8) Encrypt Database ✓
    9) Ping check ✓
    10) Restor configuration from backup - telnet ✓
    11) Basic configuration template for switch - console ✓
    12) SNMP get  ✓
    13) SNMP get bulk ✓
    14) Print database  ✓
    *15) Telnet connetion
    *16) SSH connection
    17) Restor configuration from backup - SSH ✓
    18) Get DNS record ✓
    19) Print netstat ✓
    20) Print tracert / traceroute ✓
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
        Restore_Configuration_Telnet()
    elif int(choice) == 11:
        Configuration_Template_Switch()
    elif int(choice) == 12:
        SNMP_Get_Next()
    elif int(choice) == 13:
        SNMP_Get_Bulk()
    elif int(choice) == 14:
        Print_Database()
    elif int(choice) == 15:
        Telnet_Connection()
    elif int(choice) == 16:
        SSH_Connection()
    elif int(choice) == 17:
        Restore_SSH()
    elif int(choice) == 18:
        Get_DNS()
    elif int(choice) == 19:
        Print_Netstat()
    elif int(choice) == 20:
        Print_Tracert()

    else:
        Menu()
############################################    GUI     #######################################################
'''
sg.theme('DarkAmber')
layout = [  [sg.Text('Welcome to automatization tool for network device, supported os: Extreme, HP, 3com, Huawei, Cisco')],
            [sg.Button('Create new Database')],
            [sg.Button('Edit existing Database')],
            [sg.Button('Do backup using telnet')],
            [sg.Button('Do backup using SSH')],
            [sg.Button('Start simple FTP server')],
            [sg.Button('SNMP walk')],
            [sg.Button('Execute custom command')],
            [sg.Button('Encrypt Database')],
            [sg.Button('Ping check')],
            [sg.Button('Restor configuration from backup - telnet')],
            [sg.Button('Basic configuration template for switch - console')],
            [sg.Button('SNMP get')],
            [sg.Button('SNMP get bulk')],
            [sg.Button('Print database')],
            [sg.Button('Telnet connetion')],
            [sg.Button('SSH connection')],
            [sg.Button('Restor configuration from backup - SSH')],
            [sg.Button('Get DNS record')],
            [sg.Button('Print netstat')],
            [sg.Button('Print tracert / traceroute')],
        ]

window = sg.Window('Py_Network', layout)
while True:
    choice, value = window.read()
    print(choice)
    if choice == 'Create new Database':
        Create_DB()

window.close()
'''
############################################    MAIN    #######################################################
Menu()

