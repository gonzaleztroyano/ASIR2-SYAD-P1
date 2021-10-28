##########################################
Convertirnos en Autoridad de Certificación
##########################################

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


.. image :: ../images/web3.png
   :width: 500
   :align: center
   :alt: Captura de pantalla durante la importación del certificado AC
|br|

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


.. image :: ../images/web4.png
   :width: 500
   :align: center
   :alt: Captura de pantalla durante la importación del certificado AC
|br|

Si hacemos clic en los detalles del certificado para ver la ruta de certificación veremos:


.. image :: ../images/web5.png
   :width: 500
   :align: center
   :alt: Captura de pantalla durante la importación del certificado AC
|br|

.. |br| raw:: html

   <br />