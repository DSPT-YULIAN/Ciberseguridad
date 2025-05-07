Pruebas de penetracion 


	Reconocimiento 

		Es el primer paso en cualquier intervención de hacking. Consiste en recopilar información sobre los sistemas o redes objetivo para comprender a 
		fondo el entorno que se pretende evaluar
	
	
	Fase 1. Recomocimiento pasivo (No hay interacción directa con el objetivo)
	
		La principal forma de lograrlo es mediante Inteligencia de Fuentes Abiertas (OSINT) , que consiste en recopilar información sobre nuestro objetivo 
		de fuentes públicas, incluido el sitio web público
	
	
		Recopilacion de informacion: (OSINT)
		
				1. Personas
				
					• Empleados (Búsqueda en redes sociales o bases de datos públicas.)
					• Direcciones de correo (Obtención mediante filtraciones, buscadores, herramientas como Hunter.io.)
					
				2. Activos
				
					• Documentacion (Revisión de archivos públicos, repositorios, informes publicados.)
					• Dominios (Identificación en registros WHOIS, búsquedas en Shodan y Osint)

	Métodos			
	
		• Certificados SSL:  Comprueba qué certificados ha solicitado la empresa para facilitar el acceso HTTPS a su sitio web. 
		¡Un excelente lugar para encontrar nombres de dominio y subdominio!
		
		• Análisis del sitio web: Revisar el sitio web de la empresa sin hacer nada más allá de lo que haría un usuario típico. 
		Por ejemplo, revisar su página "Sobre nosotros" está bien. Adivinar rutas aleatorias en el sitio ( mytarget.com/admin ).
		
		• Consultas WHOIS: recuperación de información de registro de dominio.
		
		• Consultas DNS: recopilación de registros DNS, como registros MX, A y CNAME.
		
		• Motores de búsqueda: utilice motores de búsqueda para encontrar información sobre el objetivo que ya han realizado un 
		reconocimiento activo para usted.
		
		• Informes disponibles públicamente: análisis de informes anuales, registros judiciales, comunicados de prensa, artículos de noticias y otros documentos 
		disponibles públicamente.
		
		• Redes sociales: recopilación de información de plataformas de redes sociales.



	Herramientas:	
	
	
				• Descubrimiento de dominios: crt.sh, dnsdumpster, subfinder, amass
			
				• Analizadores de Techstack: Wappalyzer, BuiltWith, WhatRuns
			
				• Escáneres de Internet: Shodan, Censys, Netlas, Greynoise
			
				• Archivos web: Wayback Machine, Common Crawl
			
				• Motores de búsqueda: Google, Bing, DuckDuckGo, Brave, Yandex, Baidu
		
				
