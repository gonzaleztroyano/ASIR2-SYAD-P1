#############
Servidor web
#############

Instalar servidor web
=====================

Para instalar el servidor SSH, si no estuviera instalado, debemos ejecutar el siguiente comando:

.. code-block:: console
    
    user@server-carpet:~$ apt update
    user@server-carpet:~$ apt install apache2

Si lo acabamos de instalar debemos iniciarlo y permitir su inicio en el arranque del equipo:

.. _referencia-reinicio-apache:

.. code-block:: console
    
    user@server-carpet:~$ systemctl enable apache2
    user@server-carpet:~$ systemctl start apache2


Conectarse al servidor web
===========================

Modificar archivo hosts / añadir subdominio
--------------------------------------------

En nuestro caso, al disponer de un dominio resoluble en Internet, hemos añadido el subdominio *www.carpet4you.site*. 

Comprobaremos con el comando *dig* si ha sido añadido correctamente:

.. code-block:: console
    
    user@server-carpet:~$ dig www.carpet4you.site.

    ; <<>> DiG 9.11.3-1ubuntu1.11-Ubuntu <<>> www.carpet4you.site.
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 30217
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 65494
    ;; QUESTION SECTION:
    ;www.carpet4you.site.           IN      A

    ;; ANSWER SECTION:
    www.carpet4you.site.    3600    IN      A       192.168.56.109

    ;; Query time: 111 msec
    ;; SERVER: 127.0.0.53#53(127.0.0.53)
    ;; WHEN: Sun Oct 24 19:37:36 UTC 2021
    ;; MSG SIZE  rcvd: 64


Si ahora intentamos conectarnos a dicho dominio desde el navegador web veremos:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/web1.png" alt="Captura de pantalla del servidor">
    </div>


.. note ::

    Si no tuviéramos un archivo disponible siempre podríamos editar el archivo hosts de nuestro equipo.


Generar certificado autofirmado
================================

Para generar el certificado autofirmado podemos utilizar el siguiente comando:

.. code-block:: console

    user@server-carpet:~$ sudo openssl req -x509 -nodes -days 90 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt


Vamos a desgranar el comando:

 * **openssl**, es el comando básico para la gestión de OpenSSL.
 * **req**, indicamos que queremos usar el estándar X.509 de petición de firma de certificados (CSR).
 * **-x509**, modificador de la opción anterior, con la que indicamos que queremos autofirmarlo en vez de generar una petición de firma a una entidad de certificación. 
 * **-nodes**, indica que no queremos proteger el certificado con una contraseña. Esto es importante puesto que Apache necesitará utilizar el certificado sin que un usuario/a tenga que introducir la contraseña simétrica con cada petición.
 * **-days 90**, periodo de validez del certificado.
 * **-newkey rsa:2048**, esto especifica que queremos generar un nuevo certificado y una nueva clave al mismo tiempo. No hemos creado la clave necesaria para firmar el certificado en un paso anterior, así que tenemos que crearla junto con el certificado. La parte rsa:2048 le indica que cree una clave RSA de 2048 bits.
 * **-keyout**, este modificador indica a OpenSSL dónde guardar el archivo de clave privada generado que estamos creando.
 * **-out**, indicamos dónde queremos guardar el certificado que estamos creando.


Nos pedirá una serie de datos que podremos ir completando con el teclado:

.. code-block:: console
    :emphasize-lines: 13,14,15,16,17,18,19

    Generating a RSA private key
    .......................+++++
    .+++++
    writing new private key to '/etc/ssl/private/apache-selfsigned.key'
    -----
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [AU]:ES
    State or Province Name (full name) [Some-State]:Badajoz
    Locality Name (eg, city) []:El Carrascalejo
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Carpet4You
    Organizational Unit Name (eg, section) []:IT Management
    Common Name (e.g. server FQDN or YOUR name) []:www.carpet4you.site
    Email Address []:pablo@carpet4you.site


Configurar el sitio nuevo en Apache
===================================

Creamos el archivo:

.. code-block:: console

    user@server-carpet:~$ sudo nano /etc/apache2/sites-available/www.carpet4you.site.conf


En dicho archivo, añadimos el siguiente texto:

.. code-block:: console

    <VirtualHost *:443>
        ServerName www.carpet4you.site
        DocumentRoot /var/www/html
        SSLEngine on
        SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
        SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
    </VirtualHost>

También debemos activar una serie de módulos y configuraciones

.. code-block:: console

    user@server-carpet:~$ sudo a2enmod ssl
    user@server-carpet:~$ sudo a2enmod headers
    user@server-carpet:~$ sudo a2enconf ssl-params


Reiniciamos el servicio tal y como hemos visto de forma previa :ref:`referencia-reinicio-apache`.

