*****************************
Configuración de RAID inicial
*****************************

.. note::

    La interfaz se encuentra en inglés.


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

Para crear el RAID:


(Aquí iría el vídeo 1 de verdad)

Crear el sistema de archivos:

(Aquí iría el vídeo 1 )


RAID 5 - SIN
=============

Para crear el RAID5 y el sistema de archivos seguimos los siguientes pasos. También hemos creado la carpeta compartida para el *home*:

(Aquí iría el vídeo 2)

Crear usuario
==============

Para crear un usuario seguimos los siguientes pasos:

1. Navegamos desde el menú lateral hasta *Users*
2. Hacemos clic, en el menú superior, en la opción *Add*.
3. Rellenamos los datos necesarios para la creación del usuario:   
    3.1. Configuramos el nombre para el usuario
    3.2. Escribimos un correo electrónico para el usaurio
    3.3. Definimos una contraseña (*Clave_00* en nuestro caso) para el usaurio.
    3.4. Definimos una *shell* para nuestro usuario. Como no queremos que pueda iniciar sesión mediante SSH seleccionamos ``/usr/sbin/nologin`` .
4. Hacemos clic en *Save*. Aplicamos los cambios.



Configurar la carpeta *home*
-----------------------------

Debemos indicar a OpenMediaVault dónde se van a guardar los datos del *home* de los usuarios. Para hacerlo:

1. Navegamos desde el menú lateral hasta *Users*
2. En la barra superior seleccionamos *Settings*
3. Aquí marcamos *Enable*
4. Seleccionamos la carpeta compartida *home* que hemos creado anteriormente.
5. Hacemos clic en *Save*. Aplicamos los cambios.
