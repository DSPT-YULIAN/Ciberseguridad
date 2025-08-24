<p align="center">

  <img src="https://i.postimg.cc/j5knS9Sw/Pentesting.jpg" alt="Descripción de la imagen">
</p>


<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<!--h1 without bottom border-->
<div id="user-content-toc">
  <ul align="center">
    <summary><h1 style="display: inline-block">PENETRATION TESTS</h1></summary>
  </ul>
</div>



<img alt="Night Coding" src="./assets/Hand%20Wave.gif" width='40' align="left"/><h2>Reconocimiento</h2>

<!-- ## Reconocimiento -->

<p> Es el primer paso en cualquier intervención de hacking. Consiste en recopilar información sobre los sistemas o redes objetivo para comprender a 
	fondo el entorno que se pretende evaluar  </p>

</br>



<!--h1 without bottom border-->
<div id="user-content-toc">
  <ul align="left">
    <summary><h2 style="display: inline-block">Fase 1. Recomocimiento pasivo y activo</h2></summary>
  </ul>
</div>



<!--h1 without bottom border-->
<div id="user-content-toc">
  <ul align="left">
    <summary><h4 style="display: inline-block">Recomocimiento pasivo (No hay interacción directa con el objetivo)</h4></summary>
  </ul>
</div>


<p> La principal forma de lograrlo es mediante Inteligencia de Fuentes Abiertas (OSINT) , que consiste en recopilar información sobre nuestro objetivo 
	de fuentes públicas, incluido el sitio web público  </p>

</br>

###  Recopilacion de informacion: (OSINT)

</br>

<p align="center">

  <img src="https://i.postimg.cc/2yHRhJ54/categorias-osint.jpg" alt="Descripción de la imagen">
</p>


</br>

### 1. Personas

<p> • Empleados (Búsqueda en redes sociales o bases de datos públicas.)</p>
<p> • Direcciones de correo (Obtención mediante filtraciones, buscadores, herramientas como Hunter.io.)</p>


### 2. Activos

<p> • Empleados (Búsqueda en redes sociales o bases de datos públicas.)</p>
<p> • Direcciones de correo (Obtención mediante filtraciones, buscadores, herramientas como Hunter.io.)</p>


<p align="center">

  <img src="https://i.postimg.cc/c4bGJV2W/Recursos.jpg" alt="Descripción de la imagen">
</p>


### Metodos


<p><b>  • Certificados SSL:</b> Comprueba qué certificados ha solicitado la empresa para facilitar el acceso HTTPS a su sitio web. 
			¡Un excelente lugar para encontrar nombres de dominio y subdominio!</p>
		
<p><b> • Análisis del sitio web:</b> Revisar el sitio web de la empresa sin hacer nada más allá de lo que haría un usuario típico. 
			Por ejemplo, revisar su página "Sobre nosotros" está bien. Adivinar rutas aleatorias en el sitio ( mytarget.com/admin )</p>
		
<p><b> • Consultas WHOIS:</b> recuperación de información de registro de dominio.</p>
	
<p><b> • Consultas DNS:</b> recopilación de registros DNS, como registros MX, A y CNAME.</p>
	
<p><b> • Motores de búsqueda:</b> utilice motores de búsqueda para encontrar información sobre el objetivo que ya han realizado un 
			reconocimiento activo para usted.</p>
			
<p><b> • Informes disponibles públicamente:</b> análisis de informes anuales, registros judiciales, comunicados de prensa, artículos de noticias y otros documentos 
		disponibles públicamente.</b>
	
<p><b> • Redes sociales:</h3> recopilación de información de plataformas de redes sociales.</p>

</br>

### 🛠 &nbsp;Herramientas


<p><b> • Descubrimiento de dominios:</b> crt.sh, dnsdumpster, subfinder, amass</p>
<p><b> • Analizadores de Techstack:</b> Wappalyzer, BuiltWith, WhatRuns</p>
<p><b> • Escáneres de Internet:</b> Shodan, Censys, Netlas, Greynoise</p>
<p><b> • Archivos web:</b> Wayback Machine, Common Crawl</p>
<p><b> • Motores de búsqueda:</b> Google, Bing, DuckDuckGo, Brave, Yandex, Baidu</p>


</br>



<!--h1 without bottom border-->
<div id="user-content-toc">
  <ul align="left">
    <summary><h4 style="display: inline-block">Recomocimiento activo (Implica interacción directa con el objetivo)</h4></summary>
  </ul>
