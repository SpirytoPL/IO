import telnetlib
import socket
import tftpy
import pyAesCrypt


######################################  TFTP  Server  ###########################################################
MAXSIZE = 500
PORT = 69

def TFTP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = input("Enter server IP adrress: ")     #get data from user
    s.bind((ip_address, PORT))
    print ("listening on {}".format(PORT))

    while True:
    	data, addr = s.recvfrom(MAXSIZE)
    	print( "{} from {}".format(data, addr))
    	s.sendto("Hello, {}".format(addr), addr)

'''       
def tftp():
    server = tftpy.TftpServer('/tftpboot')
    ip_address = input("Enter server IP adrress: ")
    server.listen(ip_address, 69)'''
######################################  Crypto Module  ###########################################################
def Crypto():
    db_passord = input("Database password: ")
    db_plain = pyAesCrypt.decryptFile(r"PATH", r"PATH", main_password, bufferSize)
    db_read = open(r"PATH_TO_DEVICE_LIST", "r")
    db_cipher = pyAesCrypt.encryptFile(r"PATH", r"PATH", main_password, bufferSize)

    for line in file:
        x = line.split(",")
        ip.append(x[0])
        login.append(x[1])
        password.append(x[2])
        switch_os.append(x[3])
        counter = counter + 1
    file.close()
######################################  Backup Telnet Module  ###########################################################
def Backup_Telnet():
    dasd

######################################  Backup SSH Module  ###########################################################
def Backup_SSH():
    dasd

############################################    MAIN    #######################################################
if __name__ == "__main__":
	TFTP()