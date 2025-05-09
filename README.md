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

### 👨🏻‍💻 &nbsp; Fase 1. Recomocimiento pasivo (No hay interacción directa con el objetivo)

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


### 🛠 &nbsp;Herramientas


<p><b> • Descubrimiento de dominios:</b> crt.sh, dnsdumpster, subfinder, amass</p>
<p><b> • Analizadores de Techstack:</b> Wappalyzer, BuiltWith, WhatRuns)</p>
<p><b> • Escáneres de Internet:</b> Shodan, Censys, Netlas, Greynoise</p>
<p><b> • Archivos web:</b> Wayback Machine, Common Crawl</p>
<p><b> • Motores de búsqueda:</b> Google, Bing, DuckDuckGo, Brave, Yandex, Baidu</p>
					
<p align="center">

  <img src="https://i.postimg.cc/kgsWrP5Q/reconocimiento-vs-enumeracion.jpg">
</p>


<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<img alt="Night Coding" src="./assets/Hand%20Wave.gif" width='40' align="left"/><h2>Enumeracion</h2>

<!-- ## Enumeracion -->

<p> Es el proceso de extraer información más detallada sobre los activos que descubrimos durante nuestro reconocimiento inicial.</p>


### 👨🏻‍💻 &nbsp; Fase 2. Recomocimiento activo (Implica interacción directa con el objetivo)


<p> Lo logramos pulsando (disparando paquetes) a nuestro objetivo, o pidiendo a otros que lo hagan por nosotros, y usando las respuestas para determinar 
	detalles específicos.  </p>


### 1. Activos

<p> • Infraestructura (Escaneo con herramientas como Nmap, Nessus, OpenVAS.)</p>
<p> • Dominios (Enumeración DNS con herramientas como DNSRecon o Sublist3r.)</p>


### Metodos


<p><b>  • Barrido de ping :</b> envío de solicitudes de eco ICMP para identificar hosts activos.</p>
		
<p><b> • Escaneo de puertos:</b> uso de herramientas para escanear la infraestructura de destino para identificar puertos abiertos/sin filtrar y los servicios 
		que se ejecutan en ellos.</p>
		
<p><b> • Tracerout:</b>Mapeo de la ruta que siguen los paquetes para llegar al destino. Esto nos ayuda a identificar otros sistemas y controles implementados, 
		lo que nos permite comprender mejor la red.</p>
	
<p><b> • Huella digital de servicio:</b>identificación de las versiones específicas de los servicios que se ejecutan en puertos abiertos.</p>
	
<p><b> • Motores de búsqueda:</b> utilice motores de búsqueda para encontrar información sobre el objetivo que ya han realizado un 
			reconocimiento activo para usted.</p>
			
<p><b> • Captura de banners:</b> captura de la respuesta inicial de los servicios para recopilar información sobre las versiones y configuraciones del software.</b>
	

### Tipos de enumeracion


<p><b> • Enumeración remota:</b> Lo hacemos a distancia. Este es el tipo de enumeración que sigue a nuestro reconocimiento inicial general. Escaneo con Nmap, la consulta de 
		servicios con Netcat, o la obtención de información con SNMP.</p>

<p><b> • Enumeración local:</b> esto suele ocurrir después de la explotación, centrándose en los sistemas a los que hemos obtenido acceso y buscando datos confidenciales,
		 privilegios adicionales o formas de acceder a otros sistemas. Herramientas como PowerShell, whoami, net user, y wmic permiten extraer información valiosa.</p>
		
<p><b> • Enumeración de hots:</b> Es posible que haya encontrado sistemas específicos en el reconocimiento inicial que necesitan una exploración más detallada (remoto), 
		o es posible que ya tenga acceso a una máquina y desee explorarla para ver qué información puede obtener y cómo podría ayudar a acceder a otros sistemas (local).
		Herramientas como Fping, Masscan, y Angry IP Scanner son utilizadasSe enfoca en identificar dispositivos activos en una red. Técnicas como el ping sweep, el escaneo ARP</p>
		
<p><b> • Enumeración de servicios:</b> LTras identificar los servicios en ejecución (y sus posibles versiones) en un host, es hora de interactuar con ellos utilizando sus protocolos. 
		Si no se encontró nada interesante ni vulnerable en las fases anteriores, aquí es donde profundizamos en los detalles y donde dedicaremos la mayor parte del tiempo.</p>