</div>

### 👨🏻‍💻 &nbsp; Recomocimiento activo (Implica interacción directa con el objetivo)


<p> Recopilar información interactuando directamente con el objetivo (envío de paquetes, solicitudes, etc.)  </p>


</br>

<p> • Puede ser detectado por el objetivo (deja rastro en logs).</p>
<p> • Se enfoca en descubrir sistemas, servicios abiertos, topología de red, etc.</p>

</br>

### &nbsp; Metodos

</br>


<p><b> • Barrido de ping :</b>envío de solicitudes de eco ICMP para identificar hosts activos.</p>
		
<p><b> • Escaneo de puertos:</b> uso de herramientas para escanear la infraestructura de destino para identificar puertos abiertos/sin filtrar y los servicios 
		que se ejecutan en ellos.</p>
		
<p><b> • Tracerout:</b>Mapeo de la ruta que siguen los paquetes para llegar al destino. Esto nos ayuda a identificar otros sistemas y controles implementados, 
		lo que nos permite comprender mejor la red.</p>
	
<p><b> • Huella digital de servicio:</b>identificación de las versiones específicas de los servicios que se ejecutan en puertos abiertos.</p>
	
<p><b> • Motores de búsqueda:</b> utilice motores de búsqueda para encontrar información sobre el objetivo que ya han realizado un 
		reconocimiento activo para usted.</p>
			
<p><b> • Captura de banners:</b> captura de la respuesta inicial de los servicios para recopilar información sobre las versiones y configuraciones del software.</b>
	

</br>


### 🛠 &nbsp;Herramientas

</br>

<p><b> • Escáneres de puertos :</b> Nmap, Rustscan, Unicornscan, Masscan, Kiterunner</p>
<p><b> • Descubrimiento de red :</b> Netdiscover, SSB, SNMPwalk, ldapsearch, BloodHound</p>
<p><b> • Descubrimiento de dominios:</b> Dnsenum</p>


</br>
					
<p align="center">

  <img src="https://i.postimg.cc/kgsWrP5Q/reconocimiento-vs-enumeracion.jpg">
</p>



<img alt="Night Coding" src="./assets/Hand%20Wave.gif" width='40' align="left"/><h2>Enumeracion</h2>


### 👨🏻‍💻 &nbsp; Fase 2.Escaneo y Análisis de vulnerabilidades

<!-- ## Enumeracion -->

<p> Es el proceso de extraer información más detallada sobre los activos que descubrimos durante nuestro reconocimiento inicial.</p>


### &nbsp; Tipos de enumeracion

</br>

<p><b> • Enumeración remota:</b> Lo hacemos a distancia. Este es el tipo de enumeración que sigue a nuestro reconocimiento inicial general. Escaneo con Nmap, la consulta de 
		servicios con Netcat, o la obtención de información con SNMP.</p>

<p><b> • Enumeración local:</b> esto suele ocurrir después de la explotación, centrándose en los sistemas a los que hemos obtenido acceso y buscando datos confidenciales,
		 privilegios adicionales o formas de acceder a otros sistemas. Herramientas como PowerShell, whoami, net user, y wmic permiten extraer información valiosa.</p>
		
<p><b> • Enumeración de hots:</b> Es posible que haya encontrado sistemas específicos en el reconocimiento inicial que necesitan una exploración más detallada (remoto), 
		o es posible que ya tenga acceso a una máquina y desee explorarla para ver qué información puede obtener y cómo podría ayudar a acceder a otros sistemas (local).
		Herramientas como Fping, Masscan, y Angry IP Scanner son utilizadasSe enfoca en identificar dispositivos activos en una red. Técnicas como el ping sweep, el escaneo ARP</p>
		
<p><b> • Enumeración de servicios:</b> LTras identificar los servicios en ejecución (y sus posibles versiones) en un host, es hora de interactuar con ellos utilizando sus protocolos. 
		Si no se encontró nada interesante ni vulnerable en las fases anteriores, aquí es donde profundizamos en los detalles y donde dedicaremos la mayor parte del tiempo.</p>

<p> 	» Enumeración NetBIOS :recopilación de información sobre recursos compartidos, cuentas de usuario y servicios en redes de Windows.</p>

