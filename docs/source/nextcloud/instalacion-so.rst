################################
Instalación de Sistema Operativo
################################

Configuración de la MV
========================

Llamaremos a la máquina virtual *ASIR2.SYAD.P1.NextCloud*. Será tipo Linux, versión Ubuntu 20.04 64bits. Asignaremos 4GB de memoria RAM y no añadiremos durante la creación ningún disco duro, pues lo haremos después.

En tanto a la red, se configuran 2 adaptadores virtuales:
 * Adaptador 1, configurado en modo NAT para la conexión a internet. 
 * Adaptador 2, confiugrado en modo solo-anfitrión, para la conexión vía web y a los servicios.


Sobre los discos, se crean los siguientes discos virtuales:
 * 1 disco duro virtual de 10 Gb, que será donde instalaremos el arranque. 
 * 2 discos duros virtuales de 50 Gb. En estos instalaremos el sistema operativo, configurándolos en RAID 1 para la instalación del SO. 
 * 3 discos duros virtuales de 200 Gb. Sobre estos configuraremos RAID 5 para alojar los datos. 

Configuración RAID 0 para SO
-----------------------------

Puesto que considero bastante interesante la configuración del RAID 0 durante la instación, lo incluiremos en esta guía. Puede ser muy útil `esta guía <https://askubuntu.com/questions/1066028/install-ubuntu-18-04-desktop-with-raid-1-and-lvm-on-machine-with-uefi-bios>`_

Llegados a la siguiente pantalla, hacemos clic en *Custom storage layout*:

.. image :: ../images/nextcloud/nc-1.png
   :width: 500
   :align: center
|br|

Marcamos que queremos configurar un RAID:

.. image :: ../images/nextcloud/nc-2.png
   :width: 500
   :align: center
|br|


En la configuración del RAID, seleccionamos el nivel de RAID deseado y los discos destino. 

.. image :: ../images/nextcloud/nc-3.png
   :width: 500
   :align: center
|br|

De nuevo en el resumen de discos, en el menú del RAID, hacemos clic en formatear. Utilizamos ext4 como sistema de archivos y */* como punto de montaje. 

.. image :: ../images/nextcloud/nc-4.png
   :width: 500
   :align: center
|br|

También aprovecharemos para crear el RAID 5 para los datos: 

.. image :: ../images/nextcloud/nc-5.png
   :width: 500
   :align: center
|br|

Indicamos que sea el disco de 10 Gb el que se utilizará para el *boot device*. También indicamos que el RAID 5 sea utilizado para los datos, y montado en la ruta ``/nc-data``:

.. image :: ../images/nextcloud/nc-6.png
   :width: 500
   :align: center
|br|

El resultado de los discos es el siguiente:

.. image :: ../images/nextcloud/nc-7.png
   :width: 500
   :align: center
|br|

.. Se configura user:user. cloud como hostname

.. error::

   Tras la segunda vez dando error en la instalación, se instala en un solo disco, sin RAID:
     
      .. image :: ../images/nextcloud/nc-8.png
         :width: 500
         :align: center
|br|

.. |br| raw:: html

   <br />
