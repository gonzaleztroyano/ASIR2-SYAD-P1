*********************************
RAID en Linux Ubuntu Server 18.04
*********************************

Configuración de la MV
=======================

Se utilizará una máquina virtual con Windows Server 2019 como sistema operativo. Se le asignan 4 GB de RAM y 4 vCPUs. 
En tanto a la red, se configuran 1 adaptadores virtual:
 * Adaptador 1, configurado en modo NAT para la conexión a internet. 

En tanto al usuario administrador utiliza la (poco segura) combinación *user:user*.

Se añaden 9 discos virtuales a la máquina:

    * El disco principal de 50GB, donde almacenaremos el sistema operativo. 
    * 8 discos de 5GB que utilizaremos para configurar los sistemas RAID.

La configuración por tanto es la siguiente:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/raid/raid4.png" alt="Imagen en la que se pueden ver los discos virtuales conectados a la máquina">
    </div>


Una vez hemos arrancado la máquina podemos utilizar el comando *lsblk* para ver la lista de dispositivos conectados al equipo.

.. code-block:: console

    user@server-carpet:~$ lsblk 
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    loop0    7:0    0 88,5M  1 loop /snap/core/7270
    sda      8:0    0  160G  0 disk 
    ├─sda1   8:1    0    1M  0 part 
    ├─sda2   8:2    0    4G  0 part [SWAP]
    └─sda3   8:3    0  156G  0 part /
    sdb      8:16   0    5G  0 disk 
    sdc      8:32   0    5G  0 disk 
    sdd      8:48   0    5G  0 disk 
    sde      8:64   0    5G  0 disk 
    sdf      8:80   0    5G  0 disk 
    sdg      8:96   0    5G  0 disk 
    sdh      8:112  0    5G  0 disk 
    sdi      8:128  0    5G  0 disk 


Para ver el estado de los RAID (gestionado por *mdadm*) utilizamos el siguiente comando:

.. code-block:: console

    user@server-carpet:~$ cat /proc/mdstat
    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
    unused devices: <none>

Como podemos ver, no tenemos (de momento) ninguno configurado. 


RAID0 - Stripped
=================

Creación del array
------------------

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --create --verbose \ 
    /dev/md0 --level=0 --raid-devices=2 /dev/sdb /dev/sdc

    mdadm: chunk size defaults to 512K
    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md0 started.


Las opciones de este comando son:

* **mdadm**, es el comando en sí, nos sirve para gestionar toda la configuración relativa a RAIDs. 
* **--create**, indicamos a *mdadm* que queremos crear uno nuevo, puesto que también podríamos borrarlos o modificarlos. 
* **--verbose**, para que nos muestre detalles sobre las acciones que está realizando. 
* **/dev/md0**, este es el dispositivo de bloque que vamos a crear.
* **/--level=0**, nivel de RAID con el que vamos a configurar el nuevo dispositivo lógico. 
* **--raid-devices=2**, número de dispositivos que vamos a agregar al RAID. 
* **/dev/sdb /dev/sdc**, los dispositivos que vamos a utilizar. 


Si ahora vemos la información de *mdstat* veremos el nuevo dispositivo creado. 

.. code-block:: console

    user@server-carpet:~$ cat /proc/mdstat
    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
    md0 : active raid0 sdc[1] sdb[0]
        10475520 blocks super 1.2 512k chunks
    unused devices: <none>



Crear sistema de archivos y montar
----------------------------------

Creamos el sistema de archivos en el nodo RAID;

.. code-block:: console

    user@server-carpet:~$ sudo mkfs.ext4 -F /dev/md0
        mke2fs 1.44.1 (24-Mar-2018)
        Creating filesystem with 2618880 4k blocks and 655360 inodes
        Filesystem UUID: 0d3d57e0-8bf2-4d1e-8289-c3996ecdf606
        Superblock backups stored on blocks: 
                32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

        Allocating group tables: done                            
        Writing inode tables: done                            
        Creating journal (16384 blocks): done
        Writing superblocks and filesystem accounting information: done 



Creamos la carpeta donde montaremos el sistema de archivos:

.. code-block:: console

    user@server-carpet:~$ sudo mkdir -p /mnt/md0


Montamos el dispositivo RAID en nuestro sistema de archivos:

.. code-block:: console

    user@server-carpet:~$ sudo mount /dev/md0 /mnt/md0


Comprobaciones
--------------

Para ver el sistema de archivos resultante podemos ejecutar el siguiente comando:

.. code-block:: console

    user@server-carpet:~$ df -h /dev/md0 
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/md0        9,8G   37M  9,3G   1% /mnt/md0


Automontaje en inicio
----------------------

Para estar seguros de que al reiniciar el equipo el sistema reconoce el RAID con las mismas características debemos  actualizar el archivo ``/etc/mdadm/mdadm.conf``

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
    ARRAY /dev/md0 metadata=1.2 name=server-carpet:0 UUID=5f784e4c:b5877144:918ac136:c341cb10


