#Pragma Once
import telnetlib, paramiko

def Backup_Telnet(IP, login, password, TFTP_IP):
    print("Backup_Telnet")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.write(b"\n")
    tn.read_until(b"Username:")
    tn.write(login.encode('ascii') + b"\n")
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(b"conf t\n")
    time.sleep(1)
    tn.write(b"copy running-config tftp " + TFTP_IP.encode('ascii') + b" config-" + IP.encode('ascii') + b"\n")
    time.sleep(30)
    print("Done\n")


def Backup_SSH(IP, login, password, TFTP_IP):
    print("Backup SSH")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(b"copy running-config tftp " + TFTP_IP.encode('ascii') + b" config-" + IP.encode('ascii') + b"\n")
    time.sleep(30)
    print("Done\n")


def Configuration_Template():
    print("Configuration_Template")

def Execute_Command_Telnet(IP,login,password,command):
    print("Executing command on HP")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.write(b"\n")
    tn.read_until(b"Username:")
    tn.write(login.encode('ascii') + b"\n")
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(b"conf t\n")
    time.sleep(1)
    tn.write(command.encode('ascii') + b"\n")
    time.sleep(1)
    print("Done\n")

def Execute_Command_SSH(IP,login,password,command):
    print("Executing command on HP")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(command + b"\n")
    time.sleep(1)
    print("Done\n")