<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Enumeración NetBIOS :recopilación de información sobre recursos compartidos, cuentas de usuario y servicios en redes de Windows.</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Enumeración SNMP :Extracción de información de dispositivos que utilizan el Protocolo Simple de Administración de Red (SNMP). 
												 Permite extraer configuraciones de red, interfaces, direcciones IP y procesos en ejecución.</p>
				
<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Enumeración LDAP :LDAP (Protocolo Ligero de Acceso a Directorios) se utiliza para acceder y mantener servicios de información de directorio 
												 distribuidos a través de una red IP. Permite extraer nombres de usuario, direcciones de correo electrónico, grupos, departamentos y servidores 
												 del directorio.</p>
				
<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Transferencia de Zona DNS :La Transferencia de Zona DNS es un mecanismo que permite a los servidores DNS compartir información. Puede estar mal configurada, 
												 lo que permite a los atacantes recuperar archivos de zona DNS completos, que contienen información sobre el dominio y sus direcciones IP asociadas.</p>
				
<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Enumeración NFS :NFS (Sistema de Archivos de Red) permite a los usuarios acceder a archivos en red como si estuvieran en sus discos locales. 
												 La enumeración puede revelar directorios y archivos compartidos.</p>
				
<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Enumeración SMB :SMB (Bloque de Mensajes del Servidor) es un protocolo para compartir archivos, impresoras y otros recursos. La enumeración puede 
												asignarte nombres de usuario, información de servicio, archivos, carpetas, impresoras: todo lo que vale la pena compartir.</p>
				
<p>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp• Enumeración HTTP :HTTP (Protocolo de Transferencia de Hipertexto), utilizado para proporcionarnos ese excelente tráfico web. Además de la versión 
												del servicio web, la enumeración de servidores web consiste en encontrar todas las rutas (archivos y directorios) que residen en ellos.</p>


### 🛠 &nbsp;Herramientas



<p><b> • Escáneres de puertos :</b> Nmap, Rustscan, Unicornscan, Masscan, Kiterunner</p>
<p><b> • Descubrimiento de red :</b> Netdiscover, SSB, SNMPwalk, ldapsearch, BloodHound</p>
<p><b> • Descubrimiento de dominios:</b> Dnsenum</p>
<p><b> • Descubrimiento de contenido :</b> Gobuster, Dirbuster, Feroxbuster</p>
<p><b> • Pruebas de aplicaciones web :</b> Burp Suite, OWASP ZAP, Nuclei</p>
<p><b> • Análisis de vulnerabilidades :</b> SQLmap, Nikto</p>
<p><b> • Enumeración del sistema operativo :</b> PEASS, enum4linux</p>
<p><b> • Marcos de reconocimiento :</b> Marcos de reconocimiento: Recon-ng, ReconFTW, rengine</p>


### 🛠 &nbsp;Herramientas recomendadas



<p>&nbsp;&nbsp;<h3>1. enum4linux  // enum4linux -U [host]<h3></p>

<p>&nbsp;&nbsp;&nbsp;• -U busca usuarios configurados</p>
<p>&nbsp;&nbsp;&nbsp;• -S obtiene una lista de archivos compartidos</p>
<p>&nbsp;&nbsp;&nbsp;• -G obtiene una lista de los grupos y sus miembros</p>
<p>&nbsp;&nbsp;&nbsp;• -P enumera las políticas de contraseñas</p>
<p>&nbsp;&nbsp;&nbsp;• -i obtiene una lista de impresoras</p>
<p>&nbsp;&nbsp;&nbsp;• -a Combina las opciones -U, -S, -G, -P, -r, -o, -n, -i en un solo comando</p>


<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


### 👨🏻‍💻 &nbsp; Fase 3. Análisis de vulnerabilidades



### 🛠 &nbsp;Herramientas recomendadas


<p>&nbsp;&nbsp;<h3>NMAP<h3></p>


<p>&nbsp;&nbsp;&nbsp;1. Hacer ping al destino de ataque (host)</p>
<p>&nbsp;&nbsp;&nbsp;2. Identifique los puertos y servicios abiertos. nmap -sV (host)</p>
<p>&nbsp;&nbsp;&nbsp;3. Identificar el sistema operativo  sudo nmap -O (host) OS details</p>
<p>&nbsp;&nbsp;&nbsp;4. Utilice el guion de Nmap Vulners para buscar vulnerabilidades. nmap -sV --script vulners --script-args mincvss=4 (host)</p>


<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">



### 👨🏻‍💻 &nbsp; Fase 4. Explotacion


