##############
Servicio FTP
##############

.. note::

    La interfaz se encuentra en Inglés.

Crear carpeta
=============

Crearemos la carpeta *FTP-Carpet4You* y la compartiremos con nuestro usuario. 

Para hacerlo, seguiremos los siguientes pasos:

#. Entramos al panel de control web de OMV.
#. En el menú de la izquierda, seleccionamos *Shared folders*. Hacemos clic en *Add* para crear una nueva carpeta compartida. 
#. Escribimos los detalles de la nueva carpeta que estamos creando: nombre (*FTP-Carpet4You*). Seleccionamos el sistema de archivos deseado, *RAID5FS*. En Path, si no se autocompleta, introduciremos el valor deseado. 
#. Hacemos clic en guardar. Salvamos los cambios desde el botón de la parte superior. 

Permisos de carpeta
====================

Ya con la carpeta creada, debemos dar permisos a los usuarios para que puedan acceder y/o editar el contenido de la misma. 

Debemos tener en cuenta que tenemos dos controles de acceso: el sistema de permisos POSIX del propio Linux y el ACL de la carpeta compartida. 

Para modificar los permisos de ACL, seleccionamos la carpeta compartida y después hacemos clic en *ACL*. 

En el menú superior, marcamos que *usuario* tenga acceso a la carpeta. Además, le hacemos propietario de la misma. También damos permisos al grupo. 

Seleccionamos que los permisos sean recursivos.


Configurar servicio FTP
=======================

En el menú de la izquierda, seleccionamos el servicio FTP. Por defecto está apagado, *encendemos* el interruptor y hacemos clic en *Save*.

En tanto a las modificaciones de configuración debemos:

* Modificar el puerto para usar el 990 (es el que utiliza FTP seguro)
* Activamos SPF pasivo, manteniendo los puertos por defecto.
* Activamos el log de transferencias, para tener un registro en caso de auditoría. 

.. warning::

    Debemos tener en cuenta que los puertos deben estar abiertos. OpenMediaVault lo hace de forma automática. 


En la pestaña *SSL/TLS* modificamos/activamos las siguientes configuraciones:

* Activamos las conexiones SSL/TLS con el interruptor.
* Selecciomos el certificado que queremos utilizar para encriptar las comunicaciones. En nuestro caso, hemos seleccionado el expedido por Let's Encrypt. 
* Marcamos como requerida la conexión segura. 
* Activamos la opción *No session reuse required*.

Guardamos los cambios haciendo clic en el botón *Save*- 

En la misma pantalla en la que nos encontrábamos, seleccionamos *Shares* en la parte superior de la pantalla. Hacemos clic en *Add*.

Seleccionamos la carpeta *FTP-Carpet4You* que hemos creado anteriormente. 

Acceder a la carpeta
=====================

Utilizaremos la aplicación *FileZilla* para acceder a la carpeta compartida. 

.. image :: ../images/nas/nas32.png
   :width: 500
   :align: center
   :alt: Configuración de Filezilla
|br|

Cuando nos conectamos vemos el certificado:

.. image :: ../images/nas/nas33.png
   :width: 500
   :align: center
   :alt: Certificado en Filezilla
|br|

Podemos listar y añadir archivos sin problemas:


.. image :: ../images/nas/nas34.png
   :width: 500
   :align: center
   :alt: Certificado en Filezilla
|br|

.. |br| raw:: html

   <br />