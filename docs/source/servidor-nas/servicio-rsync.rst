################
Servicio Rsync
################

Configuración del servicio
===========================

.. note::

    La interfaz se encuentra en Inglés.

Para acceder a la configuración del servicio Rsync debemos navegar desde el menú izquierdo a Services > Rsync.

Aquí, en la parte superior, vemos dos pestañas: *Jobs* y *Server*. Seleccionamos *Server* para configurarlo. 

*Jobs* para configurar trabajos como **cliente** Rsync y *Server* para que OpenMediaVault actúe como **servidor** Rsync ofreciendo módulos a clientes. 

Dentro de *Server* hay dos opciones: *Settings* y *Modules*. En la "jerga" de Rsync, los módulos son las carpetas compartidas

Para **activar el servicio Rsync** debemos marcar el interruptor. El puerto lo mantendremos en el por defecto. 

Al igual que con SSH, podemos añadir opciones extra no contempladas en la GUI. Las posibles modificaciones están recogidas en `este enlace <http://www.samba.org/ftp/rsync/rsyncd.conf.html>`_.


Habilitar módulo
=================

Para gestionar los módulos ("carpetas compartidas") de Rsync, debemos navegar hasta *Services > Rsync > Server > Modules*. 

Hacemos clic en *Add* y completamos los datos que nos solicita la interfaz:

.. image :: ../images/nas/nas41-rsync.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|


En esta misma ventana, desde la pestaña *Users* añadimos a nuestro usuario. (Si no lo hacemos no dejará guardarlo. Eso sí, no nos avisará de cuál es el error).

.. |br| raw:: html

   <br />

Conexión desde el cliente
===========================

Desde el equipo cliente:

.. code-block:: console
        
    user@server-carpet:~$ rsync ^C
    user@server-carpet:~$ mkdir ./prueba
    user@server-carpet:~$ echo "Hola esto es una prueba" > prueba/hola.txt

    user@server-carpet:~$ rsync -avh ./prueba user@nas.corp.carpet4you.site::home
    Password: # [Introducimos contraseña]
    sending incremental file list
    prueba/
    prueba/hola.txt

    sent 164 bytes  received 39 bytes  81.20 bytes/sec
    total size is 24  speedup is 0.12