******************************************************************************************	

	Enumeración

		Es el proceso de extraer información más detallada sobre los activos que descubrimos durante nuestro reconocimiento inicial. 


	Fase 2. Reconocimiento activo (Implica interacción directa con el objetivo)
	
	
		Lo logramos pulsando (disparando paquetes) a nuestro objetivo, o pidiendo a otros que lo hagan por nosotros, y usando las respuestas para determinar 
		detalles específicos.
	
	

		Escaneo de puertos


				1. Activos
				
					• Infraestructura (Escaneo con herramientas como Nmap, Nessus, OpenVAS.)
					• Dominios (Enumeración DNS con herramientas como DNSRecon o Sublist3r.)

	Métodos


		• Barrido de ping : envío de solicitudes de eco ICMP para identificar hosts activos.
		
		• Escaneo de puertos : uso de herramientas para escanear la infraestructura de destino para identificar puertos abiertos/sin filtrar y los servicios 
		que se ejecutan en ellos.
		
		• Traceroute : Mapeo de la ruta que siguen los paquetes para llegar al destino. Esto nos ayuda a identificar otros sistemas y controles implementados, 
		lo que nos permite comprender mejor la red.
		
		• Huella digital de servicio : identificación de las versiones específicas de los servicios que se ejecutan en puertos abiertos.
		
		• Captura de banners : captura de la respuesta inicial de los servicios para recopilar información sobre las versiones y configuraciones del software.



	Tipos de enumeracion 
	
	
		• Enumeración remota: lo hacemos a distancia. Este es el tipo de enumeración que sigue a nuestro reconocimiento inicial general. Escaneo con Nmap, la consulta de 
		servicios con Netcat, o la obtención de información con SNMP.
		
		• Enumeración local: esto suele ocurrir después de la explotación, centrándose en los sistemas a los que hemos obtenido acceso y buscando datos confidenciales,
		 privilegios adicionales o formas de acceder a otros sistemas. Herramientas como PowerShell, whoami, net user, y wmic permiten extraer información valiosa.
		 
		• Enumeración de hots: Es posible que haya encontrado sistemas específicos en el reconocimiento inicial que necesitan una exploración más detallada (remoto), 
		o es posible que ya tenga acceso a una máquina y desee explorarla para ver qué información puede obtener y cómo podría ayudar a acceder a otros sistemas (local).
		Herramientas como Fping, Masscan, y Angry IP Scanner son utilizadasSe enfoca en identificar dispositivos activos en una red. Técnicas como el ping sweep, el escaneo ARP
		
		
		
		• Enumeración de servicios: Tras identificar los servicios en ejecución (y sus posibles versiones) en un host, es hora de interactuar con ellos utilizando sus protocolos. 
		Si no se encontró nada interesante ni vulnerable en las fases anteriores, aquí es donde profundizamos en los detalles y donde dedicaremos la mayor parte del tiempo.
		
		
		
		

				• Enumeración NetBIOS : recopilación de información sobre recursos compartidos, cuentas de usuario y servicios en redes de Windows.
				
				• Enumeración SNMP : Extracción de información de dispositivos que utilizan el Protocolo Simple de Administración de Red (SNMP). 
				Permite extraer configuraciones de red, interfaces, direcciones IP y procesos en ejecución.
				
				• Enumeración LDAP : LDAP (Protocolo Ligero de Acceso a Directorios) se utiliza para acceder y mantener servicios de información de directorio 
				distribuidos a través de una red IP. Permite extraer nombres de usuario, direcciones de correo electrónico, grupos, departamentos y servidores del directorio.
				
				• Transferencia de Zona DNS : La Transferencia de Zona DNS es un mecanismo que permite a los servidores DNS compartir información. Puede estar mal configurada, 
				lo que permite a los atacantes recuperar archivos de zona DNS completos, que contienen información sobre el dominio y sus direcciones IP asociadas.
				
				• Enumeración NFS : NFS (Sistema de Archivos de Red) permite a los usuarios acceder a archivos en red como si estuvieran en sus discos locales. 
				La enumeración puede revelar directorios y archivos compartidos.
				
				• Enumeración SMB : SMB (Bloque de Mensajes del Servidor) es un protocolo para compartir archivos, impresoras y otros recursos. La enumeración puede 
				asignarte nombres de usuario, información de servicio, archivos, carpetas, impresoras: todo lo que vale la pena compartir.
				
				• Enumeración HTTP : HTTP (Protocolo de Transferencia de Hipertexto), utilizado para proporcionarnos ese excelente tráfico web. Además de la versión 
				del servicio web, la enumeración de servidores web consiste en encontrar todas las rutas (archivos y directorios) que residen en ellos.



	Herramientas:	
	

				• Escáneres de puertos: Nmap, Rustscan, Unicornscan, Masscan, Kiterunner
				
				• Descubrimiento de red: Netdiscover, SSB, SNMPwalk, ldapsearch, BloodHound
				
				• Descubrimiento de dominios: Dnsenum
				
				• Descubrimiento de contenido: Gobuster, Dirbuster, Feroxbuster
				
				• Pruebas de aplicaciones web: Burp Suite, OWASP ZAP, Nuclei
				
				• Análisis de vulnerabilidades: SQLmap, Nikto
				
				• Enumeración del sistema operativo: PEASS, enum4linux
				
				• Marcos de reconocimiento: Recon-ng, ReconFTW, rengine
			
					
	
	


				1. enum4linux  // enum4linux -U [host]
				
						-U busca usuarios configurados
						-S obtiene una lista de archivos compartidos
						-G obtiene una lista de los grupos y sus miembros
						-P enumera las políticas de contraseñas
						-i obtiene una lista de impresoras
						-a Combina las opciones -U, -S, -G, -P, -r, -o, -n, -i en un solo comando
						
						
						
		
************************************************************************************************************************	



	Fase 3. Análisis de vulnerabilidades 



Herramientas:

		NMAP
				1. Hacer ping al destino de ataque (host)
				2. Identifique los puertos y servicios abiertos. nmap -sV (host)
				3. Identificar el sistema operativo  sudo nmap -O (host) OS details
				4. Utilice el guion de Nmap Vulners para buscar vulnerabilidades. nmap -sV --script vulners --script-args mincvss=4 (host)







******************************	




	Fase 4 Explotacion 	
	
	
	
	

		2.Searchsploit







*******************************




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