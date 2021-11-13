########################################
Copias de seguridad difereciales con tar
########################################

.. note::

    Para simplificar y universalizar la documentación no se utilizarán las rutas completas, sino las siguientes convenciones:
    
    * ``/home/pablo``, como carpeta de trabajo local del ususario *pablo*. Este valor cambiará según el usuario con el que se esté operando. 
    * ``/mnt/raid1/incremental``, carpeta en el RAID 1 de OpenMediaVault donde se almacenarán las copias incrementales. 
    * ``/mnt/raid1/diferencial``, carpeta en el RAID 1 de OpenMediaVault donde se almacenarán las copias diferenciales. 

Al iniciar la práctica, el estado de las carpeta *home* es el siguiente:

.. code-block:: console

    pablo@OpenMediaVault:/home/pablo# ll
    total 20
    drwxr-xr-x 2 pablo pablo  4096 Nov 13 16:57 ./
    drwxr-xr-x 5 root  root  4096 Nov 13 16:55 ../
    -rw-r--r-- 1 pablo pablo   27 Nov 13 16:57 arch1
    -rw-r--r-- 1 pablo pablo   39 Nov 13 16:57 arch2
    -rw-r--r-- 1 pablo pablo   50 Nov 13 16:57 arch3

Copia completa
===============

.. important::

    El nombre de la carpeta destino no es "BackupDiferencial", como se indica en la práctica, sino "diferencial".

Para la creación de la copia completa del primer día de cada mes se utilizará el siguiente comando:

.. code-block:: console

    tar -cpvzf "/mnt/raid1/diferencial/backupcompleto_`date +%d%m%Y`.tgz" /home/*


Copias diferenciales
=====================

Para la creación de los siguientes backups diferenciales se utilizará el siguiente comando:

.. code-block:: console

    tar -cpvzf "/mnt/raid1/diferencial/backupdiferencial`date +%d%m%Y`.tgz" /home/* -N 13-nov-2021



Automatización del proceso de copia
=====================================

Para que el primer día de mes se ejecute el backup diferencial añadimos la siguiente entrada en el crontab:

.. code-block::

    0 3 1 * * "tar -cpvzf "/mnt/raid1/diferencial/backupcompleto_`date +%d%m%Y`.tgz" /home/*"

Este comando se ejecutará el primer día del mes a las 3 de la mañana y creará una copia completa del contenido de /home/, guardándolo en ``/mnt/raid1/diferencial``, con el nombre ``backupcompleto_`` seguido del día de creación. 

Para la copia de seguridad diaria, ejecutaremos un script, el siguiente:

.. code-block:: console

    # La siguiente instrucción guarda en la variable "TARCOMPLETO" la salida de los comandos siguientes.
    #   1. Para empezar, listamos el contenido de la carpeta destino. 
    #       Pero no lo listamos de cualquier manera, sino que lo hacemos en forma de lista (-l) 
    #       y ordenado por fecha de modificación (-t). Además, solo sacará los archivos de backup completo. 
    #   2. Con "head -1" nos quedamos solo con la primera línea de la salida. 
    #       Esta primera línea coincide con el último archivo modificado. 
    #   3. Después, cortaremos (awk) para quedarnos con la ruta al archivo. 

    TARCOMPLETO=`ls -lt  /mnt/raid1/diferencial/backupcompleto* | head -1 | grep backupcompleto_ | awk '{printf $NF}'`

        # Podemos comprobar con "echo $TARCOMPLETO"

    # Con el siguiente comando obtenemos la fecha de modificación del archivo anterior. 
    FECHA=`date -r "$TARCOMPLETO" "+%F %H:%M"`

        # Podemos comprobar con "echo $FECHA"

    # Una vez ya tenemos almacenada en FECHA el punto desde el cual tenemos que hacer la siguiente copia diferencial, ejecutamos el comando TAR:

    tar -cpvzf "/mnt/raid1/diferencial/backupdiferencial`date +%d%m%Y`.tgz" /home/* -N "$FECHA"

        # El comando anterior creará dentro de la carpeta de copias diferenciales un nuevo archivo con todo el contenido 
        # de los directorios *home* de trabajo modificado desde la fecha del útimo completo. 

Todo esto lo guardaremos como script en ``/etc/diferencial.sh`` y añadiremos la siguiete línea a *crontab*:


.. code-block::

    0 4 * * * /bin/sh /etc/diferencial.sh