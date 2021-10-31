######################
Instalación NextCloud
######################

Paquetes necesarios
====================

Instalaremos los siguientes paquetes desde la terminal:

.. code-block:: console
    
    sudo apt update
    sudo apt install apache2 mariadb-server libapache2-mod-php7.4
    sudo apt install php7.4-gd php7.4-mysql php7.4-curl php7.4-mbstring php7.4-intl
    sudo apt install php7.4-gmp php7.4-bcmath php-imagick php7.4-xml php7.4-zip


Crear base de datos
===================

NextCloud almacena la información en una base de datos MySQL/MariaDB. 

Iniciaremos el proceso e iniciaremos sesión en el administrador de la base de datos para proceder a craer la base de datos que NextCloud usará:

.. code-block:: console

    # Iniciar el proceso, si no lo estuviera
    sudo /etc/init.d/mysql start

    # Iniciar sesión con el usuario root
    sudo mysql -uroot -p


.. code-block:: mysql
    
    CREATE USER 'nc_pablo_oAb30'@'localhost' IDENTIFIED BY 'nc_pablo_pw_6BN6';
    CREATE DATABASE IF NOT EXISTS nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    GRANT ALL PRIVILEGES ON nextcloud.* TO 'nc_pablo_oAb30'@'localhost';

Salimos, pues el propio NextCloud creará las tablas en la primera conexión:

.. code-block:: mysql
   
    quit;

Descargar NextCloud
====================

Descargaremos la última versión d NextCloud:

#. Accedemos a la `página de descarga <https://nextcloud.com/install/>`_ de NextCloud. 
#. Seleccionamos la versión *Server* y hacemos clic en *Download for Server*. 
#. En la parte inferior de la página, haremos clic en el botón *Details and download options*. 
#. En nuestro caso, utilizaremos el archivo tar comprimido y descargaremos:

 * El `instalador <https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2>`_, la `suma MD5 <https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2.md5>`_ y la `suma SHA256 <https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2.sha256>`_.
 * Descargaremos la `clave GPG <https://nextcloud.com/nextcloud.asc>`_ de NextCloud y la `firma .asc <https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2.asc>`_.


.. code-block:: console

    mkdir nextcloud-temp
    cd nextcloud-temp
    wget https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2
    wget https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2.md5
    wget https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2.sha256
    wget https://download.nextcloud.com/server/releases/nextcloud-22.2.0.tar.bz2.asc
    wget https://nextcloud.com/nextcloud.asc

Verificación del archivo:

.. code-block:: console

    pablo@cloud:~/nextcloud-temp$ md5sum -c nextcloud-22.2.0.tar.bz2.md5 
    nextcloud-22.2.0.tar.bz2: OK
    pablo@cloud:~/nextcloud-temp$ sha256sum -c nextcloud-22.2.0.tar.bz2.sha256 
    nextcloud-22.2.0.tar.bz2: OK


Importación de la clave de NextCloud:

.. code-block:: console

    pablo@cloud:~/nextcloud-temp$ gpg --import nextcloud.asc
        gpg: directory '/home/pablo/.gnupg' created
        gpg: keybox '/home/pablo/.gnupg/pubring.kbx' created
        gpg: /home/pablo/.gnupg/trustdb.gpg: trustdb created
        gpg: key D75899B9A724937A: public key "Nextcloud Security <security@nextcloud.com>" imported
        gpg: Total number processed: 1
        gpg:               imported: 1


Verificación de la firma:

.. code-block:: console

    pablo@cloud:~/nextcloud-temp$ gpg --verify nextcloud-22.2.0.tar.bz2.asc nextcloud-22.2.0.tar.bz2
        gpg: Signature made Wed Sep 29 21:24:40 2021 UTC
        gpg:                using RSA key 28806A878AE423A28372792ED75899B9A724937A
        gpg: Good signature from "Nextcloud Security <security@nextcloud.com>" [unknown]
        gpg: WARNING: This key is not certified with a trusted signature!
        gpg:          There is no indication that the signature belongs to the owner.
        Primary key fingerprint: 2880 6A87 8AE4 23A2 8372  792E D758 99B9 A724 937A


Extracción de archivos
=======================

Usaremos el siguiente comando, teniendo en cuenta que puede tardar un poco, al ser bastantes archivos:


.. code-block:: console

    pablo@cloud:~/nextcloud-temp$ tar -xjvf nextcloud-22.2.0.tar.bz2

Copiamos el contenido a la raíz del servidor web:

.. code-block:: console

    pablo@cloud:~/nextcloud-temp$ cp -r nextcloud /var/www


Configuración servidor web
==========================

Crearemos el archivo ``/etc/apache2/sites-available/nextcloud.conf``, añadiendo el siguiente contenido:

.. code-block::

    <VirtualHost *:80>
    DocumentRoot /var/www/nextcloud/
    ServerName  cloud.carpet4you.site

    <Directory /var/www/nextcloud/>
        Require all granted
        AllowOverride All
        Options FollowSymLinks MultiViews

        <IfModule mod_dav.c>
        Dav off
        </IfModule>
    </Directory>
    </VirtualHost>


Activamos el sitio y reiniciamos Apache:

.. code-block:: console

    a2ensite nextcloud.conf
    systemctl reload apache2

Activamos una serie de módulos necesarios:

.. code-block:: console

    a2enmod rewrite
    a2enmod headers
    a2enmod env
    a2enmod dir
    a2enmod mime


Cambiamos de propiedad los archivos:

.. code-block:: console

    chown -R www-data:www-data /var/www/nextcloud/

Primer acceso
==============

Añadiremos un registro A en cloud.carpet4you.site con la IP de la máquina virtual. 

Al acceder a esta dirección, deberemos escribir los detalles de acceso a la base de datos:

.. image :: ../images/nextcloud/nc-9.png
   :width: 500
   :align: center
|br|

Nota: no indicamos que instale Talk, Mail, Contacts ni Edición Colaborativa; pues lo haremos posteriormente.

En unos segundos estaremos dentro:

.. image :: ../images/nextcloud/nc-10.png
   :width: 500
   :align: center
|br|


.. |br| raw:: html

   <br />