### 🛠 &nbsp;Herramientas recomendadas


<p>&nbsp;&nbsp;<h3>Searchsploit<h3></p>



![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)&nbsp;
![JavaScript](https://img.shields.io/badge/-JavaScript-05122A?style=flat&logo=javascript)&nbsp;
![Java](https://img.shields.io/badge/-Java-05122A?style=flat&logo=Java&logoColor=FFA518)&nbsp;
![C](https://img.shields.io/badge/-C-05122A?style=flat&logo=C&logoColor=A8B9CC)&nbsp;
![C++](https://img.shields.io/badge/-C++-05122A?style=flat&logo=C%2B%2B&logoColor=00599C)&nbsp;
![R (Statistics)](https://img.shields.io/badge/-R-05122A?style=flat&logo=R&logoColor=276DC3)\
![React](https://img.shields.io/badge/-React-05122A?style=flat&logo=react)&nbsp;
![Node.js](https://img.shields.io/badge/-Node.js-05122A?style=flat&logo=node.js)&nbsp;
![Django](https://img.shields.io/badge/-Django-05122A?style=flat&logo=django&logoColor=092E20)&nbsp;
![Flask](https://img.shields.io/badge/-Flask-05122A?style=flat&logo=flask)&nbsp;
![Bootstrap](https://img.shields.io/badge/-Bootstrap-05122A?style=flat&logo=bootstrap&logoColor=563D7C)\
![HTML](https://img.shields.io/badge/-HTML-05122A?style=flat&logo=HTML5)&nbsp;
![CSS](https://img.shields.io/badge/-CSS-05122A?style=flat&logo=CSS3&logoColor=1572B6)&nbsp;
![Git](https://img.shields.io/badge/-Git-05122A?style=flat&logo=git)&nbsp;
![GitHub](https://img.shields.io/badge/-GitHub-05122A?style=flat&logo=github)&nbsp;
![Markdown](https://img.shields.io/badge/-Markdown-05122A?style=flat&logo=markdown)\
![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-05122A?style=flat&logo=visual-studio-code&logoColor=007ACC)&nbsp;
![RStudio](https://img.shields.io/badge/-RStudio-05122A?style=flat&logo=rstudio)&nbsp;
![Eclipse](https://img.shields.io/badge/-Eclipse-05122A?style=flat&logo=eclipse-ide&logoColor=2C2255)\
![Illustrator](https://img.shields.io/badge/-Illustrator-05122A?style=flat&logo=adobe-illustrator)&nbsp;
![Photoshop](https://img.shields.io/badge/-Photoshop-05122A?style=flat&logo=adobe-photoshop)&nbsp;
![InDesign](https://img.shields.io/badge/-InDesign-05122A?style=flat&logo=adobe-indesign)

### ⚙️ &nbsp;GitHub Analytics

<p align="center">
<a href="https://github.com/AVS1508">
  <img height="180em" src="https://github-readme-stats-eight-theta.vercel.app/api?username=AVS1508&show_icons=true&theme=algolia&include_all_commits=true&count_private=true"/>
  <img height="180em" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=AVS1508&layout=compact&langs_count=8&theme=algolia"/>
</a>
</p>

### 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.adityavsingh.com"><img src="https://img.shields.io/badge/-adityavsingh.com-3423A6?style=flat&logo=Google-Chrome&logoColor=white"/></a>
<a href="https://linkedin.com/in/AVS1508"><img src="https://img.shields.io/badge/-Aditya%20Vikram%20Singh-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>
<a href="mailto:avsingh@umass.edu"><img src="https://img.shields.io/badge/-avsingh@umass.edu-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://instagram.com/adityavs_"><img src="https://img.shields.io/badge/-@adityavs__-E4405F?style=flat&logo=Instagram&logoColor=white"/></a>
<a href="https://facebook.com/AVS1508"><img src="https://img.shields.io/badge/-@AVS1508-1877F2?style=flat&logo=Facebook&logoColor=white"/></a>
<a href="https://www.pinterest.ca/AVS1508"><img src="https://img.shields.io/badge/-@AVS1508-BD081C?style=flat&logo=Pinterest&logoColor=white"/></a>
<a href="https://www.behance.net/AVS1508"><img src="https://img.shields.io/badge/-@AVS1508-1769FF?style=flat&logo=Behance&logoColor=white"/></a>
</p>

-----
Credits: [Aditya Vikram Singh](https://github.com/AVS1508)

Last Edited on: 11/12/2020