****************************
RAID en Windows Server 2019
****************************

Configuración de la MV
=======================

Se utilizará una máquina virtual con Windows Server 2019 como sistema operativo. Se le asignan 4 GB de RAM y 4 vCPUs. 
En tanto a la red, se configuran 1 adaptadores virtual:
 * Adaptador 1, configurado en modo NAT para la conexión a internet. 

En tanto al usuario administrador utiliza la (poco segura) combinación administrador:Clave_00.

Se añaden 8 discos virtuales a la máquina:

    * El disco principal de 50GB, donde almacenaremos el sistema operativo. 
    * 7 discos de 5GB que utilizaremos para configurar los sistemas RAID.



.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/raid/raid1.png" alt="Imagen en la que se pueden ver los discos virtuales conectados a la máquina">
    </div>


Sistema RAID0 - Stripped
=======================

Si estuviéramos reutilizando discos debiéramos utilizar diskpart para limpiar todas las particiones. O utilizar el Administrador de Discos (que puede ser bastante más lento si tenemos varias particiones).

Para configurar el sistema RAID 0 lo primero que debemos hacer es inicializar los discos. 
Para ello, hacemos clic sobre uno de ellos y seleccionamo *Inicializar disco*. Al hacerlo debemos seleccionar los discos que queremos que formen parte del RAID. 

En nuestro caso seleccionamo *Disco 1* y *Disco 2*, utilizamos GPT como formato de partición para no tener limitaciones en tanto a particiones que sí podríamos llegar a tener con MBR. 

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/raid/raid2.png" alt="Imagen en la que se puede ver cómo inicializar un disco desde el administrador de Discos de Windows">
    </div>


Después debemos convertir los discos a discos dinámicos. Para hacerlo, basta con seleccionar el disco correspondiente, hacer clic derecho sobre el nombre y marcar la opción *Convertir en disco dinámico*. Al igual que cuando hemos incializado los discos, el asistente nos permite convertir varios en un mismo paso. Seleccionamos ambos discos con los que estamos trabajando. 


Para crear y formatear el RAID0 podemos segur los pasos descritos en `este vídeo <https://www.loom.com/embed/be68eb9e04394a1e9ebe60d27d05286f>`_:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <div style="position: relative; padding-bottom: 68.5546875%; height: 0;"><iframe src="https://www.loom.com/embed/be68eb9e04394a1e9ebe60d27d05286f" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </div>

Sistema RAID1 - Espejo
=======================

Para configurar el sistema RAID 1 lo primero que debemos hacer es inicializar los discos. 
Para ello, hacemos clic sobre uno de ellos y seleccionamo *Inicializar disco*. Al hacerlo debemos seleccionar los discos que queremos que formen parte del RAID. 

En nuestro caso seleccionamo *Disco 3* y *Disco 5* (debido a un error en la creación el disco 4 tiene solo 500MB en lugar ed 5GB), utilizamos GPT como formato de partición para no tener limitaciones en tanto a particiones que sí podríamos llegar a tener con MBR. 

En el `siguiente vídeo <https://www.loom.com/embed/dbefee751fc94b9f8773d0ea2e74b2a1>`_ podemos ver el proceso completo de inicialización de los discos y configuración del RAID1 en espejo. 

.. raw:: html

     <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <div style="position: relative; padding-bottom: 68.5546875%; height: 0;"><iframe src="https://www.loom.com/embed/dbefee751fc94b9f8773d0ea2e74b2a1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </div>


Sistema RAID5 - Distribuido
============================

Para configurar el sistema RAID 5 lo primero que debemos hacer es inicializar los discos. 
Para ello, hacemos clic sobre uno de ellos y seleccionamo *Inicializar disco*. Al hacerlo debemos seleccionar los discos que queremos que formen parte del RAID. 

En nuestro caso seleccionamo *Disco 6*, *Disco 7* y *Disco 8* (debido a un error en la creación el disco 4 tiene solo 500MB en lugar ed 5GB), utilizamos GPT como formato de partición para no tener limitaciones en tanto a particiones que sí podríamos llegar a tener con MBR. 

En el `siguiente vídeo <https://www.loom.com/embed/6726d53eb66c4530a9452854ef2b2f67>`_ podemos ver cómo crear un volumen RAID5:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <div style="position: relative; padding-bottom: 68.5546875%; height: 0;"><iframe src="https://www.loom.com/embed/6726d53eb66c4530a9452854ef2b2f67" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </div>


Resultado
===========

En la siguiente imagen podemos ver el resultado de los pasos mostrados en esta página:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/raid/raid3.png" alt="Imagen en la que se puede ver cómo inicializar un disco desde el administrador de Discos de Windows">
    </div>