#Pragma Once
import telnetlib

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

def Configuration_Template():
    print("Configuration_Template")