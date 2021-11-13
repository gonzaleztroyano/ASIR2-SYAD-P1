##########################################
Copias de seguridad incrementales con tar
##########################################

.. note::

    Para simplificar y universalizar la documentación no se utilizarán las rutas completas, sino las siguientes convenciones:
    
    * ``/home/pablo``, como carpeta de trabajo local del ususario *pablo*. Este valor cambiará según el usuario con el que se esté operando. 
    * ``/mnt/raid1/incremental``, carpeta en el RAID 1 de OpenMediaVault donde se almacenarán las copias incrementales. 
    * ``/mnt/raid1/diferencial``, carpeta en el RAID 1 de OpenMediaVault donde se almacenarán las copias diferenciales. 

Primera copia
=============

.. important::

    El nombre de la carpeta destino no es "BackupIncremental.", como se indica en la práctica, sino "incremental".

Para la creación de la copia completa del primer día de cada mes se utilizará el siguiente comando:

.. code-block:: console

    tar -cpvzf "/mnt/raid1/incremental/backupcompleto_`date +%d%m%Y`.tgz" /home/*



Copias incrementales
=====================

Para la creación de los siguientes backups incrementales se utilizará el siguiente comando:

.. code-block:: console

    # En la variable AYER guardamos el día de ayer.

    AYER=`date -d "yesterday" '+%Y-%m-%d'`

    tar -cpvzf "/mnt/raid1/incremental/backupincremental`date +%d%m%Y`.tgz" /home/* -N $AYER


Automatización del proceso de copia
=====================================

Para que el primer día de mes se ejecute el backup incremental añadimos la siguiente entrada en el crontab:

.. code-block::

    0 3 1 * * "tar -cpvzf "/mnt/raid1/incremental/backupcompleto_`date +%d%m%Y`.tgz" /home/*"

Este comando se ejecutará el primer día del mes a las 3 de la mañana y creará una copia completa del contenido de /home/, guardándolo en ``/mnt/raid1/incremental``, con el nombre ``backupcompleto_`` seguido del día de creación. 

Para la copia de seguridad diaria, ejecutaremos un script, el siguiente:

.. code-block:: console

    # En la variable AYER guardamos el día de ayer.

    AYER=`date -d "yesterday" '+%Y-%m-%d'`

    tar -cpvzf "/mnt/raid1/incremental/backupincremental`date +%d%m%Y`.tgz" /home/* -N $AYER

Lo guardaremos como script en ``/etc/incremental.sh`` y añadiremos la siguiete línea a *crontab*, habiendo permitido que root lo ejecute:

.. code-block::

    0 4 * * * /bin/sh /etc/incremental.sh