<p> 	» Enumeración SNMP :Extracción de información de dispositivos que utilizan el Protocolo Simple de Administración de Red (SNMP). 
     	Permite extraer configuraciones de red, interfaces, direcciones IP y procesos en ejecución.</p>
				
<p>		» Enumeración LDAP :LDAP (Protocolo Ligero de Acceso a Directorios) se utiliza para acceder y mantener servicios de información de directorio 
	 	distribuidos a través de una red IP. Permite extraer nombres de usuario, direcciones de correo electrónico, grupos, departamentos y servidores del directorio.</p>
				
<p>		» Transferencia de Zona DNS :La Transferencia de Zona DNS es un mecanismo que permite a los servidores DNS compartir información. Puede estar mal configurada, 
     	lo que permite a los atacantes recuperar archivos de zona DNS completos, que contienen información sobre el dominio y sus direcciones IP asociadas.</p>
				
<p>		» Enumeración NFS :NFS (Sistema de Archivos de Red) permite a los usuarios acceder a archivos en red como si estuvieran en sus discos locales. 
	 	La enumeración puede revelar directorios y archivos compartidos.</p>
				
<p>		» Enumeración SMB :SMB (Bloque de Mensajes del Servidor) es un protocolo para compartir archivos, impresoras y otros recursos. La enumeración puede 
    	asignarte nombres de usuario, información de servicio, archivos, carpetas, impresoras: todo lo que vale la pena compartir.</p>
				
<p>		» Enumeración HTTP :HTTP (Protocolo de Transferencia de Hipertexto), utilizado para proporcionarnos ese excelente tráfico web. Además de la versión 
     	del servicio web, la enumeración de servidores web consiste en encontrar todas las rutas (archivos y directorios) que residen en ellos.</p>

</br>

### 🛠 &nbsp;Herramientas

</br>

<p><b> • Descubrimiento de contenido :</b> Gobuster, Dirbuster, Feroxbuster</p>
<p><b> • Pruebas de aplicaciones web :</b> Burp Suite, OWASP ZAP, Nuclei</p>
<p><b> • Análisis de vulnerabilidades :</b> SQLmap, Nikto</p>
<p><b> • Enumeración del sistema operativo :</b> PEASS, enum4linux</p>
<p><b> • Marcos de reconocimiento :</b> Marcos de reconocimiento: Recon-ng, ReconFTW, rengine</p>

</br>

### 🛠 &nbsp;Herramientas recomendadas

</br>

### 🛠 &nbsp;enum4linux

</br>

<p>Enum4linux es una herramienta de enumeración para sistemas Windows que se utiliza principalmente para recopilar información sobre usuarios, grupos, recursos compartidos, políticas 
y otras configuraciones a través del protocolo SMB. Es muy útil en la fase de reconocimiento de un test de penetración para identificar posibles vectores de ataque en redes Windows.</p>


<p>&nbsp;&nbsp;&nbsp; enum4linux [host] </p>

<p>	•	Información sobre objetivos </p>
<p>	•	Enumerar grupo de trabajo/dominio</p>
<p>	•	Información sobre Nbtstat</p>
<p>	•	Comprobación de la sesión</p>
<p>	•	Obtención del SID de dominio</p>
<p>	•	Información sobre el Sistema Operativo </p>

<p align="center">

  <img src="https://i.postimg.cc/cHc90Bmb/1.png" alt="Descripción de la imagen">
</p>

<p>	•	Usuarios</p>

<p align="center">

  <img src="https://i.postimg.cc/yxQLS62h/2.png" alt="Descripción de la imagen">
</p>

<p>	•	Enumeración de acciones </p>
<p>	•	Informacion de politicas de contraseñas </p>

<p align="center">

  <img src="https://i.postimg.cc/WbzWcrJ5/3.png" alt="Descripción de la imagen">
</p>


<p>	•	Grupos </p>
<p>	•	Enumerando usuarios usando SID  y nombre de usuario '', contraseña ''</p>


<p align="center">

  <img src="https://i.postimg.cc/s2YK44tg/4.png" alt="Descripción de la imagen">
</p>



<p>opciones de uso: enum4linux -U [host]  </p>


