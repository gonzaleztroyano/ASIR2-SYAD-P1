##############
Servidor FTP
##############

Instalación de proftpd
======================

Actualizaremos los paquetes disponibles desde los repositorios:

.. code-block:: console

    user@server:~$ sudo apt update

Después instalaremos Samba:

.. code-block:: console

    user@server:~$ sudo apt install proftpd

Configuración del servicio
============================

Editaremos el archivo de configuración

.. code-block:: console

    user@server:~$ sudo nano /etc/proftpd/proftpd.conf

Aquí modificamos/añadimos las siguientes entradas:

.. code-block::

    ServerName   "Carpet4You"

    DefaultRoot /md0/home/usuario1 usuario1
    DefaultRoot /md0/home/compartidoFTP usuario2
    DefaultRoot /md0/home/compartidoFTP usuario4

Guardamos el archivo

    DefaultRoot /home/usuario1 usuario1
    DefaultRoot /home/compartidoFTP usuario2
    DefaultRoot /home/compartidoFTP usuario4

FTP Seguro
============

Generar certificado
---------------------

Instalamos, si no lo estuviera ya, OpenSSL:

.. code-block:: console

    user@server:~$ sudo apt install openssl -y


Generamos la clave, introduciendo los datos que nos solicite el comando:

.. important::

    Fijaremos los bits de la misma en 2048, no en 1024 como se puede ver en el ejemplo del archivo de configuración. 

.. code-block:: console

    user@server:~$ sudo openssl req -x509 -newkey rsa:2048 -keyout /etc/ssl/private/proftpd.key -out /etc/ssl/certs/proftpd.crt -nodes -days 90

Configuramos los permisos correctos para la clave y el certificado:

.. code-block:: console

    user@server:~$ sudo chmod 600 /etc/ssl/private/proftpd.key
    user@server:~$ sudo chmod 600 /etc/ssl/certs/proftpd.crt

Activar FTP Seguro
-------------------

Volvemos a editar el archivo de configuración ``/etc/proftpd/proftpd.conf``. En dicho archivo, descomentamos, si no lo estuviera ya, la siguiente línea:

.. code-block:: 

    Include /etc/proftpd/tls.conf

En este archivo, ``/etc/proftpd/tls.conf``, añadimos o modificamos las sigueintes líneas:

.. code-block:: 

    TLSRSACertificateFile /etc/ssl/certs/proftpd.crt
    TLSRSACertificateKeyFile /etc/ssl/private/proftpd.key
    TLSEngine on
    TLSLog /var/log/proftpd/tls.log
    TLSProtocolo SSLv23
    TLSRequired off
    TLSOptions NoCertRequest NoSessionReuseRequired
    TLSVerifyClient off

Una vez hecho, debemos reiniciar el servicio:

.. code-block:: console

    user@server:~$ systemctl restart proftpd

Conexión al servidor
=====================

En el programa Filezilla introducimos los datos de conexión 

.. image :: ../images/servicio/ftp-1.png
   :width: 500
   :align: center
   :alt: Conexión a la carpeta compartida con Filezilla
|br|


.. |br| raw:: html

   <br />