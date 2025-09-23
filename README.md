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



<!--h1 without bottom border-->
<div id="user-content-toc">
  <ul align="left">
    <summary><h2 style="display: inline-block">Fase 1. Recomocimiento pasivo y activo</h2></summary>
  </ul>
</div>


<!-- ## Reconocimiento -->

<p> Es el primer paso en cualquier intervención de hacking. Consiste en recopilar información sobre los sistemas o redes objetivo para comprender a 
	fondo el entorno que se pretende evaluar  </p>

</br>


<img alt="Night Coding" src="./assets/Hand%20Wave.gif" width='40' align="left"/><h2> 👨🏻‍💻 Recomocimiento pasivo (No hay interacción directa con el objetivo) </h2>



<p> La principal forma de lograrlo es mediante Inteligencia de Fuentes Abiertas (OSINT) , que consiste en recopilar información sobre nuestro objetivo 
	de fuentes públicas, incluido el sitio web público de la organizacion </p>

</br>

###  Recopilacion de informacion: (OSINT)

</br>

<p align="center">

  <img src="https://i.postimg.cc/2yHRhJ54/categorias-osint.jpg" alt="Descripción de la imagen">
</p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/c4bGJV2W/Recursos.jpg" alt="Descripción de la imagen">
</p>


### Metodos


<p><b>  • Certificados SSL:</b></p>
<p> Comprueba qué certificados ha solicitado la empresa para facilitar el acceso HTTPS a su sitio web. ¡Un excelente lugar para encontrar nombres de dominio y subdominio! </p>

<p><b> • Análisis del sitio web:</b></p>
<p> Revisar el sitio web de la empresa sin hacer nada más allá de lo que haría un usuario típico. Por ejemplo, revisar su página "Sobre nosotros". Adivinar rutas aleatorias en el sitio ejemplo ( mytarget.com/admin ) </p>

<p><b> • Consultas WHOIS:</b></p>
<p> Recuperación de información de registro de dominio.</p>
	
<p><b> • Consultas DNS:</b></p>
<p> Recopilación de registros DNS, como registros MX, A y CNAME.</p>
	
<p><b> • Informes disponibles públicamente:</b></p>
<p> Análisis de informes anuales, registros judiciales, comunicados de prensa, artículos de noticias y otros documentos disponibles públicamente.</b>

<p><b> • Redes sociales:</b></p>
<p> Recopilación de información de plataformas de redes sociales.</p>

</br>

### 🛠 &nbsp;Herramientas


<p><b> • Descubrimiento de dominios:</b> &nbsp; crt.sh, dnsdumpster, subfinder, amass</p>
<p><b> • Analizadores de Techstack:</b> &nbsp; Wappalyzer, BuiltWith, WhatRuns</p>
<p><b> • Escáneres de Internet:</b> &nbsp; Shodan, Censys, Netlas, Greynoise</p>
<p><b> • Archivos web:</b> &nbsp; Wayback Machine, Common Crawl</p>
<p><b> • Motores de búsqueda:</b> &nbsp; Google, Bing, DuckDuckGo, Brave, Yandex, Baidu</p>


</br>


<img alt="Night Coding" src="./assets/Hand%20Wave.gif" width='40' align="left"/><h2> 👨🏻‍💻 Recomocimiento activo (Implica interacción directa con el objetivo) </h2>


<p> Recopilar información interactuando directamente con el objetivo (envío de paquetes, solicitudes, etc.)  </p>

</br>

<p> • Puede ser detectado por el objetivo (deja rastro en logs).</p>
<p> • Se enfoca en descubrir sistemas, servicios abiertos, topología de red, etc.</p>

</br>

### &nbsp; Metodos

</br>

<p><b> • Barrido de ping :</b></p>  
<p> Envío de solicitudes de eco ICMP para identificar hosts activos.</p>
		
<p><b> • Escaneo de puertos:</b></p>
<p>	Uso de herramientas para escanear la infraestructura de destino para identificar puertos abiertos/sin filtrar y los servicios que se ejecutan en ellos.</p>
		
<p><b> • Tracerout:</b></p>
<p> Mapeo de la ruta que siguen los paquetes para llegar al destino. Esto nos ayuda a identificar otros sistemas y controles implementados, lo que nos permite comprender mejor la red.</p>
	
<p><b> • Huella digital de servicio:</b></p>
<p> Identificación de las versiones específicas de los servicios que se ejecutan en puertos abiertos.</p>
	
			
<p><b> • Captura de banners:</b></p> 
<p> Captura de la respuesta inicial de los servicios para recopilar información sobre las versiones y configuraciones del software.</b>
	

</br>


