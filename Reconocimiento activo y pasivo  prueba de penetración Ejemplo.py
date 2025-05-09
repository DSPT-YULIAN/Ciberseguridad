

Escenario de prueba de penetración 
Tomemos un ejemplo para demostrar cómo podríamos integrar las herramientas mencionadas anteriormente. En esta evaluación simulada, nos centramos en Crybaby LLC. 
Han indicado que todos sus activos están dentro del alcance y nos han proporcionado un nombre de dominio para comenzar: crybaby.it .



Motores de búsqueda
Herramienta: Google
Resultado: Buscamos nuestro objetivo en Google y encontramos un subdominio, mail.crybaby.it. Probablemente sea un servidor de correo, pero aún no es un hallazgo importante. 
Sigamos adelante.

Descubrimiento de dominio
Herramienta: dnsenum
Resultado: Usando dnsenum, descubrimos mail.crybaby.it y un entorno de desarrollo, dev.crybaby.it. Este segundo parece interesante.

Escaneo de puertos
Herramienta: Nmap
Resultado: No hay puertos abiertos en dev.crybaby.it, pero sí varios en mail.crybaby.it: puertos 80 (HTTP), 443 (HTTPS), 25 (SMTP) y 161/162 (SNMP). 
Inesperadamente, hay un servidor web y un servicio SNMP. Analicemos SNMP.

Descubrimiento de red
Herramienta: SNMP Walk
Resultado: Tenemos detalles sobre los dispositivos de red y sus configuraciones, incluyendo la cadena de comunidad (similar a una contraseña) utilizada para las consultas. 
Esto podría ser útil más adelante. Ahora, exploremos el servicio web.

Análisis de Techstack
Herramienta: Wappalyzer
Resultado: Encontramos una página de inicio de sesión en dev.crybaby.it. Wappalyzer muestra que ejecuta Apache, PHP, MySQL y algunos frameworks JavaScript populares, 
pero no presenta vulnerabilidades conocidas. Es hora de investigar más a fondo.

Pruebas de aplicaciones web
Herramienta: Burp Suite
Resultado: Con Burp Suite, revisamos las llamadas realizadas por el sitio web e identificamos posibles puntos de inyección SQL. ¡Genial! Intentemos aprovecharlos.

Análisis de vulnerabilidad
Herramienta: SQLmap
Resultado: ¡Ejecutamos SQLmap y pudimos detectar y explotar algunas inyecciones SQL! ¡Eso va a aparecer en nuestro informe! ¡Genial! Lamentablemente, 
no hemos encontrado ninguna cuenta de usuario que nos permita superar ese inicio de sesión. Repasemos el análisis y veamos si alguno de esos escáneres de internet ha identificado vulnerabilidades que nos permitan ahorrar tiempo en ese aspecto.


Escaneo de Internet
Herramienta: Shodan
Resultado: ¡Claro que sí, Shodan! Al parecer, este servidor usa credenciales predeterminadas. O al menos, así era hace una semana cuando Shodan realizó el análisis. 
Resulta que no funcionan. ¡Qué lástima! Pero, si prefieren usar credenciales predeterminadas, quizá haya otros sitios que las tengan...

Archivos web
Herramienta: Wayback Machine
Resultado: Wayback Machine muestra una captura de pantalla de dev.crybaby.it/adm. Resulta que esta página sigue activa y las credenciales predeterminadas funcionan. 
Ahora tenemos acceso a un área autenticada de la aplicación web, pero no al servidor.

Descubrimiento de contenido
Herramienta: Feroxbuster
Resultado: ¡Feroxbuster nos encuentra una sección para subir archivos! Subir un archivo PHP nos da acceso a una consola remota, pero con privilegios limitados. 
Veamos qué podemos hacer.

Enumeración de hosts
Herramienta: LinPEAS
Resultado: LinPEAS proporciona un informe con código de colores de posibles vectores de escalada de privilegios. Nuestro usuario tiene privilegios SUID para /bin/cp, 
lo que nos permite agregar un nuevo usuario con privilegios y obtener acceso completo.



********************************************************************************************************

Parte 1: Sitios web objetivo

1. Navegar por el sitio WEB "rekt.systems"

2. Evidenciar Subdominios navegando cada enlace en el menú de navegación del sitio WEB Ejemplo 
"https://rekt.systems./software-engineer.html"

En la descripción completa del puesto de Ingeniero de Software . 
Se evidencia que solicitan personas con experiencia específica en una version de phpmyadmin.
(preferiblemente experiencia con la versión 4.8.1)

3.Capturemos nuestro historial de navegación para poder inspeccionar este recurso desde otra perspectiva

Con la herramienta 1History permite hacer una copia de seguridad de nuestro historial de navegación y exportarlo a un archivo CSV

	•	ejecute onehistory backup
	•	ejecute onehistory export (para exportar el historial del navegador a un archivo CSV)
	•	ejecute cat (visualizar archivos desde la terminal) onehistory-xx-xx-xx.csv
	•	ejecute gf urls onehistory-xxxx-xx-xx.csv | anew > url.lst para capturar todas las URL (gf para encontrar patrones específicos (URL))
		(anew coincidencias de patrones)
	•	ejecute getJS --input url.lst --complete | xargs wget (para capturar todas las URL que ha explorado en un archivo de texto) 
		lo que le permite ver el código fuente (proporciona información sobre la funcionalidad del sitio y puede revelar puntos finales adicionales)
	•	ejecute getJS --input url.lst --complete | xargs wget (para encontrar todos los archivos javascript referenciados en el HTML de las URL descubiertas)
		(--input url.lst), mostrar la URL completa de esos archivos (--complete) en la salida y descargar cada uno al directorio actual 
		(| xargs wget)
		
	• 	ejecute gf urls main.js | anew > url.lst para encontrar las URL en el archivo Javascript y añadir las nuevas a su lista
	
	
	
Parte 2: Motores de búsqueda

1. Operadores de busqueda

	• site:rekt.systems - limita los resultados a cualquier término en "rekt.systems"
	• inurl:rekt.systems - limita los resultados a las URL que contienen "rekt.systems"
	• intitle:rekt.systems - restringe los resultados a títulos de páginas que contengan "rekt.systems"
	• intext:rekt.systems - restringe los resultados a cualquier texto de página que contenga "rekt.systems"
	• filetype:pdf - "rekt.systems:pdf" restringe los resultados a archivos PDF "rekt.systems"
	• ext:pdf - "rekt.systems:ext:pdf" restringe los resultados a archivos que terminan en .pdf
	
2. Herramientas OSINT
	
	• https://inteltechniques.com/tools/Domain.html
		
3. Analizar Metadata

	• exiftool 
	
		Coordenadas GPS: identifican la ubicación física donde se tomó la imagen.
		Nombre del autor: identifica a los empleados.
		Productor: identifica el software utilizado para convertir a PDF.
		Creador: identifica el software utilizado para crear el documento original.
		
4. Busqueda de vulnerabilidades
		
		
Parte 3: Registros publicos
	
	• whois obtener la información de registro del dominio de su destino. 
	• ctfr (terminal) buscar certificados registrados para subdominios de *rekt.systems.

Parte 4: Plataformas CTI y archivos web

	• ejecute gau (Terminal) rekt.systems para obtener todas las URL conocidas por AlienVaultOTC, CommonCrawl, urlscan.io y waybackmachine.
	

Parte 5: Plataformas sociales

	• Linkedln
	• site:linkedin.com intext:rektsystems
	
	
	
	