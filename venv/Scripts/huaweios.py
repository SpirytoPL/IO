#Pragma Once
import telnetlib, paramiko

def Backup_Telnet(IP, login, password, TFTP_IP):
    print("Backup_Telnet")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.write(b"\n")
    tn.read_until(b"Username:")
    tn.write(login.encode('ascii') + b"\n")
    time.sleep(1)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(b"tftp " + TFTP_IP.encode('ascii') + b" put vrpcfg.zip vrpcfg2.zip" + b"\n")
    time.sleep(30)
    print("Done\n")


def Backup_SSH(IP, login, password, TFTP_IP):
    print("Backup SSH")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(b"tftp " + TFTP_IP.encode('ascii') + b" put vrpcfg.zip vrpcfg2.zip" + b"\n")
    time.sleep(30)
    print("Done\n")

def Configuration_Template():
    print("Configuration_Template")

def Execute_Command_Telnet(IP,login,password,command):
    print("Executing command on Huawei")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.write(b"\n")
    tn.read_until(b"Username:")
    tn.write(login.encode('ascii') + b"\n")
    time.sleep(1)
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(b'system-view'  + b"\n")
    time.sleep(1)
    tn.write(command.encode('ascii')  + b"\n")
    time.sleep(1)
    print("Done\n")

def Execute_Command_SSH(IP,login,password,command):
    print("Executing command on Huawei")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(b"system-view" + b"\n")
    time.sleep(1)
    ssh.exec_command(command + b"\n")
    time.sleep(1)
    print("Done\n")