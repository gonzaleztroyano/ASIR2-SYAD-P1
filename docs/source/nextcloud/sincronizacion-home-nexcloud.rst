############################################
Sincronización entre la *home* y NextCloud
############################################

.. note::

   Los archivos se están copiando desde la carpeta home de los usuarios del equipo, no desde la home de OpenMediaVault. Para copiar/sincronizar estas carpetas sería suficiente con cambiar las rutas pertinentes


En una instalación mediante paquetes APT, como es la nuestra, la carpeta por defecto donde se guardan los datos de los usuarios está localizada en la ruta ``/var/www/nextcloud/data/``. 

Dentro de este directorio, encontraremos una carpeta para cada usuario. Dentro de dicha carpeta, tendremos una carpeta, llamada ``data`` (junto con otras), donde se guardará los datos:

.. code-block::

    pablo@nextcloud-server:/var/www/nextcloud/data/pablo# tree -L 2
    .
    ├── cache
    ├── files
    │   ├── BOCM-20180824-12.PDF
    │   ├── Documento.docx
    │   ├── Documentokk.docx
    │   ├── Documents
    │   ├── Nextcloud Manual.pdf
    │   ├── Nextcloud intro.mp4
    │   ├── Nextcloud.png
    │   ├── Photos
    │   ├── Plantillas
    │   ├── Reasons to use Nextcloud.pdf
    │   └── bash-shell-cheat-sheet.pdf
    ├── files_versions
    │   └── Documento.docx.v1635706677
    ├── onlyoffice
    │   └── 469
    └── uploads


Como vemos, la estructura del directorio ``files`` es lo mismo que podemos ver desde la interfaz web. 

.. image :: ../images/nexcloud/nc-31.png
   :width: 500
   :align: center
   :alt: Imagen en la que se puede ver la estructura de las carpetas desde la web. 
|br|


Vamos a probar a crear una carpeta llamada ``home`` dentro del directorio de archivos del usuario. 

Debemos cambiar los permisos y el propietario de los archivos:

.. code-block:: console

   pablo@nextcloud-server:/ chown www-data:www-data /var/www/nextcloud/data/pablo/files/home
   pablo@nextcloud-server:/ chmod 755 /var/www/nextcloud/data/pablo/files/home


Copia con Rsync
================

Para copiar los archivos desde la *home* del usuario hacia la carpeta en NextCloud usaremos Rsync con las siguientes opciones:

.. code-block::

   rsync -a --exclude={.*} --chmod=755 --chown=www-data:www-data /home/pablo/ /var/www/nextcloud/data/pablo/files/home/


Desglosemos las opciones:

* **-a**, la utilizamos para activar el formato archivo. Es una forma sencilla de aplicar recursividad y otras opciones que nos serán útiles.
* **--exclude={.*}**, con esta opción excluimos los archivos y directorios que empiezan por ``.``. Es decir, los que están ocultos. 
* **--chmod=755**, estos son los permisos que se aplicarán a los archivos copiados en destino. 
* **--chown=www-data:www-data**, los datos copiados serán propiedad del usuario que está ejecutando el servidor web, ``www-data`` en nuestro caso. 
* **/home/pablo/**, es el directorio origen de los datos. 
* **/var/www/nextcloud/data/pablo/files/home/**, es el directorio destino de los datos. 


Ahora en el destino tenemos los datos:

.. code-block::

   pablo@nextcloud-server:/var/www/nextcloud/data/pablo/files# tree home/
   home/
   ├── dhparam.pem
   ├── tls.crt
   ├── tls.csr
   └── tls.key


Actualizar datos en NextCloud
===============================

Aunque físicamente estén los archivos en el directorio, NextCloud "no sabe" de su existencia, pues han sido añadidos por otro proceso. Debemos forzar un escaneo de los archivos. 

Podemos hacerlo con el siguientes comando:


.. code-block::

   sudo -u www-data php ./occ files:scan --all


.. important::

   El usuario ejecutante del script php ``occ`` debe ser el del usuario web. 


La salida del comando es la siguientes:


.. code-block::

   Starting scan for user 1 out of 2 (pablo)
      +---------+-------+--------------+
      | Folders | Files | Elapsed time |
      +---------+-------+--------------+
      | 18      | 49    | 00:00:00     |
      +---------+-------+--------------+


Si ahora accedemos desde la interfaz web veremos los archivos:

.. image :: ../images/nexcloud/nc-32.png
   :width: 500
   :align: center
   :alt: Interfaz web en la que se ven los archivos copiardos con Rsync en la web.
|br|




.. |br| raw:: html

   <br />