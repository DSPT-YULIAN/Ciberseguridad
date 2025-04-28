Ciberseguridad


Análisis de vulnerabilidades

Fase de reconomiento con Nmap

1. Hacer ping al destino de ataque (host)
2. Identifique los puertos y servicios abiertos. nmap -sV (host)
3. Identificar el sistema operativo  sudo nmap -O (host) OS details
4. Utilice el guion de Nmap Vulners para buscar vulnerabilidades. nmap -sV --script vulners --script-args mincvss=4 (host)