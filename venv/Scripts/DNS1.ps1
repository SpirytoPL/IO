$w="10"
while ($w -ne "0") {
Write-Host "Choose options:"
$w = Read-Host "1 - Check domain / 0 - Back to the main menu"
switch($w)
 {      1 {
            $x ="K"; 
            while($x -eq "K")
            {
                    $domena=Read-Host "Enter the domian";
                    [string]$sAutodiscover='autodiscover.'+$domena;
                    [string]$sSIP='sip.'+$domena;
                    [string]$sSIPTLS='_sip._tls.'+$domena;
                    [string]$sSIPFederationtls='_sipfederationtls._tcp.'+$domena;
                    [string]$slyncdiscover='lyncdiscover.'+$domena;
                    [string]$senterpriseregistration='enterpriseregistration.'+$domena;
                    [string]$senterpriseenrollment='enterpriseenrollment.'+$domena
                    Resolve-DnsName -type cname -name $sAutodiscover -erroraction 'silentlycontinue';
                    Resolve-DnsName -type cname -name $sSIP -erroraction 'silentlycontinue';
                    Resolve-DnsName -type cname -name $slyncdiscover -erroraction 'silentlycontinue';
                    Resolve-DnsName -type cname -name $senterpriseregistration -erroraction 'silentlycontinue';
                    Resolve-DnsName -type cname -name $senterpriseenrollment -erroraction 'silentlycontinue';
                    Resolve-DnsName -type TXT $domena -erroraction 'silentlycontinue';
                    Resolve-DnsName -type MX $domena -erroraction 'silentlycontinue';
                    Resolve-DnsName -type SRV -name $sSIPTLS -erroraction 'silentlycontinue';
                    Resolve-DnsName -type SRV -name $sSIPFederationtls -erroraction 'silentlycontinue';
                    $z =Read-Host "Do you want to check another domain? Y/N"; 
                if($z -ne "Y"){$x="x"}
            }
            continue;
        }
    }        
}