### 🛠 &nbsp;Herramientas

</br>

<p><b> • Escáneres de puertos :</b> &nbsp; Nmap, Rustscan, Unicornscan, Masscan, Kiterunner</p>
<p><b> • Descubrimiento de red :</b> &nbsp;Netdiscover, SSB, SNMPwalk, ldapsearch, BloodHound</p>
<p><b> • Descubrimiento de dominios:</b> &nbsp; Dnsenum</p>


</br>

### 🛠 &nbsp;Herramientas recomendadas

</br>

### 🛠 &nbsp;Nmap

<p> Es una herramienta esencial en pruebas de penetración para el descubrimiento de hosts y servicios en una red. </p>


<p>Reconocimiento Activo con NMAP</p>

<p>Descubrir información básica sobre los sistemas objetivo, como hosts vivos, puertos abiertos y servicios, sin profundizar en detalles específicos.</p>


<p><b> • Descubrimiento de hosts en una red :&nbsp; Detecta hosts vivos (sin escanear puertos).</b></p> 

<p> El escaneo de deteccion de host (-sn) es enviar un paquete de solicitud de eco ICMP al destino, un TCP SYN al puerto 443, un TCP ACK al puerto 80 y una solicitud de marca de tiempo ICMP. Si el objetivo responde al eco de ICMP o a los paquetes mencionados anteriormente, se considera activo. un escaneo de este tipo para la detección de host de una subred completa a veces se denomina barrido de ping.</p> 


</br>

<p align="center">

  <img src="https://i.postimg.cc/T2B41B89/5-1.png" alt="Descripción de la imagen">
</p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/wTtwd27m/5.png" alt="Descripción de la imagen">
</p>


<p><b> •Escaneo de puertos abiertos :&nbsp; El escaneo (-sS) usa un escaneo SYN para identificar puertos abiertos de manera sigilosa. Sin completar la conexión TCP </b></p> 

</br>

<p align="center">

  <img src="https://i.postimg.cc/xdy23nQn/5-2.png" alt="Descripción de la imagen">
</p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/7YRCzMPw/5-5.png" alt="Descripción de la imagen">
</p>



<p><b> Detección de sistemas operativos (-O) y servicios básicos (-sV) :&nbsp; Determina el sistema operativo y las versiones de servicios sin explotar vulnerabilidades. </b></p> 

</br>

<p align="center">

  <img src="https://i.postimg.cc/hvRZy71Y/5-3.png" alt="Descripción de la imagen">
</p>


<p><b> Evadir firewalls/IDS :&nbsp; Fragmentación de paquetes y timing lento y reducir la probabilidad de ser detectado.


<p> •T0 (Paranoico) :&nbsp; muy lento, se usa para la evasión de IDS </p> 
<p> •T1 (Furtivo) :&nbsp; bastante lento, se usa para la evasión de IDS </p> 
<p> •T2 (Educado) :&nbsp; se ralentiza para consumir menos ancho de banda, se ejecuta aproximadamente 10 veces más lento que el valor predeterminado </p> 
<p> •T3 (Normal) :&nbsp; predeterminado, un modelo de tiempo dinámico basado en la capacidad de respuesta del objetivo </p> 
<p> •T4 (Agresivo) :&nbsp; supone una red rápida y confiable y puede abrumar a los objetivos </p> 
<p> •T5 (Demente) :&nbsp; muy agresivo; probablemente abrumará a los objetivos o perderá los puertos abiertoswindows + enter abre terminal </p> 


<p align="center">

  <img src="https://i.postimg.cc/SRyCxWLC/5-4.png" alt="Descripción de la imagen">
</p>


<p><b> Escaneo de conexión TCP (-sT) :&nbsp; Utiliza el mecanismo de red del sistema operativo subyacente para establecer una conexión TCP completa con el dispositivo de destino que se está escaneando. Dado que crea una conexión completa, crea más tráfico (y, por lo tanto, tarda más en ejecutarse).</b></p> 

</br>

<p align="center">

  <img src="https://i.postimg.cc/Hs8YqGH1/5-6.png" alt="Descripción de la imagen">
</p></p>

<p><b> Escaneo UDP (-sU) :&nbsp; si se intenta enumerar un servidor DNS, SNMP o DHCP. Todos estos servicios utilizan UDP para la comunicación entre el cliente y el servidor. Para escanear puertos UDP, Nmap envía un paquete UDP a todos los puertos especificados en la configuración de la línea de comandos. Espera la respuesta del destino. Si recibe un mensaje ICMP de puerto inaccesible, ese puerto se marca como cerrado. Si no se recibe respuesta del puerto UDP de destino, Nmap lo marca como abierto/filtrado</b></p> 

