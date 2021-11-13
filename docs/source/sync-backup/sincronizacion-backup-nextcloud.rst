###############################################
Sincronizar carpetas de *backup* y NextCloud
###############################################

Estructura de archivos
========================

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

.. image :: ../images/nextcloud/nc-31.png
   :width: 500
   :align: center
   :alt: Imagen en la que se puede ver la estructura de las carpetas desde la web. 
|br|


Vamos a probar a crear una carpeta llamada ``backups`` dentro del directorio de archivos del usuario. 

Debemos cambiar los permisos y el propietario de los archivos:

.. code-block:: console

   pablo@nextcloud-server:/ chown www-data:www-data /var/www/nextcloud/data/pablo/files/backups
   pablo@nextcloud-server:/ chmod 755 /var/www/nextcloud/data/pablo/files/backups

Copia con Rsync
================

Para copiar los archivos desde la *home* del usuario hacia la carpeta en NextCloud usaremos Rsync con las siguientes opciones:

.. code-block::

   rsync -au --chmod=755 --chown=www-data:www-data /mnt/raid1/diferencial /var/www/nextcloud/data/pablo/files/backups/

   rsync -au --chmod=755 --chown=www-data:www-data /mnt/raid1/incremental /var/www/nextcloud/data/pablo/files/backups/

Desglosemos las opciones:

* **-a**, la utilizamos para activar el formato archivo. Es una forma sencilla de aplicar recursividad y otras opciones que nos serán útiles.
* **-u**, esta opción fuerza al comando a omitir cualquier archivo que en el destino tenga una fecha de actualización posterior a la fecha en origen. 
* **--chmod=755**, estos son los permisos que se aplicarán a los archivos copiados en destino. 
* **--chown=www-data:www-data**, los datos copiados serán propiedad del usuario que está ejecutando el servidor web, ``www-data`` en nuestro caso. 
* **/mnt/raid1/diferencial**, es el directorio origen de los datos. 
* **/var/www/nextcloud/data/pablo/files/backups/**, es el directorio destino de los datos.

Actualizar datos en NextCloud
===============================

Aunque físicamente estén los archivos en el directorio, NextCloud "no sabe" de su existencia, pues han sido añadidos por otro proceso. Debemos forzar un escaneo de los archivos. 

Podemos hacerlo con el siguientes comando:


.. code-block::

   sudo -u www-data php ./occ files:scan --all


.. important::

   El usuario ejecutante del script php ``occ`` debe ser el del usuario web. 



Automatización
===============

Se crea un script, que será ejecutado de forma automática por el *cron*. 

El script se alojará en /etc/sync-backup.sh y tendrá el siguiente contenido:

.. code-block::

   inicio=$(date)

   logger "Proceso de copia iniciado: $inicio"

   rsync -au --chmod=755 --chown=www-data:www-data /mnt/raid1/diferencial /var/www/nextcloud/data/pablo/files/backups/

   rsync -au --chmod=755 --chown=www-data:www-data /mnt/raid1/incremental /var/www/nextcloud/data/pablo/files/backups/

   sudo -u www-data php ./occ files:scan --all

   final=$(date)

   logger "Proceso de copia finalizado: $final"

.. note::

    El proceso solo se realizará en un sentido, pues no son archivos que se deban modificar via web.

Lo añadiremos al *cron daemon* utilizando el comando ``crontab -e``.

.. code-block::

   0 * * * * /bin/sh /etc/sync-backup.sh

.. |br| raw:: html

   <br />