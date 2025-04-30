Ciberseguridad


Análisis de vulnerabilidades

Fase de reconomiento con Nmap

1. Hacer ping al destino de ataque (host)
2. Identifique los puertos y servicios abiertos. nmap -sV (host)
3. Identificar el sistema operativo  sudo nmap -O (host) OS details
4. Utilice el guion de Nmap Vulners para buscar vulnerabilidades. nmap -sV --script vulners --script-args mincvss=4 (host)



root@kali:/usr/share/nmap/scripts# ls -1 snmp*
snmp-brute.nse
snmp-hh3c-logins.nse
snmp-info.nse
snmp-interfaces.nse
snmp-ios-config.nse
snmp-netstat.nse
snmp-processes.nse
snmp-sysdescr.nse
snmp-win32-services.nse
snmp-win32-shares.nse
snmp-win32-software.nse
snmp-win32-users.nse
root@kali:/usr/share/nmap/scripts#