<p>NOTA:&nbsp; Tenga en cuenta que los mensajes ICMP inaccesibles a veces pueden tener una velocidad limitada y, en ese caso, un escaneo de puerto UDP puede tardar mucho más. La limitación de velocidad ICMP se utiliza principalmente para limitar el comportamiento de gusanos o virus y normalmente debe configurarse para permitir que entre el 1 % y el 5 % del ancho de banda entrante disponible (a velocidades de 10 Mbps o 100 Mbps) o entre 100 kbps y 10 000 kbps (a velocidades de 1 Gbps o 10 Gbps) se utilice para el tráfico ICMP.</p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/yYTgNgWy/5-7.png" alt="Descripción de la imagen">
</p></p>

</br>

<p align="center">

  <img src="https://i.postimg.cc/DwCsyJmb/5-8.png" alt="Descripción de la imagen">
</p></p>


<p><b> Escaneo TCP FIN (-sF) :&nbsp; En ocasiones, un filtro de red o un firewall puede detectar un escaneo SYN. En tales casos, es necesario emplear un tipo de paquete diferente en un escaneo de puertos. Con el escaneo TCP FIN, se envía un paquete FIN a un puerto de destino. Si el puerto está cerrado, el sistema de destino devuelve un paquete RST. Si no se recibe nada del puerto de destino, se puede considerar abierto, ya que el comportamiento normal sería ignorar el paquete FIN.</b></p> 

<p>NOTA:&nbsp; Un escaneo TCP FIN no es útil cuando se escanean sistemas basados en Windows, ya que responden con paquetes RST, independientemente del estado del puerto.</p>

<p align="center">

  <img src="https://i.postimg.cc/wvD7J7x2/5-9.png" alt="Descripción de la imagen">
</p></p>

</br>

 <img src="https://i.postimg.cc/bw28d4wH/5-10.png" alt="Descripción de la imagen">
</p></p>


<!---------------------------------------------------------------------------------------------------------------------- ## FASE 2 ------------------------------------------------------------------------------------------------------------------------------------------------->
<!--horizontal divider(gradiant)-->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<div id="user-content-toc">
  <ul align="left">
    <summary><h2 style="display: inline-block">Fase 2.Escaneo y Análisis de vulnerabilidades </h2></summary>
  </ul>
</div>

<p align="center">

  <img src="https://i.postimg.cc/kgsWrP5Q/reconocimiento-vs-enumeracion.jpg">
</p>

<img alt="Night Coding" src="./assets/Hand%20Wave.gif" width='40' align="left"/><h2> 👨🏻‍💻 Enumeracion</h2>

<!-- ## Enumeracion -->

<p> Extracción de información detallada sobre recursos específicos: usuarios, directorios, vulnerabilidades, etc.)</p>


<p><b> • Motores de búsqueda:</b></p> 
<p> Utilice motores de búsqueda para encontrar información sobre el objetivo que ya han realizado un reconocimiento activo para usted.</p>

</br>

<p><h2> Enumeración de Servicios de Red: </h2> Su objetivo principal es descubrir qué servicios están corriendo, en qué puertos están escuchando, qué versiones de software utilizan y cómo están configurados.</p>


<p>1.  Identificar servicios vulnerables: Al conocer la versión de un servicio, se pueden buscar vulnerabilidades conocidas asociadas a esa versión.</p>
<p>2.  Determinar vectores de ataque: Por ejemplo, si un servicio como FTP o SMB está expuesto, podría ser explotado para ganar acceso inicial.</p>
<p>3.  Mapear la red: Ayuda a entender la arquitectura de la red y cómo interactúan los sistemas entre sí.</p>


<div id="user-content-toc">
  <ul align="center">
    <summary><h3 style="display: inline-block">🛠 NMAP Scripting Engine (NSE) </h3></summary>
  </ul>
</div>

 <p align="center">

 <img src="https://i.postimg.cc/4xXgh65J/NMAP.png" alt="Descripción de la imagen">

 </p>

</br>
</br>

<p> El NSE (Nmap Scripting Engine - Motor de Scripting de Nmap ) permite a los usuarios automatizar y ampliar las capacidades de Nmap mediante scripts escritos en el lenguaje de programación Lua. Estos scripts pueden realizar tareas como detección de vulnerabilidades, recolección de información, explotación de servicios y más.</p>


<p>Ejemplo de uso:&nbsp;  nmap --script (nombre_del_script) (objetivo) </p>

<h3>Categorías de scripts:(NSE)</h3>

<p>(Auth):&nbsp; Su objetivo principal es identificar configuraciones inseguras en los servicios como FTP, SSH, HTTP, SMB, etc. Tales como credenciales predeterminadas o vulnerabilidades relacionadas con la autenticación.</p>

