Pruebas de penetracion 

	Fase 1. Recomocimiento pasivo (No hay interacción directa con el objetivo)
	
		Recopilacion de informacion: (OSINT)
		
				1. Personas
				
					• Empleados (Búsqueda en redes sociales o bases de datos públicas.)
					• Direcciones de correo (Obtención mediante filtraciones, buscadores, herramientas como Hunter.io.)
					
				2. Activos
				
					• Documentacion (Revisión de archivos públicos, repositorios, informes publicados.)
					• Dominios (Identificación en registros WHOIS, búsquedas en Shodan y Osint)
			

******************************************************************************************	


	Fase 2. Reconocimiento activo (Implica interacción directa con el objetivo)


		Escaneo de puertos


				1. Activos
				
					• Infraestructura (Escaneo con herramientas como Nmap, Nessus, OpenVAS.)
					• Dominios (Enumeración DNS con herramientas como DNSRecon o Sublist3r.)



	Herramientas:	


		1. enum4linux  // enum4linux -U [host]
		
				-U busca usuarios configurados
				-S obtiene una lista de archivos compartidos
				-G obtiene una lista de los grupos y sus miembros
				-P enumera las políticas de contraseñas
				-i obtiene una lista de impresoras
				-a Combina las opciones -U, -S, -G, -P, -r, -o, -n, -i en un solo comando
		
******************************************************************************************	



	Fase 3. Análisis de vulnerabilidades 



Herramientas:

		NMAP
				1. Hacer ping al destino de ataque (host)
				2. Identifique los puertos y servicios abiertos. nmap -sV (host)
				3. Identificar el sistema operativo  sudo nmap -O (host) OS details
				4. Utilice el guion de Nmap Vulners para buscar vulnerabilidades. nmap -sV --script vulners --script-args mincvss=4 (host)







******************************************************************************************	




	Fase 4 Explotacion 	
	
	
	
	

		2.Searchsploit







**************************************************










