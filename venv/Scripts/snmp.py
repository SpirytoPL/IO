#Pragma Once
from pysnmp.entity.rfc3413.oneliner import cmdgen

def SNMP_Get_Next(IP, OID, community):
    print("IP Address: "+str(IP))
    print(OID)
    errorIndication, errorStatus, errorIndex, \
    varBindTable = cmdgen.CommandGenerator().Cmd(
                cmdgen.CommunityData(str(community)),
                cmdgen.UdpTransportTarget((str(IP), 161)),
                (OID),
            )
    if errorIndication:
        print( errorIndication)
    else:
        if errorStatus:
            print ('%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                ))
            droped.write('%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                ) + "\n")
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    print ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

def SNMP_Get_Bulk(IP, OID, community):
    print("IP Address: "+str(IP))
    errorIndication, errorStatus, errorIndex, \
    varBindTable = cmdgen.CommandGenerator().bulkCmd(
                cmdgen.CommunityData(str(community)),
                cmdgen.UdpTransportTarget((str(IP), 161)),
                0,
                25,
                (OID),
            )
    if errorIndication:
        print( errorIndication)
    else:
        if errorStatus:
            print ('%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                ))
            droped.write('%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                ) + "\n")
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    print ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