</br>

 <img src="https://i.postimg.cc/Njyp9gD4/6.png" alt="Descripción de la imagen">

</br>


<p>(Discovery):&nbsp; Descubrimiento de hosts y servicios con mayor alcance y profundidad que un escanero comun.</p>

<p> • Descubrir hosts activos en la red (ej. con ARP, ICMP).</p>
<p> • Enumerar servicios ocultos (ej. SNMP, SMB, DNS).</p>
<p> • Recopilar metadatos (ej. sistemas operativos, dispositivos IoT, información de DNS).</p>


</br>

 <img src="https://i.postimg.cc/7YGbc6N0/6-1.png" alt="Descripción de la imagen">

</br>


 <img src="https://i.postimg.cc/wBVBJs68/6-2.png" alt="Descripción de la imagen">

</br>


 <img src="https://i.postimg.cc/CMtxj0V1/6-3.png" alt="Descripción de la imagen">

</br>


 <img src="https://i.postimg.cc/d13JyHHr/6-4.png" alt="Descripción de la imagen">

</br>
</br>

<p>(Exploit):&nbsp; Está diseñado para probar y explotar vulnerabilidades conocidas en sistemas o servicios. Su objetivo principal es verificar si un objetivo es vulnerable a un ataque específico, proporcionando una forma controlada de demostrar el riesgo</p>

</br>

 <img src="https://i.postimg.cc/L8sc8Yn0/6-5.png" alt="Descripción de la imagen">

</br>

 <img src="https://i.postimg.cc/9fRsy6Pd/6-6.png" alt="Descripción de la imagen">

</br>
</br>

<p>Ejemplo de script :&nbsp;  Exploit</p>

</br>

 <img src="https://i.postimg.cc/5Nf5hD0f/6-7.png" alt="Descripción de la imagen">

</br>
</br>

<p>(Vuln):&nbsp; Diseñado para detectar vulnerabilidades conocidas en servicios, sistemas o aplicaciones</p>

</br>

 <img src="https://i.postimg.cc/j5CGKvhj/6-8.png" alt="Descripción de la imagen">

</br>

 <img src="https://i.postimg.cc/XqCmBJmS/6-9.png" alt="Descripción de la imagen">

</br>
</br>

<p>(Brute):&nbsp; Diseñado para realizar ataques de fuerza bruta contra servicios de autenticación (como FTP, SSH, HTTP, SMB, etc.). Su objetivo es probar credenciales predeterminadas o débiles para identificar accesos no autorizados.</p>

</br>

 <img src="https://i.postimg.cc/VkGg1wZj/7.png" alt="Descripción de la imagen">

</br>
</br>

<p>Ejemplo de script :&nbsp;  Brute </p>

</br>

 <img src="https://i.postimg.cc/8CfRS66S/7-1.png" alt="Descripción de la imagen">

</br>
</br>


<p>(Safe):&nbsp; Diseñado para realizar pruebas no intrusivas y seguras en sistemas y servicios. A diferencia de los scripts vuln o brute, los scripts safe están pensados para no causar ningún daño o interrupción en los sistemas objetivo, lo que los hace ideales para:</p>


<p> • Escaneos preliminares en entornos sensibles.</p>
<p> • Auditorías de cumplimiento donde se requiere minimizar riesgos.</p>
<p> • Verificación básica de servicios sin afectar su funcionamiento.</p>

</br>

 <img src="https://i.postimg.cc/G2Y6HtZ0/7-2.png" alt="Descripción de la imagen">

</br>


<div id="user-content-toc">
  <ul align="center">
    <summary><h3 style="display: inline-block">🛠 NETCAT </h3></summary>
  </ul>
</div>


<p align="center">

 <img src="https://i.postimg.cc/G3vVJB99/netcat.png" alt="Descripción de la imagen">

 </p>

</br>


<p>Netcat (nc) es una herramienta de red versátil conocida como el "navaja suiza" de las redes. Permite leer y escribir datos en conexiones de red usando protocolos TCP o UDP. Es ampliamente utilizado en pruebas de penetración, administración de redes y debugging.</p>

<p> &nbsp; &nbsp; Nota: El trafico no esta encriptado </p>

<p> Usos comunes de NETCAT</p>

<p> <h4> 1. Depuración de redes </h4> </p>
<p>    &nbsp; &nbsp;  • Verifique si un puerto está abierto o cerrado.</p>
<p>    &nbsp; &nbsp;  • Probar servicios de red (HTTP, SMTP, etc.).</p>

