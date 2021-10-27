##################
Servicio SMB/CIFS
##################

.. note::

    La interfaz se encuentra en Inglés.


Crear carpeta
=============

Crearemos la carpeta *SMB-Carpet4You* y la compartiremos con nuestro usuario. 

Para hacerlo, seguiremos los siguientes pasos:

#. Entramos al panel de control web de OMV.
#. En el menú de la izquierda, seleccionamos *Shared folders*. Hacemos clic en *Add* para crear una nueva carpeta compartida. 
#. Escribimos los detalles de la nueva carpeta que estamos creando: nombre (*SMB-Carpet4You*). Seleccionamos el sistema de archivos deseado, *RAID5FS*. En Path, si no se autocompleta, introduciremos el valor deseado. 
#. Hacemos clic en guardar. Salvamos los cambios desde el botón de la parte superior. 

Permisos de carpeta
====================

Ya con la carpeta creada, debemos dar permisos a los usuarios para que puedan acceder y/o editar el contenido de la misma. 

Debemos tener en cuenta que tenemos dos controles de acceso: el sistema de permisos POSIX del propio Linux y el ACL de la carpeta compartida. 

Para modificar los permisos de ACL, seleccionamos la carpeta compartida y después hacemos clic en *ACL*. 

En el menú superior, marcamos que *usuario* tenga acceso a la carpeta. Además, le hacemos propietario de la misma. También damos permisos al grupo. 

Seleccionamos que los permisos sean recursivos.


Configurar servicio SMB
=======================

En el menú de la izquierda, seleccionamos el servicio SMB/CIFS. 

Por defecto está apagado, *encendemos* el interruptor. Activamos los directorios *home* de los usuarios. 

Por seguridad, marcamos la opción de registrar la actividad de los usuarios. 


Compartir una carpeta por SMB
-----------------------------

En la misma pantalla en la que nos encontrábamos, seleccionamos *Shares* en la parte superior de la pantalla. Hacemos clic en *Add*.

Marcamos la compartición como activada, en *Shared folder* marcamos la carpeta que hemos creado previamente, *SMB-Carpet4You*. 

No cambiamos ningún parámetro más. Hacemos clic en Save y aplicamos los cambios. 


Acceder a la carpeta compartida
================================

Desde nuestra máquina escribimos ``smb://nas.corp.carpet4you.site``.

Nos pedirá el usuario y contraseña. 



.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/nas/nas28.png" alt="Captura de pantalla durante la importación del certificado.">
    </div>