<p> •  -U obtener lista de usuarios </p>
<p> •  -M obtener lista de máquinas </p>
<p> •  -S obtener lista compartida </p>
<p> •  -P obtener información sobre la política de contraseñas </p>
<p> •  -G obtener lista de grupos y miembros </p>
<p> •  -d ser detallado, se aplica a -U y -S </p>
<p> •  -u user especifica el nombre de usuario a utilizar (por defecto «») </p> 
<p> •  -p pass especificar la contraseña a utilizar (por defecto «») </p>
<p> •  -i obtiene una lista de impresoras</p>
<p> •  -a Combina las opciones -U, -S, -G, -P, -r, -o, -n, -i en un solo comando</p>
<p> •  -k user Usuario(s) que existe(n) en el sistema remoto</p>
<p> •  -o Obtener información del sistema operativo</p>
<p> •  -n Hacer un nmblookup (similar a nbtstat)</p>
<p> •  -v Verbose.  Muestra todos los comandos que se están ejecutando (net, rpcclient, etc.)</p>
<p> •  -A Agresivo. Realiza comprobaciones de escritura en recursos compartidos, etc.</p>


<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">



<p>Es un proceso automatizado que identifica las debilidades de seguridad conocidas en los sistemas, las redes o las aplicaciones. Estos análisis 
generan informes en los que se enumeran las posibles vulnerabilidades en función de las firmas y las configuraciones, pero no confirman si esas 
fallas pueden aprovecharse realmente.</p>



### 🛠 &nbsp;Herramientas recomendadas


### 🛠 &nbsp; Searchsploit

<p>	Es una herramienta de línea de comandos incluida en el framework Exploit-DB (Exploit Database), que permite buscar exploits y vulnerabilidades en una base de datos local.</p>

</br>

<p>	1. Realizar un escaneo de detección de versiones de servicios y aplicaciones que se ejecutan en puertos abiertos de un sistema objetivo. (nmap -sV). </p>
<p>	2. Colocar el nombre del servicio del cual se quiere buscar el exploit, teniendo en cuenta los puertos o servicios expuestos. </p>
<p> &nbsp;&nbsp;&nbsp; • searchsploit [opciones] término de búsqueda.  </p>


<p align="center">

  <img src="https://i.postimg.cc/LX4kBKtx/1.png" alt="Descripción de la imagen">
</p>


<p> 3. Descargar el exploit. </p>

<p >&nbsp;&nbsp;&nbsp; • searchsploit -m [Nombre del exploit]. </p>
<p> Exploit descargado en el directorio selecionado. </p>


<p align="center">

  <img src="https://i.postimg.cc/tgpFpQM9/3.png" alt="Descripción de la imagen">
</p>


<p> Base de datos de Exploit. </p>

<p align="center">

  <img src="https://i.postimg.cc/t4HpGqGn/5.png" alt="Descripción de la imagen">
</p>



### 👨🏻‍💻 &nbsp; NMAP



<p>&nbsp;&nbsp;&nbsp;1. Hacer ping al destino de ataque (host)</p>
<p>&nbsp;&nbsp;&nbsp;2. Identifique los puertos y servicios abiertos. nmap -sV (host)</p>
<p>&nbsp;&nbsp;&nbsp;3. Identificar el sistema operativo  sudo nmap -O (host) OS details</p>
<p>&nbsp;&nbsp;&nbsp;4. Utilice el guion de Nmap Vulners para buscar vulnerabilidades. nmap -sV --script vulners --script-args mincvss=4 (host)</p>


<p align="center">

  <img src="https://i.postimg.cc/dVvB6xKZ/1.png" alt="Descripción de la imagen">
</p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/VsCW88fb/2.png" alt="Descripción de la imagen">
</p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/MKJbZFH3/4.png" alt="Descripción de la imagen">
</p>





<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">



### 👨🏻‍💻 &nbsp; Fase 3. Explotacion


<p>&nbsp;&nbsp;<h3>Ataques de red pasivos vs. activos<h3></p>


### 👨🏻‍💻 &nbsp; Ataques pasivos


<p> implican la monitorización o interceptación del tráfico de red sin alterar ni interferir con los datos transmitidos. El objetivo principal es recopilar información sobre la red o sus usuarios </p>

<p><b>&nbsp;&nbsp;&nbsp; • Network Sniffing</b> Captura y análisis de paquetes de datos a medida que viajan a través de la red para extraer información útil. </p>
<p><b>&nbsp;&nbsp;&nbsp; • Análisis de tráfico</b> Observación de patrones y volúmenes de tráfico para inferir información sensible, como los hábitos de comunicación de 
los usuarios o la estructura de la red.</p>

