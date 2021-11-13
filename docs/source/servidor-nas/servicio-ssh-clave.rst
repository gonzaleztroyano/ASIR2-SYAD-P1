#####################################################
Servicio SSH autenticado con clave pública-privada
#####################################################

Configuración del servicio
===========================

.. note::

    La interfaz se encuentra en Inglés.

Para acceder a la configuración del servicio SSH debemos navegar desde el menú izquierdo a Services > SSH.

Ya hemos visto en el apartado alterior algunas de las modificaciones que podíamos realizar. Para esta práctica vamos a activar la autenticación SSH mediante infraestructura de clave pública. 

En el apartado de configuración debemos modificar algunos ajustes:

* Desactivar la autenticación por contraseña. Solo queremos que se pueda iniciar sesión utilizando la clave pública. 
* Activar, si no lo estuviera ya el interruptor de *Public Key Authentication*. 

.. tip:: 
    
    Es altamente recomendable cambiar el puerto por uno no estándar. En este caso no se va a realizar, aunque es un *must-do* para añadir una capa de seguridad adicional a nuestro servidor. Al igual que deshabilitar el usaurio root.
    
    Cabe una mención especial a la posibilidad de activar la autenticación en dos factores para SSH. A través de `este enlace <https://ubuntu.com/tutorials/configure-ssh-2fa#1-overview>`_ se puede obtener más información.


Una vez realizadas las modificaciones desde la interfaz web, guardamos los cambios y los aplicamos. 


Generación de claves
=====================

Usaremos el usuario "user" para este ejercicio. 

Para generar un par de claves nuevo debemos utilizar el siguientes comando:

.. code-block:: console
    
    pablo@carpet:~$ ssh-keygen -t rsa
        Generating public/private rsa key pair.
        Enter file in which to save the key (/home/user/.ssh/id_rsa): user
        Enter passphrase (empty for no passphrase):
        Enter same passphrase again:
        Your identification has been saved in user.
        Your public key has been saved in user.pub.
        The key fingerprint is:
        SHA256:J4Fc6i7vVuZNatQmOxlKGGSyR4Ax0mluvHyhEBLyxAE user@server-carpet
        The key's randomart image is:
        +---[RSA 2048]----+
        |EB++    .        |
        |*+* +. +         |
        |.=.*  + .        |
        |. = +.   .       |
        | + + +. S..      |
        |  + o.. *o+      |
        |   ....* X       |
        |     oo B .      |
        |     oo. .       |
        +----[SHA256]-----+


        # Movemos las claves a la carpeta .ssh de nuestro equipo cliente para tenerlas localizadas. 
        user@carpet:~$ mv user .ssh/
        user@carpet:~$ mv user.pub .ssh/


OpenMediaVault necesita que la clave pública sea introducida en un formato consecuente con el estandar RFC4716. Después de crearla necesitamos ejecutar el siguiente comando:

.. code-block:: console
    
    pablo@carpet:~$ ssh-keygen -e -f ~/.ssh/user.pub
        ---- BEGIN SSH2 PUBLIC KEY ----
        Comment: "2048-bit RSA, converted by user@server-carpet from OpenSSH"
        AAAAB3NzaC1yc2EAAAADAQABAAABAQC+cdESzhtIoTq0xWrUeQNYg6VkMOg1cNj7TDC+fX
        XIPdj10TFmitQ7if5PgcyOVPccEJ9TF2+lCcAbgPSNxUjptY+IjV39exucVUN1hdRRxxBQ
        Ol6YDiG4CND5oMUqyHFzYR7Oornh+hkaw89MOzRU/K9xRsYoRmrK8BeYE4gxsyeCA5vNf8
        Z2imukgOF3u7/zvQF3Z4oZYkGG2X8qFlgS1bfmwZ7kjT0JFjtEd6+gIUUuZpI0s3SOpX81
        5doJQS0gSHFJj4Qo9MhjvnIVVd1Og0arZsKXysCZnEKQuFYEVWmH7dcWgIDH2aHeZ9LtEO
        7JcBu1DblYwgcFqiF8T0mP
        ---- END SSH2 PUBLIC KEY ----




Añadir claves al perfil del usuario
====================================

Debemos copiar la clave pública generada en el paso anterior. Es importante copiar la salida del comando de transformación (``ssh-keygen -e -f ~/.ssh/user.pub``) y no el contenido iniciar del archivo. 


.. image :: ../images/nas/nas38-ssh.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|

Para añadir la clave al perfil del usaurio nos desplazamos en el menú de la izquierda al apartado *Users*. Aquí, hacemos doble clic sobre el usuario que queremos modificar para acceder a sus ajustes. 

Una vez en la ficha debemos hacer clic sobre la pestaña *Public Keys* (identificador *1* en la imagen). Aquí haremos clic en *Add* para añadir una nueva (identificador *2* en la imagen). 

