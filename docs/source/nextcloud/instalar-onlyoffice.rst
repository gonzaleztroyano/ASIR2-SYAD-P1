#################################
Instalar OnlyOffice en NextCloud
#################################

Instalación de servidor OnlyOffice
===================================

.. note::
    
    Vamos a instalar el servidor de OnlyOffice en Docker para la práctica nos es suficiente. No estamos en un entorno de producción. 

Instalamos docker:

.. code-block:: console

    # Desinstalar versiones antiguas, si las hubiera
    sudo apt remove docker docker-engine docker.io containerd runc

    # Actualizar paquetes en los repos
    sudo apt update

    # Instalar dependencias
    sudo apt install ca-certificates curl gnupg lsb-release

    # Descargar clave GPG de Docker
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    # Añadir el repositorio de docker
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # Instalar el motor Docker
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io

Iniciar el contenedor docker:

.. code-block:: console

    sudo docker run -i -t -d -p 8443:443 \
        -v /app/onlyoffice/DocumentServer/logs:/var/log/onlyoffice  \
        -v /app/onlyoffice/DocumentServer/data:/var/www/onlyoffice/Data  \
        -v /app/onlyoffice/DocumentServer/lib:/var/lib/onlyoffice \
        -v /app/onlyoffice/DocumentServer/rabbitmq:/var/lib/rabbitmq \
        -v /app/onlyoffice/DocumentServer/redis:/var/lib/redis \
        -v /app/onlyoffice/DocumentServer/db:/var/lib/postgresql  onlyoffice/documentserver


Deberán descargarse y descomprimirse varios archivos, que juntos formarán la imagen del contenedor. Para ver si está funcionando usamos el comando:

.. code-block:: console

    sudo docker container list

.. important::

    Debemos utilizar como puerto externo (el primero de la combinación docker, 8443) del contenedor uno que no esté en uso por ningún otro proceso. 

    Alojar las rutas indicadas en nuestro propio sistema de archivos nos ayudará a "debuguear" problemas. 

    Más información sobre la imagen docker de Onlyoffice en `este enlace <https://github.com/ONLYOFFICE/Docker-DocumentServer>`_


Generar certificados para el servidor
=======================================

.. code-block:: console

    openssl genrsa -out tls.key 2048
    openssl req -new -key tls.key -out tls.csr
    openssl x509 -req -days 90 -in tls.csr -signkey tls.key -out tls.crt
    openssl dhparam -out dhparam.pem 2048
    mkdir -p /app/onlyoffice/DocumentServer/data/certs
    cp tls.key /app/onlyoffice/DocumentServer/data/certs/
    cp tls.crt /app/onlyoffice/DocumentServer/data/certs/
    cp dhparam.pem /app/onlyoffice/DocumentServer/data/certs/
    chmod 400 /app/onlyoffice/DocumentServer/data/certs/tls.key



Aplicación en NextCloud
========================

Instalaremos la aplicación desde el *Marketplace* de Nextcloud

https://cloud.carpet4you.site/settings/apps/office/onlyoffice

Hacemos clic en *Descargar e Instalar*.

.. image :: ../images/nextcloud/nc-26.png
   :width: 500
   :align: center
|br|


Conectar NextCloud con OnlyOffice
====================================

Navegamos hasta los ajustes (<URL_de_nuestro_nextcloud>/settings/admin/onlyoffice) y aquí introducimos la dirección de conexión de nuestro servidor Onlyoffice:::

    https://onlyoffice.int.carpet4you.site:8443/

Veremos un mensaje de confirmación, si todo ha ido bien:

.. image :: ../images/nextcloud/nc-27.png
   :width: 500
   :align: center
|br|


En la parte inferior podemos ver los ajustes de la aplicación:

.. image :: ../images/nextcloud/nc-28.png
   :width: 500
   :align: center
|br|

.. |br| raw:: html

   <br />