<p> En los ataques pasivos, el atacante pasa desapercibido, ya que no modifica ni interrumpe el tráfico de la red, como si se espiara una conversación. 
"Cuanto más silencioso te vuelves, más puedes oír." - Ram Dass</p>


### 🛠 &nbsp;Herramientas

</br>

<p><b> • Above :</b> Identifica los protocolos en uso en una red y cualquier vulnerabilidad obvia.</p>
<p><b> • Pcredz :</b> Identifica y extrae información confidencial del tráfico de red.</p>
<p><b> • Wireshark :</b> La herramienta de rastreo y análisis de paquetes. Si no la conoces, familiarízate con ella</p>
<p><b> • tcpdump :</b> Herramienta de captura de paquetes de línea de comandos. </p>
<p><b> • Kismet  :</b> Rastreador pasivo para varias redes inalámbricas (Wi-Fi, Bluetooth, etc.).</p>



### 👨🏻‍💻 &nbsp; Ataques de red activos

</br>

### &nbsp; Tipos de ataque

</br>

<p> Implican la modificación, interrupción o manipulación deliberada del tráfico o las comunicaciones de la red para lograr objetivos maliciosos. </p>

<p><b>&nbsp;&nbsp;&nbsp;• Ataques Man-in-the-Middle (MitM)</b> : Interceptar y alterar la comunicación entre dos partes sin su conocimiento. </p>


<p align="center">

  <img src="https://i.postimg.cc/3xghnVqC/MITM.png" alt="Descripción de la imagen">
</p>




### &nbsp; 1. Técnicas de intermediario (MiTM)

<p><b>• Suplantación de DHCP :</b> envío de respuestas DHCP falsas para redirigir el tráfico de red.</p>
<p><b>• Ataque gemelo malvado :</b> configuración de un punto de acceso Wi-Fi falso para interceptar el tráfico.</p>
<p><b>• Envenenamiento de caché ARP :</b> envío de mensajes ARP falsos para vincular su dirección MAC con la dirección IP de otro host.</p>
<p><b>• Envenenamiento LLMNR/NBT-NS :</b> explotación de protocolos de red para interceptar y retransmitir tráfico de autenticación.</p>

<p> Una vez que nos hemos posicionado en el medio, podemos empezar a rastrear el tráfico en busca de información confidencial. Si el tráfico está cifrado, podemos emplear técnicas como: </p>

<p><b>• Debilitar el cifrado :</b> comprometer las capacidades de cifrado de un dispositivo de red</p>
<p><b>• Ataque de degradación: </b> aprovecha la compatibilidad con versiones anteriores de un sistema para obligarlo a utilizar una versión menos segura.</p>


### 🛠 &nbsp;Herramientas

</br>

<p><b> • SSLstrip+ :</b> Realizar ataques de degradación de HTTPS a HTTP.</p>
<p><b> • Bettercap :</b> Marco de reconocimiento y explotación de redes tanto cableadas como inalámbricas</p>
<p><b> • Ettercap :</b> </p>
<p><b> • Cain y abel :</b> </p>
<p><b> • Mitmframwork :</b> Envenenar consultas LLMNR, NBT-NS y mDNS</p>
<p><b> • Arpspoof :</b> Ataques de envenenamiento de caché ARP.</p>
<p><b> • Aircrack-ng :</b> Conjunto de herramientas para atacar redes Wi-Fi.</p>
<p><b> • Airgeddon :</b> Framework para atacar redes WiFi. Incluye ataques de gemelo malvado.</p>
<p><b> • Fluxion :</b> Ataques MiTM contra redes Wi-Fi.</p>


### &nbsp; 2. Ataques de denegación de servicio (DoS)

</b> 

<p>Saturar una red o un servicio con tráfico excesivo para que no esté disponible para usuarios legítimos.La mayoría de los ataques DoS implican inundación, 
lo que significa saturar al objetivo con solicitudes. </p>


### 👨🏻‍💻 &nbsp;Tipos

###  Basado en volumen

<p> Saturar el ancho de banda del sitio, medido en bps (bits por segundo), atacando las capas inferiores del modelo TCP/IP. </p>

<p><b> • Inundaciones ICMP :</b> envío de muchos pings.</p>
<p><b> • Inundaciones UDP :</b> envío de una gran cantidad de datos UDP.</p>
<p><b> • Red de botnet :</b> Un _botnet _es un conjunto de máquinas comprometidas que el atacante puede manipular desde un sistema de comando y control (CnC o C2) para participar en un ataque de DDoS, 
enviar correos electrónicos no deseados y realizar otras actividades ilícitas.</p>

