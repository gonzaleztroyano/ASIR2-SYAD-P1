##############
Servidor SSH
##############

A continuación se detalla el proceso de instalación y configuración del servidor SSH para un equipo de la empresa.

Máquina Virtual de trabajo
==========================

Se utilizará una máquina virtual con Ubuntu Server 18.04 como sistema operativo. Se le asignan 4 GB de RAM y 4 vCPUs. 
En tanto a la red, se configuran 2 adaptadores virtuales:
 * Adaptador 1, configurado en modo NAT para la conexión a internet. 
 * Adaptador 2, confiugrado en modo solo-anfitrión, para la conexión SSH y a los servicios.

En tanto al usuario administrador utiliza la (poco segura) combinación user:user.

Instalación del servidor SSH
=============================

Para instalar el servidor SSH, si no estuviera instalado, debemos ejecutar el siguiente comando:

.. code-block:: console
    
    user@server-carpet:~$ apt update
    user@server-carpet:~$ apt install openssh-server

Si lo acabamos de instalar debemos iniciarlo y permitir su inicio en el arranque del equipo:

.. _referencia-reinicio-ssh:

.. code-block:: console
    
    user@server-carpet:~$ systemctl enable ssh
    user@server-carpet:~$ systemctl start ssh


Configuración personalizada
============================

Cambiar puerto de conexión
---------------------------

Para cambiar el puerto de conexión debemos editar el archivo */etc/ssh/sshd_config* para modificar la siguiente política:

.. code-block:: console

   Port 3200

Conexión mediante clave publica
--------------------------------

Primero debemos haber generado un par de claves, como es nuestro caso. La clave pública debemos copiarla al archivo *~/.ssh/authorized_keys*. En nuestro caso la hemos generado desde el equipo cliente y la hemos copiado al servidor.

.. code-block:: console

    user@server-carpet:~/.ssh$ cat authorized_keys
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMyXStDPWjrmR2WejGUFS6RN5TlWNOiXErOANYAwY2jeOA2i0EPgBNhIV+PEy+APUZzUJOEOtDy
    USfPDIT5GcgeuHSMm3WwU+ax6IeJ8lYRJuVGP9cmiJFhVYSOF1FrjuC39vLuTmSPxr4kzU/TronZmQ5jbwWuZfEtSAMEslaQST1t9HTZZWPXmyhyn
    ya1f4tAxD34vOTDZ6Cc3N+xI3NuCBFZRd1fVDsOKyot3vhwpNi0VbVYF9uMFGQdgiTPVSRgrnbxTiUtfyvz4FnyWHRZl+x+k7n11zojf8nrqsjgi3
    zPAbss7Be8hK1Tmh68J5UfOPowWNWW1dG1RakyVuLd1t/eYTn8t+w7qnMp8mkosat6LW/ARD1BupCCmPe/hTyysh5pMe66gb6R1yMBrHzokbd6EOv
    C5f2Rlc+TYETujJronVIwznAeNuJB3F8U1v4PDcGpzDTAmHcTLyi7Mp32J2qbkjQ+lNO9vnr7eE+mWV86GB5KlxR7f0VTHPbso5gYbGOTRxaK2n3h
    imV9/K6AUqCb4HNDBcYs3D19OsWQFNTKCp80CZPl5XcUXCase3qbpnoInXkSUdNCYnkGskgzVZuiJmt7uxIGLaLoXXpBczN7Bj1LbVmZ48B7CZhBA
    w7Qq13Vwepzs8nEbcvLxD3Z0vN8t+e5kSxU3McyIqTQ== user@server-carpet


Lo siguiente que debemos hacer es modifcar el archivo */etc/ssh/sshd_config* para modificar las siguientes políticas:

.. code-block:: console
    
    PasswordAuthentication no

Debemos reiniciar el servicio tal y como hemos visto en :ref:`referencia-reinicio-ssh`.

Si intentamos conectarnos ahora (con el programa Putty en Windows) recibiremos un error.


.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 5%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
       <a href="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/errorssh1.png" rel="noopener"><img src="https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/docs/source/images/errorssh1.png" alt="Error SSH"></a>
    </div>


Desconexión automática
-----------------------

Debemos modifcar el archivo */etc/ssh/sshd_config* para modificar las siguientes políticas:

.. code-block:: console
    
    ClientAliveInterval 60

Solo usuario 'administrador'
-----------------------------

Debemos modifcar el archivo */etc/ssh/sshd_config* para modificar las siguientes políticas:

.. code-block:: console
    
    AllowUsers administrador

No permitir acceso root
------------------------
Debemos modifcar el archivo */etc/ssh/sshd_config* para modificar las siguientes políticas:

.. code-block:: console
    
    PermitRootLogin no

Prohibir acceso a usuario 'invitado'
-------------------------------------
Debemos modifcar el archivo */etc/ssh/sshd_config* para modificar las siguientes políticas:

.. code-block:: console
    
    DenyUsers invitado