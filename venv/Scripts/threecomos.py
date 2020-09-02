#Pragma Once
import telnetlib

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

def Configuration_Template():
    print("Configuration_Template")