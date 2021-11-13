###############
Servidor SAMBA
###############

Instalación de Samba
======================

Actualizaremos los paquetes disponibles desde los repositorios:

.. code-block:: console

    user@server:~$ sudo apt update

Después instalaremos Samba:

.. code-block:: console

    user@server:~$ sudo apt install samba

Al instalar SAMBA, por defecto se iniciará el *daemon*. Para trabajar más cómodos y evitar problemas de seguridad hasta que esté completamente configurado, vamos a detener el servicio:

.. code-block:: console

    user@server:~$ sudo systemctl stop smbd.service

Configuración de Samba
=======================

Debemos conocer sobre qué adaptador vamos a trabajar, pues lo necesitaremos posteriormente para la configuración. 

Para hacerlo, usaremos el siguiente comando:

.. code-block:: console

    user@server:~$ ip a 

        1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
            link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
            inet 127.0.0.1/8 scope host lo
            valid_lft forever preferred_lft forever
            inet6 ::1/128 scope host
            valid_lft forever preferred_lft forever
        2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
            link/ether 08:00:27:d5:b1:16 brd ff:ff:ff:ff:ff:ff
            inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
            valid_lft 85970sec preferred_lft 85970sec
            inet6 fe80::a00:27ff:fed5:b116/64 scope link
            valid_lft forever preferred_lft forever
        3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
            link/ether 08:00:27:62:5d:9d brd ff:ff:ff:ff:ff:ff
            inet 192.168.56.109/24 brd 192.168.56.255 scope global dynamic enp0s8
            valid_lft 470sec preferred_lft 470sec
            inet6 fe80::a00:27ff:fe62:5d9d/64 scope link
            valid_lft forever preferred_lft forever

En nuestro caso, la interfaz que usaremos será la *enp0s8*. 


Copiaremos, para hacer *rollback* en caso de ser necesario, el archivo de configuración de Samba:

.. code-block:: console

    user@server:~$ sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.1.bak

.. note::

    Es muy interesante mantener las últimas versiones de los archivos de configuración. De esta manera, tenemos una especie de historial por si quisiéramos revertir los ajustes a una configuración anterior. 

Edición del archivo de configuración
----------------------------------------

.. tip::

    Puede ser interesante renombrar el archivo original y crear uno limpio para no tener comentarios "inútiles" en el archivo de configuración. 

.. code-block:: console

     user@server:~$ sudo nano /etc/samba/smb.conf

        #Este archivo contendrá:
        [global]
            server string = Carpet4You_SambaServer
            workgroup = carpet4you.site
            interfaces = enp0s8
            bind interfaces only = yes
            log file = /var/log/samba/smb.log
            max log size = 10000 
            ; Está en KiB, por defecto está en 1000. Logrotate recomendable. 
            
            server role = standalone server
            
            ; Esta opción sincronizará la contraseña del comando smbpasswd con la contraseña de UNIX en segundo plano 
            unix password sync = yes
            passwd program = /usr/bin/passwd %u
            passwd chat = "*New Password:*" %n\n "*Reenter New Password:*" %n\n "*Password changed.*"
            ;
            map to guest = bad user

Guardamos el archivo. Para comprobar si la configuración es corracta podemos usar el siguiente comando:

.. code-block:: console

     user@server:~$ sudo testparm
        Load smb config files from /etc/samba/smb.conf
        rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
        Loaded services file OK.
        Server role: ROLE_STANDALONE

        Press enter to see a dump of your service definitions
        [...]


Creación de usuarios
======================

Vamos a crear dos usuarios Samba: *marta* y *juan*.

Usaremos los siguientes comandos:

.. code-block:: console

    user@server:~$ sudo adduser --shell /usr/sbin/nologin --home /md0/home/marta --ingroup sambashare marta
    user@server:~$ sudo adduser --shell /usr/sbin/nologin --home /md0/home/juan --ingroup sambashare juan

.. La contraseña de los usuarios es su propio nombre. 

Si como *root* o como usuarios con permisos para ejecutar *sudo* creáramos un archivo o directorio en las carpetas de los usuarios tendríamos un problema, pues el usuario final no podría editarlo.

Para remediarlo ejecutamos los siguientes comandos:

.. code-block:: console

    user@server:~$ sudo chown juan:sambashare /md0/home/juan
    user@server:~$ sudo chown marta:sambashare /md0/home/marta
    user@server:~$ sudo chmod -R 2770 /md0/home/juan/
    user@server:~$ sudo chmod -R 2770 /md0/home/marta/

Ya tenemos creados los usuarios en el sistema operativo, pero no en Samba, para hacerlo:

.. code-block:: console

    # -a para añadir (add) el usuario
    user@server:~$ sudo smbpasswd -a juan
    # -e para activar (enable) el usuario
    user@server:~$ sudo smbpasswd -e juan
    user@server:~$ sudo smbpasswd -a marta
    user@server:~$ sudo smbpasswd -e marta


Configurar las carpetas compartidas
=====================================

Volveremos a modificar el archivo ``/etc/samba/smb.conf``, añadiendo el siguiente contenido:

.. code-block::

    [marta]
        path = /md0/home/marta
        browseable = no
        read only = no
        force create mode = 0660
        force directory mode = 2770
        valid users = marta

    [juan]
        path = /md0/home/juan
        browseable = no
        read only = no
        force create mode = 0660
        force directory mode = 2770
        valid users = juan

.. tip::

    Con cada cambio en el archivo de configuración es recomendable ejecutar ``testparm``
    Puede ser recomendable añadir un grupo o usuario administrador para la gestión Samba. 

Crearemos una carpeta compartida global, la llamaremos ``tolmundo``, también otra en ``/home/compartidoNFS``:

.. code-block:: console
    
    user@server:~$ sudo mkdir -p /samba/tolmundo
    user@server:~$ sudo mkdir -p /home/compartidoNFS


Añadiremos la siguiente sección al archivo ``/etc/samba/smb.conf`` para activar estas comparticiones:

.. code-block:: 

    [tolmundo]
        path = /samba/tolmundo
        browseable = yes
        read only = no
        force create mode = 0660
        force directory mode = 2770
        valid users = @sambashare user
    [compartidoNFS]
        path = /home/compartidoNFS
        browseable = yes
        read only = no
        force create mode = 0660
        force directory mode = 2770
        valid users = @sambashare juan marta

Iniciar el servicio
======================

Para iniciar el servicio ejecutamos:

.. code-block:: console
    
    user@server:~$ sudo systemctl start smbd.service

También debemos permitir el acceso a través del Firewall:

.. code-block:: console
    
    user@server:~$ sudo ufw allow samba

Conexión a carpeta
===================

Para conectarnos a la carpeta usamos ``smb://<IP-del-Servidor>/<Recurso>``, en Linux. En Windows abriremos el explorador de archivos y escriremos ``\<IP-del-Servidor>/<Recurso>``.

Veamos un ejemplo en Linux:

.. image :: ../images/servicio/samba-1.png
   :width: 500
   :align: center
   :alt: Conexión a la carpeta compartida
|br|

.. |br| raw:: html

   <br />