También debemos actualizar ``initframs``, que es el archivo de RAM que se carga durante el arranque del sistema:

.. code-block:: console
    
    user@server-carpet:~$ sudo update-initramfs -u


Por último, debemos actualizar el archivo ``/etc/fstab``:

.. code-block:: console
    
    user@server-carpet:~$ echo '/dev/md0 /mnt/md0 ext4 defaults,nofail,discard 0 0' | sudo tee -a /etc/fstab


RAID1 - Espejo
===============

Creación del array
------------------

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --create --verbose \
    /dev/md0 --level=1 --raid-devices=2 /dev/sdd /dev/sde


    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md1 started.


Las opciones de este comando son:

* **mdadm**, es el comando en sí, nos sirve para gestionar toda la configuración relativa a RAIDs. 
* **--create**, indicamos a *mdadm* que queremos crear uno nuevo, puesto que también podríamos borrarlos o modificarlos. 
* **--verbose**, para que nos muestre detalles sobre las acciones que está realizando. 
* **/dev/md1**, este es el dispositivo de bloque que vamos a crear.
* **/--level=1**, nivel de RAID con el que vamos a configurar el nuevo dispositivo lógico. 
* **--raid-devices=2**, número de dispositivos que vamos a agregar al RAID. 
* **/dev/sdd /dev/sde**, los dispositivos que vamos a utilizar. 


Si ahora vemos la información de *mdstat* veremos el nuevo dispositivo creado. 

.. code-block:: console

    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
    md1 : active raid1 sde[1] sdd[0]
      5237760 blocks super 1.2 [2/2] [UU]
      
    md0 : active raid0 sdc[1] sdb[0]
      10475520 blocks super 1.2 512k chunks
      
    unused devices: <none>

Crear sistema de archivos y montar
----------------------------------

Creamos el sistema de archivos en el nodo RAID;

.. code-block:: console

    user@server-carpet:~$ sudo mkfs.ext4 -F /dev/md1
        mke2fs 1.44.1 (24-Mar-2018)
        Creating filesystem with 1309440 4k blocks and 327680 inodes
        Filesystem UUID: 5f929cc1-7c5e-4107-a71a-e9cbb296c5f3
        Superblock backups stored on blocks: 
                32768, 98304, 163840, 229376, 294912, 819200, 884736

        Allocating group tables: done                            
        Writing inode tables: done                            
        Creating journal (16384 blocks): done
        Writing superblocks and filesystem accounting information: done
        


Creamos la carpeta donde montaremos el sistema de archivos:

.. code-block:: console

    user@server-carpet:~$ sudo mkdir -p /mnt/md1


Montamos el dispositivo RAID en nuestro sistema de archivos:

.. code-block:: console

    user@server-carpet:~$ sudo mount /dev/md1 /mnt/md1


Comprobaciones
--------------

Para ver el sistema de archivos resultante podemos ejecutar el siguiente comando:

.. code-block:: console

    user@server-carpet:~$ df -h /dev/md1
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/md1        4,9G   20M  4,6G   1% /mnt/md1

Automontaje en inicio
----------------------

Para estar seguros de que al reiniciar el equipo el sistema reconoce el RAID con las mismas características debemos  actualizar el archivo ``/etc/mdadm/mdadm.conf``

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
    ARRAY /dev/md0 metadata=1.2 name=server-carpet:0 UUID=5f784e4c:b5877144:918ac136:c341cb10

    ARRAY /dev/md1 metadata=1.2 name=server-carpet:1 UUID=089e4962:1c5da6a4:6fd12683:de775a6c



También debemos actualizar ``initframs``, que es el archivo de RAM que se carga durante el arranque del sistema:

.. code-block:: console
    
    user@server-carpet:~$ sudo update-initramfs -u


Por último, debemos actualizar el archivo ``/etc/fstab``:

.. code-block:: console
    
    user@server-carpet:~$ echo '/dev/md1 /mnt/md1 ext4 defaults,nofail,discard 0 0' | sudo tee -a /etc/fstab


RAID5 - Espejo
===============

Creación del array
------------------

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --create --verbose \
    /dev/md2 --level=5 --raid-devices=4 /dev/sdf /dev/sdg /dev/sdh /dev/sdi

    mdadm: layout defaults to left-symmetric
    mdadm: layout defaults to left-symmetric
    mdadm: chunk size defaults to 512K
    mdadm: size set to 5237760K
    mdadm: Defaulting to version 1.2 metadata
    mdadm: array /dev/md2 started.



Las opciones de este comando son:

* **mdadm**, es el comando en sí, nos sirve para gestionar toda la configuración relativa a RAIDs. 
* **--create**, indicamos a *mdadm* que queremos crear uno nuevo, puesto que también podríamos borrarlos o modificarlos. 
* **--verbose**, para que nos muestre detalles sobre las acciones que está realizando. 
* **/dev/md2**, este es el dispositivo de bloque que vamos a crear.
* **/--level=5**, nivel de RAID con el que vamos a configurar el nuevo dispositivo lógico. 
* **--raid-devices=4**, número de dispositivos que vamos a agregar al RAID. 
* **/dev/sdf /dev/sdg /dev/sdh /dev/sdi**, los dispositivos que vamos a utilizar. 


Si ahora vemos la información de *mdstat* veremos el nuevo dispositivo creado. 

.. code-block:: console

    Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
    md2 : active raid5 sdi[4] sdh[2] sdg[1] sdf[0]
        15713280 blocks super 1.2 level 5, 512k chunk, algorithm 2 [4/3] [UUU_]
        [=>...................]  recovery =  6.6% (350524/5237760) finish=4.8min speed=16691K/sec
        
    md1 : active raid1 sde[1] sdd[0]
        5237760 blocks super 1.2 [2/2] [UU]
        
    md0 : active raid0 sdc[1] sdb[0]
        10475520 blocks super 1.2 512k chunks
        
    unused devices: <none>


Crear sistema de archivos y montar
----------------------------------

Creamos el sistema de archivos en el nodo RAID;

.. code-block:: console

    user@server-carpet:~$ user@server-carpet:~$ sudo mkfs.ext4 -F /dev/md2
        mke2fs 1.44.1 (24-Mar-2018)
        Creating filesystem with 3928320 4k blocks and 983040 inodes
        Filesystem UUID: fb134669-8c3e-42a6-b406-53f1a32c91cb
        Superblock backups stored on blocks: 
                32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208

        Allocating group tables: done                            
        Writing inode tables: done                            
        Creating journal (16384 blocks): done
        Writing superblocks and filesystem accounting information: done   


Creamos la carpeta donde montaremos el sistema de archivos:

.. code-block:: console

    user@server-carpet:~$ sudo mkdir -p /mnt/md2


Montamos el dispositivo RAID en nuestro sistema de archivos:

.. code-block:: console

    user@server-carpet:~$ sudo mount /dev/md2 /mnt/md2


Comprobaciones
--------------

Para ver el sistema de archivos resultante podemos ejecutar el siguiente comando:

.. code-block:: console

    user@server-carpet:~$ df -h /dev/md2
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/md2         15G   41M   14G   1% /mnt/md2


Automontaje en inicio
----------------------

Para estar seguros de que al reiniciar el equipo el sistema reconoce el RAID con las mismas características debemos  actualizar el archivo ``/etc/mdadm/mdadm.conf``

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
    ARRAY /dev/md0 metadata=1.2 name=server-carpet:0 
        UUID=5f784e4c:b5877144:918ac136:c341cb10
    ARRAY /dev/md1 metadata=1.2 name=server-carpet:1 
        UUID=089e4962:1c5da6a4:6fd12683:de775a6c
    ARRAY /dev/md2 metadata=1.2 name=server-carpet:2 
        UUID=dc70161b:a4c632d6:fee7cbaa:33c7f703




También debemos actualizar ``initframs``, que es el archivo de RAM que se carga durante el arranque del sistema:

.. code-block:: console
    
    user@server-carpet:~$ sudo update-initramfs -u


Por último, debemos actualizar el archivo ``/etc/fstab``:

.. code-block:: console
    
    user@server-carpet:~$ echo '/dev/md2 /mnt/md2 ext4 defaults,nofail,discard 0 0' | sudo tee -a /etc/fstab


Ver detalles de un RAID
========================

Para ver los detalles de un RAID en Ubuntu podemos utilizar el siguiente comando, indicando el dispositivo de tipo bloque que representa al RAID.

.. code-block:: console

    user@server-carpet:~$ sudo mdadm --detail /dev/md2
    /dev/md2:
            Version : 1.2
        Creation Time : Mon Oct 25 11:41:35 2021
            Raid Level : raid5
            Array Size : 15713280 (14.99 GiB 16.09 GB)
        Used Dev Size : 5237760 (5.00 GiB 5.36 GB)
        Raid Devices : 4
        Total Devices : 4
        Persistence : Superblock is persistent

        Update Time : Mon Oct 25 11:46:20 2021
                State : active 
        Active Devices : 4
    Working Devices : 4
        Failed Devices : 0
        Spare Devices : 0

                Layout : left-symmetric
            Chunk Size : 512K

    Consistency Policy : resync

                Name : server-carpet:2  (local to host server-carpet)
                UUID : dc70161b:a4c632d6:fee7cbaa:33c7f703
                Events : 39

        Number   Major   Minor   RaidDevice State
        0       8       80        0      active sync   /dev/sdf
        1       8       96        1      active sync   /dev/sdg
        2       8      112        2      active sync   /dev/sdh
        4       8      128        3      active sync   /dev/sdi