<p> Syntax: nc -nv -w1 -z</p>
<p> nc -zv  [IP] [PUERTO] </p>

<h3> Comandos </h3>

<p> • -z: &nbsp; Modo de escaneo sin enviar datos, definir el rango de puertos a escanear sin establecer conexion completa </p>
<p> • -v: &nbsp; Muestra informacion detallada de la conexion  "Sin -v no mostrara si el puerto esta abierto o cerrado" </p>
<p> • -n: &nbsp; Evita la resolucion DNS (acelera el escaneo) Util cuando no se requiere resolver nombres de dominio </p>
<p> • -u  &nbsp; Escaneo UDP (por defecto NETCAT usa TCP) </p>
<p> • -w 1 &nbsp; Definir tiempo de espera para la conexion si el puerto no responde en "n" segundos pasa al siguiente </p>


<p align="center">

 <img src="https://i.postimg.cc/LXd5G1Cn/1.png" alt="Descripción de la imagen">

 </p>


<p> &nbsp; &nbsp; NETCAT  no tiene incorporada la opcion de escanear varios host por lo tanto existen dos soluciones:   </p>
<p> &nbsp;  • Bash scripts one-liner</p>
<p> &nbsp;  • Script en Phython  </p>


<p> <h4> Otros usos de NETCAT </h4> </p>

<p> 2. Transferencia de archivos : &nbsp; &nbsp;   Enviar o recibir archivos entre hosts.</p>

<p> 3. Shell remoto: Permite enviar y recibir datos en texto plano o binarios.</p>

<p> 4. Proxy y tunelización: &nbsp; &nbsp;   Redirigir el tráfico a través de un host intermedio.</p>

<p> 5. Creación de servidores simples: &nbsp; &nbsp; Servidor de chat, servidor HTTP básico, etc.</p>


<div id="user-content-toc">
  <ul align="center">
    <summary><h3 style="display: inline-block">🛠 Masscan </h3></summary>
  </ul>
</div>



<p align="center">

 <img src="https://i.postimg.cc/1RVY4YCM/masscan.png" alt="Descripción de la imagen">

 </p>


<p> MASSCAN es un escáner de puertos de alto rendimiento diseñado para escanear grandes redes (como toda Internet) en cuestión de minutos. A diferencia de Nmap, que es más preciso y detallado, Masscan se enfoca en la velocidad, utilizando un enfoque asíncrono y evitando el handshake TCP completo para lograr escaneos ultrarrápidos..</p>


<p> Syntax: masscan [IP] -p [puertos] [--argumentos] </p>



<p> Escaneo simple de puertos:</p>


<p align="center">

 <img src="https://i.postimg.cc/FFqbkrdJ/1.png" alt="Descripción de la imagen">

 </p>


<p> Escaneo de un rango de puertos:</p>


<p align="center">

 <img src="https://i.postimg.cc/t4bB7qwN/2.png" alt="Descripción de la imagen">

 </p>

<p> Escaneo rango de IPs y exclusion de IPs:</p>

<p align="center">

 <img src="https://i.postimg.cc/MpR8JpR0/3.png" alt="Descripción de la imagen">

 </p>

</br>
<p> Otros tipos de escaneo</p>
<p> Ajustar velocidad (--rate):&nbsp; masscan [IP] -p1-65535 --rate 100000 </p>
<p> Guardar resultados:&nbsp; masscan [IP] -p80 -oX resultado.xml </p>


<p>Opciones avanzadas</p>

</br>

<p align="center">

 <img src="https://i.postimg.cc/tCZKF4r0/4.png" alt="Descripción de la imagen">

 </p>

<p><h2> Enumeración de usuarios: </h2> La enumeración de usuarios es una técnica utilizada en pruebas de penetración y auditorías de seguridad para identificar nombres de usuario válidos en un sistema, aplicación o servicio. Este proceso es fundamental en las fases iniciales de un ataque, ya que permite a un atacante conocer qué cuentas existen en el sistema, lo que facilita ataques posteriores como fuerza bruta, phishing o ataques de diccionario.</p>


### 🛠 &nbsp;Herramientas

</br>

<p>• RPCClient: &nbsp; Enumerar usuarios en sistemas Windows</p>
<p>• Metasploit: &nbsp; (auxiliary modules): Módulos como smb_enumuser
<p>• enum4linux: &nbsp; Para enumerar usuarios en sistemas SMB/LDAP</p>



<div id="user-content-toc">
  <ul align="center">
    <summary><h3 style="display: inline-block">🛠 enum4linux </h3></summary>
  </ul>
</div>

</br>

<p align="center">

 <img src="https://i.postimg.cc/KjnWjJ70/5.png" alt="Descripción de la imagen">

 </p>



