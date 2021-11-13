#############
Servicio SSH
#############

Configuración del servicio
===========================

.. note::

    La interfaz se encuentra en Inglés.

Para acceder a la configuración del servicio SSH debemos navegar desde el menú izquierdo a Services > SSH.

Desde aquí podemos cambiar las siguientes opciones:
* Activar o desactivar el servicio utilizando el interruptor. 
* Permitir, o no, el inicio de sesión como root. Lo más recomendable sería deshabilitarlo. 
* Permitir, o no, el inicio la contraseña como método de inicio de sesión; así como el método de clave pública. 
* (Entre otras que no comentaremos, como *tunneling* y compresión).

.. important:: 

    | Como sabemos, las posibles configuraciones SSH son mucho más amplias. Para añadir otras opciones no recogidas en la interfaz directamente podemos utilizar el cuadro de texto *Extra options*. 
    | En este cuadro podemos añadir cualquier de las directivas que acepta el archivo ``/etc/ssh/sshd_config``. Podemos ver una lista completa de dichas directivas en `este enlace <https://man.openbsd.org/sshd_config.5>`_.

    Durante esta práctica se han configurado las siguientes opciones extra:

    .. code-block:: console
        
        Banner "Recuerda que debes usar el servicio SSH con responsabilidad."
        LogLevel VERBOSE
        MaxAuthTries 3
        UseDNS yes


Una vez realizadas las configuraciones, debemos guardarlas y aplicarlas. 

En la siguiente imagen tenemos un ejemplo de configuración:

.. image :: ../images/nas/nas35.png
   :width: 600
   :align: center
   :alt: Ejemplo de configuración de SSH
|br|


Configuración de usuarios
==========================

Podemos gestionar los usuarios del sistema desde *Home* > *Acces Rights management* > *Users*. Aquí veremos una lista de usuarios. Haciendo doble clic sobre su nombre podremos editarlo. 

Para usuario ``usuario`` de forma previa habíamo deshabilitado el acceso ssh y el intérprete de comando lo habíamos fijado como ``/usr/sbin/nologin``. Por tanto, este no podría iniciar sesión. 

Además de revertir estos cambios, es necesario añadir el usuario al grupo *ssh*. Para modificar la pertenencia a grupos del usuario debemos utilizar las segunda pestaña superior en la ficha del usuario. Basta marcar/desmarcar las casillas para modificar este ajuste. 

Utilizando la tercera pestaña superior en la ficha del usuario podemos ver y gestionar las claves públicas de este. 


Conexión al servidor SSH
=========================

Windows
--------

Para la conexión desde Windows utilizaremos el programa *Putty*. Basta con definir el host de conexión (IP o nombre  de dominio) y el puerto. 

Si es la primera vez que nos conectamos veremos el siguiente aviso:

.. image :: ../images/nas/nas36-ssh.png
   :width: 500
   :align: center
   :alt: Aviso new host
|br|


Nos solicitará usuario y contraseña e iniciaremos sesión:


.. image :: ../images/nas/nas37-ssh.png
   :width: 500
   :align: center
   :alt: Aviso new host
|br|


Linux
------

En linux utilizaremos el siguiente comando:

.. code-block:: console

   pablo@carpet:~$ ssh usuario@nas.corp.carpet4you.site

.. |br| raw:: html

   <br />