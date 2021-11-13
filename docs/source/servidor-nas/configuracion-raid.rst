*****************************
Configuración de RAID inicial
*****************************

.. note::

    | La interfaz se encuentra en inglés.
    | En el caso de consultar la versión PDF, puedes ver los vídeos haciendo clic en los enlaces previos a cada uno. 


El proceso de creación de RAID es medianamente sencillo:

#. Inicializar los discos
#. Crear RAID

    #. Indicando nombre
    #. Seleccionar nivel de RAID
    #. Seleccionar dispositivos 
#. Crear sistema de archivos en dispositivo RAID
#. Montar sistema de archivos RAID
#. (Opcional) Crear carpeta compartida en el sistema de archivos.


RAID 1
=======

Crear el RAID
--------------

Se puede ver la creación del RAID 1 en el `siguiente vídeo <https://www.loom.com/embed/eb3d21be6cdc4f9aadaae1c47ef8a53e>`_:

.. raw:: html
    
    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <div style="position: relative; padding-bottom: 61.1328125%; height: 0;"><iframe src="https://www.loom.com/embed/eb3d21be6cdc4f9aadaae1c47ef8a53e" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </div>

Crear el sistema de archivos:
-----------------------------

Se puede ver la creación del sistema de archivos en el `siguiente vídeo <https://www.loom.com/embed/5fa3796eeccc4636b65a48c9f4d5377c>`_:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <div style="position: relative; padding-bottom: 61.1328125%; height: 0;"><iframe src="https://www.loom.com/embed/5fa3796eeccc4636b65a48c9f4d5377c" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </div>

RAID 5
=============

Para crear el RAID5 y el sistema de archivos seguimos los pasos descritos en el `siguiente víeo <https://www.loom.com/embed/edb151c8f7d441238176dcf1700ad58e>`_. También hemos creado la carpeta compartida para el *home*:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <div style="position: relative; padding-bottom: 61.1328125%; height: 0;">
            <iframe src="https://www.loom.com/embed/edb151c8f7d441238176dcf1700ad58e" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
        </div>
    </div>

Crear usuario
==============

Para crear un usuario seguimos los siguientes pasos:

#. Navegamos desde el menú lateral hasta *Users*
#. Hacemos clic, en el menú superior, en la opción *Add*.
#. Rellenamos los datos necesarios para la creación del usuario:   
    #. Configuramos el nombre para el usuario
    #. Escribimos un correo electrónico para el usuario
    #. Definimos una contraseña (*Clave_00* en nuestro caso) para el usuario.
    #. Definimos una *shell* para nuestro usuario. Como no queremos que pueda iniciar sesión mediante SSH seleccionamos ``/usr/sbin/nologin`` .
#. Hacemos clic en *Save*. Aplicamos los cambios.



Configurar la carpeta *home*
-----------------------------

Debemos indicar a OpenMediaVault dónde se van a guardar los datos del *home* de los usuarios. Para hacerlo:

#. Navegamos desde el menú lateral hasta *Users*
#. En la barra superior seleccionamos *Settings*
#. Aquí marcamos *Enable*
#. Seleccionamos la carpeta compartida *home* que hemos creado anteriormente.
#. Hacemos clic en *Save*. Aplicamos los cambios.