Ahora podremos visitar la web con el nuevo certificado y comprobar que funciona:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/web2.png" alt="Captura de pantalla del servidor">
    </div>

Generar certificado AC y confianza
==================================

.. https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/

Generar la clave privada de la Autoridad de Certificación. Nos solicitará una contraseña para protegerla. 

.. code-block:: console

    user@server-carpet:~$ openssl genrsa -des3 -out CA_Carpet4You.key 2048


Generamos el certificado raíz para nuestra AC:

.. code-block:: console

    user@server-carpet:~$ openssl req -x509 -new -nodes -key CA_Carpet4You.key -sha256 -days 365 -out CA_Carpet4You.pem


Nos solicitará la contraseña de nuestra clave privada de AC, así como una serie de datos para el certificado raíz:

.. code-block:: console
    
    Enter pass phrase for CA_Carpet4You.key:
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [AU]:ES
    State or Province Name (full name) [Some-State]:Badajoz
    Locality Name (eg, city) []:El Carrascalejo
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Carpet4You Trust
    Organizational Unit Name (eg, section) []:Trust Service Management
    Common Name (e.g. server FQDN or YOUR name) []:AC Carpet4You Trust
    Email Address []:pablo@carpet4you.site


Importar certificado AC en dispositivo
=======================================

Normalmente no debemos importar ningún certificado raíz puesto que en el Sistema Operativo ya vienen añadidos. En nuestro caso, debemos importarlo manualmente.

Para importar el certificado debemos navegar en los ajustes del navegador Chrome hasta `chrome://settings/security <chrome://settings/security>`_. Una vez aquí hacemos clic en *Gestionar certificados*.

En la pantalla que nos aparece debemos desplazarnos hasta la sección *Entidades de certificación raíz de confianza* y hacer clic en Importar.

Seleccionamos el archivo *CA_Carpet4You.pem* generado de forma previa. Veremos un aviso al importarlo:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/web3.png" alt="Captura de pantalla durante la importación del certificado AC">
    </div>

Creción de certificado firmado por nuestra CA
==============================================

Private key
-----------

Crearemos nuestra clave privada para el servidor:

.. code-block:: console

    user@server-carpet:~$ openssl genrsa -out www.carpet4you.site.key 2048


CSR
----

Iniciamos una *Certificate Signing Request* (CSR):

.. code-block:: console

    user@server-carpet:~$ openssl req -new -key www.carpet4you.site.key -out www.carpet4you.site.csr


Archivo de configuración
------------------------

Lo siguiente que haremos es crear el certificado utilizando la CSR, la clave privada de CA, el certificado de nuestra CA y un certificado de configuración que vamos a crear a continuación.

En este archivo, que llamaremos *www.carpet4you.site.ext* añadiremos el siguiente contenido:

.. code-block:: console

    authorityKeyIdentifier=keyid,issuer
    basicConstraints=CA:FALSE
    keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
    subjectAltName = @alt_names

    [alt_names]
    DNS.1 = www.carpet4you.site

Generar certificado final
--------------------------

.. code-block:: console
    
    openssl x509 -req -in www.carpet4you.site.csr -CA CA_Carpet4You.pem -CAkey CA_Carpet4You.key -CAcreateserial \
    -out www.carpet4you.site.crt -days 90 -sha256 -extfile www.carpet4you.site.ext


Ahora tendremos varios archivos:

.. code-block:: console

    user@server-carpet:~$ ll ww*
    -rw-rw-r-- 1 user user 1570 oct 24 21:30 www.carpet4you.site.crt
    -rw-rw-r-- 1 user user 1147 oct 24 21:21 www.carpet4you.site.csr
    -rw-rw-r-- 1 user user  210 oct 24 21:28 www.carpet4you.site.ext
    -rw------- 1 user user 1679 oct 24 20:47 www.carpet4you.site.key

Utilizar certificado en Apache
------------------------------

Modificamos el archivo */etc/apache2/sites-available/www.carpet4you.site.conf* para que pase a ser de la siguiente manera:

.. code-block:: console
    
    <VirtualHost *:443>
        ServerName www.carpet4you.site
        DocumentRoot /var/www/html
        SSLEngine on
        SSLCertificateFile /home/user/www.carpet4you.site.crt
        SSLCertificateKeyFile /home/user/www.carpet4you.site.key
    </VirtualHost>


Ahora no aparecerá ningún error al cargar la página:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/web4.png" alt="Captura de pantalla durante la importación del certificado AC">
    </div>


Si hacemos clic en los detalles del certificado para ver la ruta de certificación veremos:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/web5.png" alt="Captura de pantalla durante la importación del certificado AC">
    </div>