En el nuevo cuadro de diálogo quee nos muestra la aplicación debemos introducir la clave pública en el formato RFC4716. Si no lo hacemos así ni siquiera nos permitirá guardar la nueva clave. 

Es importante también comprobar que el usuario forma parte del grupo ``ssh``. De lo contrario, se le denegará el acceso. 

Una vez introducida, hacemos clic en *Save*. Guardamos el usuario, los cambios y los aplicamos para que surtan efecto en el sistema. 


Inicio de sesión remoto con clave
==================================

.. code-block:: console
    
    pablo@carpet:~$ ssh user@nas.corp.carpet4you.site -i .ssh/user
        The authenticity of host 'nas.corp.carpet4you.site (192.168.56.113)' can't be established.
        ECDSA key fingerprint is SHA256:gLGmOzGi1mWOOKmf6dhc7xH2Ttm+ostwtN/cERjrrz0.
        Are you sure you want to continue connecting (yes/no)? yes
        Warning: Permanently added 'nas.corp.carpet4you.site,192.168.56.113' (ECDSA) to the list of known hosts.
        #[Aquí da un error "feo" que procederemos a solucionar a continuación]

¡ERROR ENCONTRADO!

..  error::
    | Hay un bug en OpenMediaVault al realizar la importación desde la GUI web. 
    | Más información en `este enlace <https://github.com/openmediavault/openmediavault/issues/160>`_
    | En mi caso, los *logs* del error generado se encuentran en `este otro enlace <https://github.com/openmediavault/openmediavault/issues/160#issuecomment-955204680>`_

    | En la *issue* se comenta también un error de permisos:

        .. image :: ../images/nas/nas39-ssh.png
            :width: 500
            :align: center
            :alt: Añadir clave púb
        |br|

    Viendo los *logs*, parece que además de la ruta ``/var/lib/openmediavault/ssh/authorized_keys/user`` (donde se genera el error de permisos, ``Authentication refused: bad ownership or modes for directory /``)  intenta buscar la clave pública en el siguiente archivo: ``/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys``.

    Vamos a probar a añadir a esta ruta la clave. Antes de nada, debemos crear el directorio ``.ssh/``, pues este no existe en el home del usuario. Aquí debemos crear el archivo ``authorized_keys``. 
    
    Copiaremos el archivo ``/var/lib/openmediavault/ssh/authorized_keys/user`` al nuevo archivo y reiniciamos el servicio SSH.

        .. code-block:: console
    
            root@nas: cp /var/lib/openmediavault/ssh/authorized_keys/user /srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys

    Por defecto el archivo tiene los permisos ``-rw-------`` y esto nos dará (me ha dado, de hecho) problemas a continuación. Los cambiaremos con el comando ``chmod 644 authorized_keys`` a ``-rw-r--r--``.

    También debe ser el usuario el propietario del archivo, como podemos ver en `este enlace <https://help.ubuntu.com/community/SSH/OpenSSH/Keys#:~:text=The%20authorized_keys%20file%20should%20have,be%20owned%20by%20the%20user.&text=The%20next%20time%20you%20connect,have%20to%20enter%20your%20password.>`_. Para hacerle propietario utilizamos el comando ``chown user:users authorized_keys``.

    Ahora en los *logs* si probamos la conexión de nuevo podemos ver "cosas" diferentes que tiene "mucha mejor pinta":

        .. code-block:: console

            Oct 30 15:24:53 nas sshd[16530]: debug1: trying public key file /srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys
            Oct 30 15:24:53 nas sshd[16530]: debug1: fd 4 clearing O_NONBLOCK
            Oct 30 15:24:53 nas sshd[16530]: debug1: /srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys:1: matching key found: RSA SHA256:wpOSevL3o4r9SNzrh0WDGhlXb1aHzgfS+ZB29YkRofI
            Oct 30 15:24:53 nas sshd[16530]: debug1: /srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
            Oct 30 15:24:53 nas sshd[16530]: Accepted key RSA SHA256:wpOSevL3o4r9SNzrh0WDGhlXb1aHzgfS+ZB29YkRofI found at /srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys:1
            Oct 30 15:24:53 nas sshd[16530]: debug1: restore_uid: 0/0
            Oct 30 15:24:53 nas sshd[16530]: Postponed publickey for user from 192.168.56.109 port 54142 ssh2 [preauth]
            Oct 30 15:24:59 nas sshd[16530]: debug1: userauth-request for user user service ssh-connection method publickey [preauth]
            [...]
            Oct 30 15:24:59 nas sshd[16530]: debug1: PAM: establishing credentials
            Oct 30 15:24:59 nas sshd[16530]: pam_unix(sshd:session): session opened for user user by (uid=0)


En el terminal cliente podemos ver la conexión establecida:

.. image :: ../images/nas/nas40-ssh.png
    :width: 500
    :align: center
    :alt: La conexión está funcionando
|br|


.. |br| raw:: html

   <br />