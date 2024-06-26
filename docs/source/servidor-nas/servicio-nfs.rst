##############
Servicio NFS
##############

.. note::

    La interfaz se encuentra en Inglés.


Crear carpeta
=============

Crearemos la carpeta *NFS-Carpet4You* y la compartiremos con nuestro usuario. 

Para hacerlo, seguiremos los siguientes pasos:

#. Entramos al panel de control web de OMV.
#. En el menú de la izquierda, seleccionamos *Shared folders*. Hacemos clic en *Add* para crear una nueva carpeta compartida. 
#. Escribimos los detalles de la nueva carpeta que estamos creando: nombre (*NFS-Carpet4You*). Seleccionamos el sistema de archivos deseado, *RAID5FS*. En Path, si no se autocompleta, introduciremos el valor deseado. 
#. Hacemos clic en guardar. Salvamos los cambios desde el botón de la parte superior. 


Permisos de carpeta
====================

Ya con la carpeta creada, debemos dar permisos a los usuarios para que puedan acceder y/o editar el contenido de la misma. 

Debemos tener en cuenta que tenemos dos controles de acceso: el sistema de permisos POSIX del propio Linux y el ACL de la carpeta compartida. 

Para modificar los permisos de ACL, seleccionamos la carpeta compartida y después hacemos clic en *ACL*. 

En el menú superior, marcamos que *usuario* tenga acceso a la carpeta. Además, le hacemos propietario de la misma. También damos permisos al grupo. 

Seleccionamos que los permisos sean recursivos.

Configurar servicio NFS
=======================

En el menú de la izquierda, seleccionamos el servicio NFS. Por defecto está apagado, *encendemos* el interruptor y hacemos clic en *Save*.

En la misma pantalla en la que nos encontrábamos, seleccionamos *Shares* en la parte superior de la pantalla. Hacemos clic en *Add*.


.. image :: ../images/nas/nas31.png
   :width: 500
   :align: center
|br|

Montar carpeta NFS
====================

Para montar la carpeta debemos ejecutar el siguiente comando:


.. code-block:: console

    user@server-carpet:~$ mkdir /mnt/carpet
    user@server-carpet:~$ mount -t nfs4 nas.corp.carpet4you.site:NFS-Carpet4You /mnt/carpet

.. |br| raw:: html

   <br />