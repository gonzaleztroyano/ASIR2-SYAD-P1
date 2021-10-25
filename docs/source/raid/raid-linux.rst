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
