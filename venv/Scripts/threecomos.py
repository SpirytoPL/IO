#Pragma Once
import telnetlib, paramiko

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

def Configuration_Template():
    print("Configuration_Template")

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

def Execute_Command_SSH(IP,login,password,command):
    print("Executing command on 3Com")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(command + "\r\n")
    time.sleep(1)
    print("Done\n")