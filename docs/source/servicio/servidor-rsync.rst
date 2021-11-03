###############
Servidor Rsync
###############

Configuración del servicio
=============================

Por defecto, en la mayoría de los sistemas Unix está instalado Rsync. Pero sólo es utilizable como cliente. 

Si solicitamos el *status* del servicio veremos que nos indica como falta el archivo ``etc/rsyncd.conf``

.. code-block:: console

    root@server-carpet:/home/user# systemctl status rsync.service
        ● rsync.service - fast remote file copy program daemon
           Loaded: loaded (/lib/systemd/system/rsync.service; enabled; vendor preset: enabled)
           Active: inactive (dead)
        Condition: start condition failed at Wed 2021-11-03 11:14:46 UTC; 2min 32s ago
                   └─ ConditionPathExists=/etc/rsyncd.conf was not met


Crearemos dicho archivo, en el que añadiremos:

.. code-block:: 

    lock file = /var/run/rsync.lock
    log file = /var/log/rsyncd.log
    pid file = /var/run/rsyncd.pid

    [rsync]
        path = /home/programster/code
        comment = Archivos_Carpet4You
        uid = user
        gid = user
        read only = no
        list = yes
        auth users = user
        secrets file = /etc/rsyncd.secrets
        hosts allow = 172.26.0.0/255.255.0.0


La autenticación la realizaremos mediante clave SSH, siguiendo los pasos descritos en :doc:`../servidor-nas/servicio-rsync-automatizado`.

Reiniciaremos el servicio para aplicar los cambios:

.. code-block:: console

    root@server-carpet:/ systemctl restart rsync.service

Configuración de autenticación
===============================

Generar clave SSH
---------------------

Por motivos de seguridad **no vamos a usar la misma clave SSH**. Por motivos intrínsecos a la ejecución del comando (debe ejecutarse de forma automática, sin interacción del usuario) la clave no debe tener contraseña simétrica. 

**Desde el cliente**, vamos a generarla. uando nos pida introducir contraseña, haremos clic en Intro para no fijar ninguna:

.. code-block:: console
    
    user@cliente:~$ ssh-keygen -t rsa

La guardaremos en ~/.ssh/rsync

Copiar clave pública a servidor
----------------------------------

Iniciando en el propio servidor (mediante SSH, por ejemplo), añadimos la clave publica al archivo ``/home/user/.ssh/authorized_keys``. Después de copiarla tendremos, al menos, dos clave:

* La clave pública para el inicio SSH "típico". 
* La clave pública que utilizaremos para la autenticación contra Rsync. 

Probar conexión a carpeta
------------------------------

Para comprobar si funciona Rsync debemos generar algunos archivos y después comprobar si se copian.

.. code-block:: console

    user@cliente:~$ sudo rsync -avRh -e "ssh -i /home/user/.ssh/rsync" prueba/ user@172.26.110.201:/rsync/

Tarea cron
===========

Añadiremos la tarea crontab con el siguiente comando:

.. code-block:: console

    user@cliente:~$ sudo su #Necesitamos que la tarea la ejecute root
    user@cliente:~$ crontab -e

    # En el archivo que se nos abre añadimos el siguiente comando:
        */15 * * * * sudo rsync -avRh -e "ssh -i /home/user/.ssh/rsync" prueba/ user@172.26.110.201:/rsync/


Limitar acceso desde IP cliente
=================================

Como medida de seguridad adicional, limitaremos el uso de la clave pública. Indicaremos que únicamente se pueda utilizar desde el equipo cliente. Para identificar al equipo usaremos su clave pública. 

.. code-block:: console

    from="<IP-del-Cliente>" ssh-rsa <Clave-SSH> <Comentario-SSH>



.. |br| raw:: html

   <br />