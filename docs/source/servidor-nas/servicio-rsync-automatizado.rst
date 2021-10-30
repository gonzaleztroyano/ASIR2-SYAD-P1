############################
Servicio Rsync automatizado 
############################

En el enunciado del ejercicio se nos solicita que la tarea de sincronización Rsync se ejecute de forma automática cada 15 minutos. 


| Para hacerlo debemos: 
| 1) Utilizar una clave SSH para autenticarnos contra Rsync.
| 2) Programar una tarea *cron* para la ejecución de la sincronización de forma automatizada. 

Generar clave SSH
==================

Por motivos de seguridad **no vamos a usar la misma clave SSH**. Por motivos intrínsecos a la ejecución del comando (debe ejecutarse de forma automática, sin interacción del usuario) la clave no debe tener contraseña simétrica. 

Vamos a generarla, cuando nos pida introducir contraseña, haremos clic en Intro para no fijar ninguna:

.. code-block:: console
    
    pablo@carpet:~$ ssh-keygen -t rsa

La guardaremos en ~/.ssh/backup

Probar conexión a carpeta
===========================

Para comprobar si funciona Rsync debemos generar algunos archivos y después comprobar si se copian.

.. code-block:: console

    user@server-carpet:~$ sudo rsync -avRh -e "ssh -i /home/user/.ssh/backup"  prueba/ user@nas.corp.carpet4you.site:/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/

Este es el resultado:

.. image :: ../images/nas/nas44-rsync.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|


Tarea cron
===========

Añadiremos la tarea crontab con el siguiente comando:

.. code-block:: console

    user@server-carpet:~$ sudo su #Necesitamos que la tarea la ejecute root
    user@server-carpet:~$ crontab -e

    # En el archivo que se nos abre añadimos el siguiente comando:
        */15 * * * * sudo rsync -aRh -e "ssh -i /home/user/.ssh/backup"  /home/user/prueba user@nas.corp.carpet4you.site:/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/

Comprobación cron
==================

Crearemos algún archivo en la carpeta prueba y veremos si se copia en el servidor.

.. tip::

    | Puede ser útil cambiar el cron para que se ejecute cada minuto durante las pruebas.
    | Para configurar la programación de cron, `esta página <https://crontab.guru/every-15-minutes>`_ es muy útil.

**¡Funciona!**

.. image :: ../images/nas/nas45-rsync.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|


.. |br| raw:: html

   <br />