#Pragma Once
import telnetlib, paramiko, serial, time

def Restore_Telnet(IP, login, password, TFTP_IP, config):
    print("Restore_Telnet")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.read_until(b"Login:")
    tn.write(login.encode('ascii') + b"\r\n")
    time.sleep(0)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(b"system backupConfig restore\r\n")
    time.sleep(1)
    tn.write(TFTP_IP.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(config.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(b"\r\n")
    time.sleep(180)
    print("Done\n")
    time.sleep(1)

def Backup_Telnet(IP, login, password, TFTP_IP):
    print("Backup_Telnet")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.read_until(b"Login:")
    tn.write(login.encode('ascii') + b"\r\n")
    time.sleep(0)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(b"system backupConfig save\r\n")
    time.sleep(1)
    tn.write(TFTP_IP.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(b"config-" + IP.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(b"\r\n")
    time.sleep(180)
    print("Done\n")
    time.sleep(1)

def Restore_SSH(IP, login, password, TFTP_IP, config):
    print("Restore_SSH")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.write(b"system backupConfig restore\r\n")
    time.sleep(1)
    ssh.write(TFTP_IP.encode('ascii') + b"\r\n")
    time.sleep(1)
    ssh.write(config.encode('ascii') + b"\r\n")
    time.sleep(1)
    ssh.write(b"\r\n")
    time.sleep(180)
    print("Done\n")
    time.sleep(1)

def Backup_SSH(IP, login, password, TFTP_IP):
    print("Backup SSH")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(b"system backupConfig save\r\n")
    time.sleep(1)
    ssh.exec_command(TFTP_IP.encode('ascii') + b"\r\n")
    time.sleep(1)
    ssh.exec_command(b"config-" + IP.encode('ascii') + b"\r\n")
    time.sleep(1)
    ssh.exec_command(b"\r\n")
    time.sleep(30)
    print("Done\n")
    time.sleep(1)

def Configuration_Template_Switch():
    print("Configuration_Template")
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
    print("You need to provide same data to template: ")
    IP = input("Entry IP: ")
    Mask = input("Entry network mask: ")
    Gateway = input("Entry gateway: ")
    Password = input("Entry password: ")
    Telnet = input("Enable telnet ? Y/N: ")
    ser.write(b'\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
    time.sleep(1)


def Execute_Command_Telnet(IP,login,password,command):
    print("Executing command on 3Com")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.read_until(b"Login:")
    tn.write(login.encode('ascii') + b"\r\n")
    time.sleep(0)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\r\n")
    time.sleep(1)
    tn.write(command.encode('ascii') + b"\r\n")
    time.sleep(1)
    print("Done\n")
    time.sleep(1)

def Execute_Command_SSH(IP,login,password,command):
    print("Executing command on 3Com")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(command + "\r\n")
    time.sleep(1)
    print("Done\n")
    time.sleep(1)