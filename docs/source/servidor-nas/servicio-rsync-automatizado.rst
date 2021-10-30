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

Para que el equipo servidor reconozca esta clave, debemos añadirla al archivo ``/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys`` en el servidor. 

.. code-block:: console

    user@server-carpet:~$ rsync -avRh -e "ssh -i ~/.ssh/backup -o StrictHostKeyChecking=no"  /home/user/prueba/* user@nas.corp.carpet4you.site:/home