<p>Enum4linux es una herramienta de enumeración para sistemas Windows que se utiliza principalmente para recopilar información sobre usuarios, grupos, recursos compartidos, políticas 
y otras configuraciones a través del protocolo SMB. Es muy útil en la fase de reconocimiento de un test de penetración para identificar posibles vectores de ataque en redes Windows.</p>


<p>&nbsp;&nbsp;&nbsp; enum4linux [host] </p>

<p> • Información sobre objetivos </p>
<p> • Enumerar grupo de trabajo/dominio</p>
<p> • Información sobre Nbtstat (tablas de nombres NetBIOS)</p>
<p> • Comprobación de la sesión</p>
<p> • Obtención del SID de dominio</p>
<p> • Información sobre el Sistema Operativo </p>

<p align="center">

  <img src="https://i.postimg.cc/cHc90Bmb/1.png" alt="Descripción de la imagen">
</p>

<p> • Usuarios</p>

<p align="center">

  <img src="https://i.postimg.cc/yxQLS62h/2.png" alt="Descripción de la imagen">
</p>

<p> • Enumeración de acciones </p>
<p> • Informacion de politicas de contraseñas </p>

<p align="center">

  <img src="https://i.postimg.cc/WbzWcrJ5/3.png" alt="Descripción de la imagen">
</p>


<p> • Grupos </p>
<p> • Enumerando usuarios usando SID  y nombre de usuario '', contraseña ''</p>


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



<div id="user-content-toc">
  <ul align="center">
    <summary><h3 style="display: inline-block">🛠 Metasploit </h3></summary>
  </ul>
</div>

</br>

<p align="center">

 <img src="https://i.postimg.cc/Gm5j0V6v/1.jpg" alt="Descripción de la imagen">

 </p>


<p>En Metasploit, puedes realizar enumeración de usuarios en diferentes protocolos y servicios, como Kerberos, SMB, LDAP, HTTP, entre otros.</p>



<p> Syntax: search enumusers: &nbsp; filtrar por todos los modulos relacionados con enumeracion de usuarios</p>



<p align="center">

 <img src="https://i.postimg.cc/tRs2Xhhh/3.png" alt="Descripción de la imagen">

 </p>

<p> usar modulo ejemplo: [use 6] o [use auxiliary/scanner/ssh/ssh_enumusers] </p>

<p> 1. Establecer la IP objetivo:&nbsp; set RHOSTS [IP objetivo] </p>
<p> 2. Especificar el archivo de usuarios a comparar con los usuarios del objetivo set USER_FILE [RUTA_DEL_ARCHIVO_CON_USUARIOS] </p>
<p> &nbsp; Nota: &nbsp; El archivo usuarios.txt debe contener una lista de nombres de usuario, uno por línea</p>

<p align="center">

 <img src="https://i.postimg.cc/wvZP6FMG/5.png" alt="Descripción de la imagen">

 </p>

<p> 3. Ejecutar el módulo [run] </p>


<p align="center">

 <img src="https://i.postimg.cc/KjbPrgHY/4.png" alt="Descripción de la imagen">

 </p>


<p> Resultado: Usuarios que se encuentran en el servidor objetivo </p>

<p> &nbsp; Nota: &nbsp; con el comando [options] sirve para validar los parametros que se pueden configurar </p>


<p align="center">

 <img src="https://i.postimg.cc/RFK1HTG8/6.png" alt="Descripción de la imagen">

 </p>


<p><h3> Enumeración de usuarios en KERBEROS </h3> La enumeración de usuarios en Kerberos es una técnica utilizada para identificar cuentas de usuario válidas en un entorno de autenticación basado en Kerberos, común en entornos de Active Directory (AD). Kerberos es un protocolo de autenticación de red que utiliza tickets para permitir nodos comunicarse de manera segura. Aunque Kerberos está diseñado para ser seguro, ciertos comportamientos pueden permitir la enumeración de usuarios.</p>


<h2> Enumeración de Recursos Compartidos </h2>

<p><h2> 1.&nbsp; Enumeración SMB </h2> (Server Message Block) es una técnica fundamental en pruebas de penetración y auditorías de seguridad para recopilar información sobre sistemas Windows:</p>

</br>

