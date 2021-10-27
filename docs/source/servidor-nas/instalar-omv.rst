************************************
Instalar y configurar OpenMediaVault
************************************

Configuración de la MV
======================

Llamaremos a la máquina virtual *ASIR2.SYAD.P1.OMV-1*. Será tipo Linux, versión Debian 64bits. Asignaremos 4GB de memoria RAM y no añadiremos durante la creación ningún disco duro, pues lo haremos después.

En tanto a la red, se configuran 2 adaptadores virtuales:
 * Adaptador 1, configurado en modo NAT para la conexión a internet. 
 * Adaptador 2, confiugrado en modo solo-anfitrión, para la conexión vía web y a los servicios.


Sobre los discos, se crean los siguientes discos virtuales:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/nas/nas4.png" alt="Imagen en la que se pueden ver los discos duros creados para la MV.">
    </div>


Instalación del SO
==================

La instalación del Sistema Operativo OpenMediaVault es realmente sencilla, de lo que podríamos denominar "Siguiente, Siguiente, Siguiente". Los únicos datos que nos solicita el programa son la contraseña del usuario *root*, algunos datos sobre la red (si bien intenta la autoconfiguración por DHCP) y la réplica de APT de Debian que queremos utilizar para la actualización e instalación de los paquetes necesarios.

En el siguiente GIF animado podemos ver el proceso, pantalla a pantalla. 

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/nas/nas_install_gif.gif" alt="Imagen animada en la que podemos ver, pantalla a pantalla, cómo es el proceso de instalación del SO OpenMediaVault">
    </div>


Dominio para el NAS
====================

La IP asignada a la máquina virtual es la 192.168.56.111. Vamos a añadir un registro tipo A en nas.corp.carpet4you.site con la IP como contenido. 

Vamos a comprobar el registro con el comando *dig*:

.. code-block:: console
    user@server-carpet:~$ dig nas.corp.carpet4you.site.
    ; <<>> DiG 9.11.5-P4-5.1+deb10u5-Debian <<>> nas.corp.carpet4you.site.
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 3770
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;nas.corp.carpet4you.site.      IN      A

    ;; ANSWER SECTION:
    nas.corp.carpet4you.site. 3600  IN      A       192.168.56.111

    ;; Query time: 17 msec
    ;; SERVER: 169.254.169.254#53(169.254.169.254)
    ;; WHEN: Mon Oct 25 21:48:32 UTC 2021
    ;; MSG SIZE  rcvd: 69



Primer acceso al panel de gestión web
======================================

Si ahora navegamos hasta la dirección nas.corp.carpet4you.site veremos el panel de administración web de OpenMedia Vault.



.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/nas/nas22.png" alt="Imagen animada en la que podemos ver, pantalla a pantalla, cómo es el proceso de instalación del SO OpenMediaVault">
    </div>


El usuario por defecto es ``admin`` y la contraseña ``openmediavault``

Cambiar contraseña de panel web
--------------------------------

Una de las acciones que debemos realizar antes de configurar OpenMediaVault es cambiar la contraseña, que como hemos visto es muy básica. 

Para cambiarlo:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/nas/nas23.png" alt="">
    </div>


Generar certificado SSL/TLS y utilizar HTTPS
---------------------------------------------

Para generar el certificado SSL y utilizarlo en la web debemos seguir los pasos descritos en el `siguiente vídeo <https://www.loom.com/embed/2ca8a17c02a64444b19793560afb7d63>`_:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <div style="position: relative; padding-bottom: 61.1328125%; height: 0;"><iframe src="https://www.loom.com/embed/2ca8a17c02a64444b19793560afb7d63" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    </div>


Si ahora accedemos a la web podremos ver nuestro certificado:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/nas/nas24.png" alt="">
    </div>
