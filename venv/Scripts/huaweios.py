#Pragma Once
import telnetlib, paramiko, serial, time

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
    ser.write(b'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(1)
    ser.write(b'system-view' + b'\n')
    time.sleep(1)
    ser.write(b'interface MEth0/0/0' + b'\n')
    time.sleep(1)
    ser.write(b'ip address ' + IP.encode('ascii') + b' ' + Mask.encode('ascii') + b'\n')
    time.sleep(1)
    ser.write(b'quit' + b'\n')
    time.sleep(1)
    ser.write(b'telnet server enable' + b'\n')
    time.sleep(1)
    ser.write(b'user-interface console 0' + b'\n')
    time.sleep(1)
    ser.write(b'authentication-mode password' + b'\n')
    time.sleep(1)
    ser.write(b'set authentication password cipher ' + Password.encode('ascii') + b'\n')
    time.sleep(1)


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