<p>&nbsp; • Recursos compartidos (Shares):&nbsp; Lista de carpetas, impresoras u otros recursos compartidos en la red.&nbsp;( bash:&nbsp; smbclient -L // [target_IP] -N ) </p>
<p>&nbsp; • Usuarios y Grupos:&nbsp; Nombres de usuarios válidos en el sistema, lo que puede ser útil para ataques de fuerza bruta o phishing. &nbsp;( bash:&nbsp; enum4linux -U [target_IP] ) </p>
<p>&nbsp; • Información del Sistema Operativo:&nbsp; Detalles como el nombre, versión y build del sistema operativo. &nbsp;( bash:&nbsp; nmap --script smb-os-discovery -p 445 [target_IP] ) </p>
<p>&nbsp; • Sesiones Activas:&nbsp;  Lista de usuarios que tienen sesiones activas en el servidor SMB. &nbsp;( bash:&nbsp; net session \\ [target_IP] ) </p>
<p>&nbsp; • Configuraciones de Seguridad:&nbsp;  Lista de usuarios que tienen sesiones activas en el servidor SMB. &nbsp; ( bash:&nbsp; enum4linux [target_IP] ) </p>
<p>&nbsp; • Vulnerabilidades Conocidas:&nbsp;  Si el sistema aún utiliza SMBv1, puede ser vulnerable a ataques como EternalBlue. &nbsp; ( bash:&nbsp;  nmap --script smb-protocols -p 445 [target_IP] ) </p>


<p align="center">

 <img src="https://i.postimg.cc/BvfscT0D/smbmap.png" alt="Descripción de la imagen">

 </p>

<p> • Puertos predeterminado: 445/tcp (SMB sobre TCP/IP) o 139/tcp (NetBIOS).</p>

<p> Versiones de SMB en Windows:

<p align="center">

 <img src="https://i.postimg.cc/T1XGnX66/SMB-W.png" alt="Descripción de la imagen">

 </p>

<p> Versiones de SMB en Linux (Samba)

<p align="center">

 <img src="https://i.postimg.cc/N09wV0Gt/SMB-L.png" alt="Descripción de la imagen">

 </p>

<p> Ejemplo de enumeracion SMB</p>

<p> &nbsp; (1).&nbsp; Escaneo de puertos SMB y recursos compartidos con NMAP  </p>

<p>&nbsp;• -sV :&nbsp; Detecta la versión de SMB. </p>
<p>&nbsp;• smb-enum-shares :&nbsp; Enumerar los recursos compartidos, permisos, configuraciones inseguras, metadatos y preparar ataques posteriores </p>


<p align="center">

 <img src="https://i.postimg.cc/dVJN883r/3.png" alt="Descripción de la imagen">

 </p>

<p> &nbsp; (2).&nbsp; Enumeracion de recursos compartidos, permisos y comentararios con SMBMAP </p>

<p> 🛠 &nbsp; SMBMAP &nbsp; Herramienta diseñada  para enumerar, explorar y explotar recursos compartidos SMB </p>

</br>

<p> • Enumerar recursos compartidos (shares) sin autenticación o con credenciales </p>
<p> &nbsp; Sin credenciales ( bash:&nbsp; smbmap -[target_IP] ) </p>
<p> &nbsp; Con credenciales ( bash:&nbsp; smbmap -H [target_IP] -u [usuario] -p [contraseña]) </p>

<p> • Explorar el contenido de un recurso compartido</p>
<p> &nbsp; ( bash:&nbsp; smbmap -H [target_IP] -u [usuario] -p [contraseña] -r [recurso_compartido]) </p>

<p> • Descargar/Subir archivos (si los permisos lo permiten)</p>
<p> &nbsp; Descargar un archivo : ( bash:&nbsp; smbmap -H [target_IP] -u [usuario] -p [contraseña] --dowload [ruta remota] </p>
<p> &nbsp; Cargar un archivo : ( bash:&nbsp; smbmap -H [target_IP] -u [usuario] -p [contraseña] --upload [archivo_local] [ruta remota] </p>

<p> • Ejecución de comandos remotos (si hay suficientes privilegios)</p>
<p> &nbsp; ( bash:&nbsp; smbmap -H [target_IP] -u [usuario] -p [contraseña] -x "net user hacker P@ssw0rd /add ) </p>


<p align="center">

 <img src="https://i.postimg.cc/J0nZrzzy/4.png" alt="Descripción de la imagen">

 </p>

 <p> Solo se tiene acceso al recurso compartido temporales (tmp) el cual se encuentra en READ, WHRITE </p>

 <p>&nbsp; (3).&nbsp; conectarse al recurso compartido que tiene permisos con SMBCLIENT</p>

 <p> 🛠 &nbsp; SMBCLIENT &nbsp; Herramienta que permite interactuar con recursos compartidos </p>


<p align="center">

 <img src="https://i.postimg.cc/qBDpDXWc/5-1.png" alt="Descripción de la imagen">

 </p>

 <p> Al ingresar al recurso compartido tmp, es posible visualizar los archivos temporales, validar los permisos de escritura y descargar archivos para revisar su contenido </p>


<p align="center">

 <img src="https://i.postimg.cc/KvLvK3sn/6.png" alt="Descripción de la imagen">

 </p>


<p>&nbsp; (4).&nbsp; Enumeracion de usuarios con RCPCLIENT cuando no se tiene acceso a ningun recurso compartido</p>

</br>

<p> 🛠 &nbsp; RCPCLIENT &nbsp; Es una herramienta de línea de comandos incluida en el paquete Samba que permite interactuar con servidores Windows mediante RPC (llamadas a procedimiento remoto). Es útil para enumerar usuarios, grupos, políticas y más en sistemas Windows (o Samba en Linux).</p>


<p align="center">

 <img src="https://i.postimg.cc/Y0MXYtdY/1.png" alt="Descripción de la imagen">

 </p>


<p> &nbsp; (5).&nbsp; Realizar ataque de fuerza bruta Metasploit, Hydra, John the Ripper</p>


<p align="center">

 <img src="https://i.postimg.cc/85BmPCgD/7.png" alt="Descripción de la imagen">

 </p>

<p align="center">

 <img src="https://i.postimg.cc/fTkm1CyM/8.png" alt="Descripción de la imagen">

 </p>

<p> &nbsp; (6).&nbsp; El usuario msfadmin tiene permisos para leer el recurso compartido (print$), leer el recurso compartido (opt) y permiso de lectura y escritura en los directorios </p>
<p> &nbsp; (7).&nbsp; Iniciar sesion con el usuario y contraseña msfadmin </p>

<p align="center">

 <img src="https://i.postimg.cc/mrrPF29B/9.png" alt="Descripción de la imagen">

<p align="center">

 <img src="https://i.postimg.cc/kXdzMVr6/10.png" alt="Descripción de la imagen">

 </p>

<p> 🛠&nbsp; (8).&nbsp; Ejecutar una reverse shell </p>

<p> ----------------------------------- Pendiente documentar-------------------------------------------</p>

<p align="center">

 <img src="https://i.postimg.cc/50fDJ3P2/8.png" alt="Descripción de la imagen">

 </p>


<p> ----------------------------------- Pendiente documentar-------------------------------------------</p>


<p><h2> 1.&nbsp; Enumeración SMB </h2> NFS permite que un servidor comparta directorios y archivos con uno o más clientes a través de una red. Los clientes pueden montar esos recursos compartidos como si fueran unidades locales, facilitando el acceso centralizado a datos</p>












<p><b> • Enumeración local:</b> esto suele ocurrir después de la explotación, centrándose en los sistemas a los que hemos obtenido acceso y buscando datos confidenciales,privilegios adicionales o formas de acceder a otros sistemas. Herramientas como PowerShell, whoami, net user, y wmic permiten extraer información valiosa.</p>
		
<p><b> • Enumeración de hots:</b> Es posible que haya encontrado sistemas específicos en el reconocimiento inicial que necesitan una exploración más detallada (remoto), 
		o es posible que ya tenga acceso a una máquina y desee explorarla para ver qué información puede obtener y cómo podría ayudar a acceder a otros sistemas (local).
		Herramientas como Fping, Masscan, y Angry IP Scanner son utilizadasSe enfoca en identificar dispositivos activos en una red. Técnicas como el ping sweep, el escaneo ARP</p>
		


<p> 	» Enumeración NetBIOS :recopilación de información sobre recursos compartidos, cuentas de usuario y servicios en redes de Windows.</p>

<p> 	» Enumeración SNMP :Extracción de información de dispositivos que utilizan el Protocolo Simple de Administración de Red (SNMP). 
     	Permite extraer configuraciones de red, interfaces, direcciones IP y procesos en ejecución.</p>
				
<p>		» Enumeración LDAP :LDAP (Protocolo Ligero de Acceso a Directorios) se utiliza para acceder y mantener servicios de información de directorio 
	 	distribuidos a través de una red IP. Permite extraer nombres de usuario, direcciones de correo electrónico, grupos, departamentos y servidores del directorio.</p>
				
<p>		» Transferencia de Zona DNS :La Transferencia de Zona DNS es un mecanismo que permite a los servidores DNS compartir información. Puede estar mal configurada, 
     	lo que permite a los atacantes recuperar archivos de zona DNS completos, que contienen información sobre el dominio y sus direcciones IP asociadas.</p>
				
<p>		» Enumeración NFS :NFS (Sistema de Archivos de Red) permite a los usuarios acceder a archivos en red como si estuvieran en sus discos locales. 
	 	La enumeración puede revelar directorios y archivos compartidos.</p>
				

				
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








