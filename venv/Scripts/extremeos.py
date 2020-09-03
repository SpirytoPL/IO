#Pragma Once
import telnetlib, paramiko

def Backup_Telnet(IP, login, password, TFTP_IP):
    print("Backup_Telnet")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.read_until(b"login:")
    tn.write(login.encode('ascii') + b"\n")
    tn.read_until(b"password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(b"tftp put " + TFTP_IP.encode('ascii') + b" primary.cfg config-" + IP.encode('ascii') + b"\n")
    time.sleep(30)
    print("Done\n")

def Backup_SSH(IP, login, password, TFTP_IP):
    print("Backup SSH")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(b"tftp put " + TFTP_IP.encode('ascii') + b" primary.cfg config-" + IP.encode('ascii') + b"\n")
    time.sleep(30)
    print("Done\n")

def Configuration_Template():
    print("Configuration_Template")

def Execute_Command_Telnet(IP,login,password,command):
    print("Executing command on EXOS")
    tn = telnetlib.Telnet(IP)
    time.sleep(1)
    tn.read_until(b"login:")
    tn.write(login.encode('ascii') + b"\n")
    tn.read_until(b"password:")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(command.encode('ascii') + b"\n")
    time.sleep(1)
    print("Done")

def Execute_Command_SSH(IP,login,password,command):
    print("Executing command on EXOS")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=login, password=password)
    time.sleep(1)
    ssh.exec_command(command + b"\n")
    time.sleep(1)
    print("Done\n")