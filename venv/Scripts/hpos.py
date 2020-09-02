#Pragma Once
import telnetlib

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

def Configuration_Template():
    print("Configuration_Template")