<p>La Figura muestra cómo un atacante puede utilizar una botnet para lanzar un ataque DDoS. La botnet está compuesta por terminales de usuario comprometidos (computadoras portátiles), enrutadores 
inalámbricos domésticos y dispositivos de Internet de las cosas (IoT), como cámaras IP. </p>

<p>El atacante envía instrucciones al C2; Posteriormente, el C2 envía instrucciones a los bots dentro de la botnet para lanzar el ataque DDoS contra el servidor víctima.</p>

<p align="center">

  <img src="https://i.postimg.cc/WpWKsLz8/2.png" alt="Descripción de la imagen">
</p>

###  Basado en protocolo

<p> Consumir recursos del servidor o del nodo de red explotando las asignaciones del protocolo </p>


<p><b> • Inundaciones SYN :</b>El atacante lanza un ataque DoS directo envío de muchos paquetes SYN para dejar conexiones TCP medio abiertas y, por lo tanto, exceder los recursos del servidor, 
impidiendo conexiones de usuarios legítimos.</p>

<p align="center">

  <img src="https://i.postimg.cc/nhjfyV1q/1.png" alt="Descripción de la imagen">
</p>

<p>Ataques DoS y DDoS reflejados</p>

<p>los atacantes envían a las fuentes paquetes falsos que parecen ser de la víctima y, luego, las fuentes se vuelven participantes involuntarios en el ataque reflejado al enviar el tráfico de respuesta a la víctima prevista.</p>

<p> el atacante envía un paquete al host A. La dirección IP de origen es la dirección IP de la víctima (10.1.2.3) y la dirección IP de destino es la dirección IP del host A (10.1.1.8). Posteriormente, el host A envía un paquete 
no deseado a la víctima. Si el atacante continúa enviando este tipo de paquetes, el Host A no solo inunda a la víctima, sino que la víctima también puede responder con paquetes innecesarios, lo que consume ancho de banda y recursos</p>

<p align="center">

  <img src="https://i.postimg.cc/sxH7Z4qQ/3.png" alt="Descripción de la imagen">
</p>


<p><b> • Ataques de paquetes fragmentados : :</b>  envío de muchos paquetes fragmentados innecesariamente para llenar la cola/ventana TCP del objetivo.</p>
<p><b> • Ataques Smurf :</b> envío de solicitudes ICMP a la dirección de transmisión, lo que hace que todas las máquinas en el dominio de transmisión respondan al objetivo.</p>
<p><b> • Ataques DDoS de amplificación :</b> es una forma de ataque de DoS reflejado en el que el tráfico de respuesta (enviado por el participante involuntario) está compuesto por paquetes que son mucho más grandes que los enviados inicialmente por el atacante 
(falsificando a la víctima). Un ejemplo de este tipo de ataque es un atacante que envía consultas de DNS a un servidor DNS abierto. Luego, el servidor DNS responde con un tamaño de paquete mucho mayor que los paquetes de consulta iniciales. 
El resultado final es que la máquina de la víctima se ve inundada por paquetes grandes para los que nunca emitió consultas</p>


<p align="center">

  <img src="https://i.postimg.cc/xCC4rtvq/4.png" alt="Descripción de la imagen">
</p>

###  Basado en solicitudes

<p> Se centra en los servicios y aplicaciones de las capas superiores del modelo TCP/IP. Se mide en rps (solicitudes por segundo). </p>

<p><b> • Ataques lentos y de bajo rendimientoP :</b> Ancho de banda bajo, solicitudes lentas para saturar todos los subprocesos de la aplicación.</p>
<p><b> • Ataques DDoS de amplificación :</b> Solicitudes constantes de contenido que consumen recursos de la aplicación.</p>


### 🛠 &nbsp;Herramientas

</br>



<p><b> • Hping3 :</b> una herramienta para crear y enviar paquetes TCP/UDP personalizados y ver respuestas.</p>
<p><b> • DHCPig :</b> agota todas las direcciones en el grupo DHCP.</p>
<p><b> • SlowLoris :</b> realiza ataques DoS lentos y de baja intensidad.</p>
<p><b> • Yersinia  :</b> Un marco de ataque de capa 2.</p>


