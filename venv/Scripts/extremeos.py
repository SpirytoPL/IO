#Pragma Once
import telnetlib

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

def Configuration_Template():
    print("Configuration_Template")