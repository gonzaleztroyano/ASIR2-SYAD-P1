##############
Servidor NFS
##############

Instalar servidor NFS
=====================

Actualizamos los paquetes disponibles en los repositorios e instalamos, si no lo estuviera ya, el paquete. 

.. code-block:: console

    pablo@server:$/ sudo apt update
    pablo@server:$/ sudo apt install nfs-common


Configuración NFS
===================

Crear carpeta nueva
----------------------

Crearemos una carpeta en el RAID1, que será la que compartiremos después:

.. code-block:: console

    pablo@server:$/ sudo mkdir /mnt/md0/compartidoNFS -p


Si ahora vemos los permisos, nos daremos cuenta de que el propietario de la carpeta es ``root:root``. Por seguridad, NFS realiza las acciones con las credenciales ``nobody:nogroup``. Para que los permisos de la carpeta coincidan con los que utilizará NFS, cambiaremos los mismos:

.. code-block:: console

    pablo@server:$/ sudo chown nobody:nogroup /mnt/md0/compartidoNFS

Añadir comparticiones
-----------------------

Editaremos el archivo ``/etc/exports``, añadiendo:

.. code-block::

    /mnt/md0/compartidoNFS 192.168.56.102(rw,sync,no_root_squash,no_subtree_check)
    /mnt/md0/compartidoNFS 192.168.56.0/24(r,sync,no_subtree_check)




Reiniciaremos el archivo
-------------------------

.. code-block:: console

    pablo@server:$/ sudo systemctl restart nfs-kernel-server


Configuración del cliente
==========================

Crear los puntos de montaje:

pablo@cliente:$/ sudo mkdir -p /nfs/compartidoNFS