<p><b>&nbsp;&nbsp;&nbsp;• Secuestro de sesión</b>: Tomar el control de una sesión activa entre dos partes para obtener acceso no autorizado a información o servicios.</p>
<p><b>&nbsp;&nbsp;&nbsp;• Ataques de repetición</b>: Captura y retransmisión de datos válidos para crear efectos no autorizados u obtener acceso a los sistemas.</p>


### &nbsp;Vulnerabilidades y las explotaciones basados en la red


<p>	• Ataques y explotaciones basados en la resolución de nombres de Windows</p>
<p>	• Ataque de envenenamiento de caché DNS</p>
<p>	• Ataques y explotaciones contra implementaciones de Server Message Block (SMB)</p>
<p>	• Vulnerabilidades y explotaciones del Protocolo simple de administración de red (SNMP)</p>
<p>	• Vulnerabilidades y explotaciones del Protocolo simple de transferencia de correo (SMTP)</p>
<p>	• Vulnerabilidades y explotaciones del Protocolo de transferencia de archivos (FTP)</p>
<p>	• Ataques de transferencia de hash</p>
<p>	• Ataques en ruta (antes conocidos como ataques de intermediario [MITM])</p>
<p>	• Ataques de eliminación de SSL</p>
<p>	• Ataques de denegación de servicio (DoS) y de denegación de servicio distribuido (DDoS)</p>
<p>	• Omisión del control de acceso a la red (NAC)</p>
<p>	• Ataques de salto a la red de área local virtual (VLAN)</p>

### &nbsp;Ataques a redes WI-FI

### &nbsp;Ataques contra WEP

</br>

<p>	WEP es susceptible a muchos ataques diferentes, se considera un protocolo inalámbrico obsoleto. ha sido derrotado durante décadas. WEP usa RC4 de una manera que permite a un atacante 
descifrar la PSK con poco esfuerzo. El problema está relacionado con cómo WEP utiliza los IV en cada paquete. Cuando WEP usa RC4 para cifrar un paquete, anteponga el IV a la clave secreta 
antes de incluir la clave en RC4. Posteriormente, un atacante tiene los primeros 3 bytes de una clave supuestamente “secreta” utilizada en cada paquete. Para recuperar el PSK, el atacante 
solo necesita recopilar suficientes datos del aire. Un atacante puede acelerar este tipo de ataque inyectando paquetes ARP (porque la longitud es predecible), lo que permite que el atacante 
recupere el PSK mucho más rápido. Después de recuperar la clave WEP, el atacante puede usarla para acceder a la red inalámbrica.</p>

### &nbsp;Ataques contra WPA

</br>

<p>	Todas las versiones de WPA admiten diferentes métodos de autenticación, incluido PSK. WPA no es susceptible a los ataques IV que afectan a WEP; Sin embargo, es posible capturar el protocolo 
de enlace de cuatro vías WPA entre un cliente y un dispositivo de infraestructura inalámbrica y luego aplicar la fuerza bruta a la PSK de WPA.</p>

<p align="center">

  <img src="https://i.postimg.cc/DZhK6SGF/1.png" alt="Descripción de la imagen">
</p>

<p><b>&nbsp;&nbsp;&nbsp; • Paso 1. </b> Un atacante monitorea la red Wi-Fi y encuentra clientes inalámbricos conectados al SSID de la red corporativa. </p>
<p><b>&nbsp;&nbsp;&nbsp; • Paso 2. </b> El atacante envía paquetes DeAuth para desautenticar al cliente inalámbrico. </p>
<p><b>&nbsp;&nbsp;&nbsp; • Paso 3. </b> El atacante captura el protocolo de enlace de cuatro vías WPA y descifra la PSK de WPA. (Es posible usar listas de palabras y herramientas como Aircrack-ng para realizar este ataque. </p>


### &nbsp;Vulnerabilidades que afectan a WPA y WPA2

### &nbsp;&nbsp; Estas vulnerabilidades, también denominadas KRACK (ataque de reinstalación de claves ) (https://www.krackattacks.com/)



### 🛠 &nbsp;Herramientas recomendadas

### 🛠 &nbsp;Ingenieria social 

### 🛠 &nbsp; Setoolkit

### 🛠 &nbsp; BeEF


<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">



### 👨🏻‍💻 &nbsp; Fase 4. Post-Explotacion


### 🛠 &nbsp; MSFVENOM

### 🛠 &nbsp; Meterpreter

### 🛠 &nbsp; Mimikatz








