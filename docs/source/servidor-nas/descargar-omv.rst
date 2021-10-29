*************************************
Descargar y comprobar OpenMediaVault
*************************************

Descargar OpenMediaVault
=========================

Podemos descargar dicho sistema operativo desde el siguiente enlace: `https://www.openmediavault.org/download.html <https://www.openmediavault.org/download.html>`_.

En la página anterior veremos un enlace hacia `SourceForge <https://sourceforge.net/projects/openmediavault/files/5.6.13/>`_, donde podremos descargar la ISO y los archivos para la verificación.

Comprobar ISO OpenMediaVault en Ubuntu
=======================================

Suma de comprobación MD5
-------------------------

.. code-block:: console

    user@server-carpet:~$ md5sum -c openmediavault_5.6.13-amd64.iso.md5

    openmediavault_5.6.13-amd64.iso: La suma coincide


Suma de comprobación SHA256
----------------------------

.. code-block:: console

    user@server-carpet:~$ sha256sum -c openmediavault_5.6.13-amd64.iso.sha256

    openmediavault_5.6.13-amd64.sha256: La suma coincide

Comprobación mediante firma 
----------------------------

.. code-block:: console

    user@server-carpet:~$ gpg --import  openmediavault_5.6.13-amd64.iso.key

    user@server-carpet:~$ gpg --verify openmediavault_5.6.13-amd64.iso.asc openmediavault_5.6.13-amd64.iso
        
        gpg: Firmado el mié 25 ago 2021 21:56:54 CEST
        gpg:                usando RSA clave D67506C878E08A94FD7E009424863F0C716B980B
        gpg: Firma correcta de "OpenMediaVault.org (OpenMediaVault packages archive) <packages@openmediavault.org>" [desconocido]
        gpg: ATENCIÓN: ¡Esta clave no está certificada por una firma de confianza!
        gpg:          No hay indicios de que la firma pertenezca al propietario.
        Huellas dactilares de la clave primaria: D675 06C8 78E0 8A94 FD7E  0094 2486 3F0C 716B 980B




Comprobar ISO OpenMediaVault en Windows
=======================================

Una vez ha terminado de descargar el archivo .iso vamos a verificarlo. Para hacerlo, utilizaremos el programa autofirma que tiene capacidad de generar checksums. 



.. image :: ../images/nas/nas1.png
   :width: 500
   :align: center
   :alt: Imagen en la que se pueden ver las opciones de autofirma para la generación de huella digital
|br|

Si tuviéramos la aplicación de 7z instalada también podríamos generar las huellas digitales del archivo .iso. 


.. image :: ../images/nas/nas2.png
   :width: 500
   :align: center
   :alt: Imagen en la que se pueden ver las opciones de 7z para la generación de huella digital.
|br|

Si comparamos las salidas de SHA256 veremos que coinciden:


.. image :: ../images/nas/nas3.png
   :width: 500
   :align: center
   :alt: Imagen en la que se pueden ver las sumas SHA256 generada y descargada
|br|


.. |br| raw:: html

   <br />