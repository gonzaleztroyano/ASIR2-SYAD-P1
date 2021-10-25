***************************************
Recuperación de la información de RAID 
***************************************

Para este apartado vamos a crear una serie de datos en el RAID 5 configurado de forma previa. 

Almacenar datos
===============

Descargamos el libro completo de *El Quijote* varias veces:

.. code-block:: console

    user@server-carpet:~$ wget https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt >> el_quijote.txt


Desconectar disco
==================

Debemos configurar en VirtualBox que nuestros discos son desconectables en caliente. 

Al desconectar desde la interfaz de VirtualBox el disco vemos lo siguiente:


.. code-block:: console

    user@server-carpet:~$ sudo mdadm --detail /dev/md2
    /dev/md2:
            Version : 1.2
        Creation Time : Mon Oct 25 11:41:35 2021
            Raid Level : raid5
            Array Size : 15713280 (14.99 GiB 16.09 GB)
        Used Dev Size : 5237760 (5.00 GiB 5.36 GB)
        Raid Devices : 4
        Total Devices : 3
        Persistence : Superblock is persistent

        Update Time : Mon Oct 25 12:07:43 2021
                State : clean, degraded 
        Active Devices : 3
    Working Devices : 3
        Failed Devices : 0
        Spare Devices : 0

                Layout : left-symmetric
            Chunk Size : 512K

    Consistency Policy : resync

                Name : server-carpet:2  (local to host server-carpet)
                UUID : dc70161b:a4c632d6:fee7cbaa:33c7f703
                Events : 43

        Number   Major   Minor   RaidDevice State
        0       8       80        0      active sync   /dev/sdf
        -       0        0        1      removed
        2       8      112        2      active sync   /dev/sdh
        4       8      128        3      active sync   /dev/sdi
