###################################
Conseguir certificado Let's Encrypt
###################################

En `esta página <https://letsencrypt.org/es/how-it-works/>`_ podremos ver información sobre cómo funciona el servicio ofrecido por Let's Encrypt. Sin duda, es una gran evolución en la seguridad de Internet. 

Seleccionar dominios
====================

Lo primero que debemos hacer es seleccionar para qué dominios vamos a generar el/los certificados. Debemos tener en cuenta que Let's Encrypt solo ofrece certificados *DV*, *Domain Validated*, en inglés.

En nuestro caso serán dos los dominios para los que solicitaremos el certificado: ``nas.corp.carpet4you.site``, ``cloud.carpet4you.site``, ``ftp.corp.carpet4you.site`` y ``www.carpet4you.site``. 

Instalar utilidad
==================

Comprobaremos que el gestor snap está instalado y en la última versión disponible. También eliminaremos, si lo tuviéramos instalado con otro gestor de paquetes, la utilidad certbot 

.. code-block:: console

    user@server-carpet:~$ sudo snap install core; sudo snap refresh core
    user@server-carpet:~$ sudo apt-get remove certbot


Una vez hemos comprobado que podemos instalar *snaps*, instalamos el *snap* que nos permitirá generar el certificado. También generaremos un enlace para asegurarnos de que encontrará el binario a la hora de ejecutar el comando.


.. code-block:: console

    user@server-carpet:~$ sudo snap install --classic certbot
    user@server-carpet:~$ sudo ln -s /snap/bin/certbot /usr/bin/certbot



Solicitar *challenge*
======================

El método de comprobación que tiene Let's Encrypt consiste en generar *challenges*, retos, para que los usuarios los completen y una vez confirmado, otorgar el certificado. 

Esto es importante, pues de no ser así, cualquier persona podría generar certificados para cualquier dominio (con el consiguiente problema que esto supondría).

.. code-block:: console

    user@server-carpet:~$ sudo certbot certonly --manual \
                            --preferred-challenges dns



Al ejecutar el comando comienza el proceso. Al inicio, nos solicita los dominios para los que queremos generar el certificado:

.. code-block:: console

    Saving debug log to /var/log/letsencrypt/letsencrypt.log
    Plugins selected: Authenticator manual, Installer None
    Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
    to cancel): www.carpet4you.site,nas.corp.carpet4you.site,ftp.corp.carpet4you.site,cloud.carpet4you.site


Después de introducir los nombres de dominio nos aparecerá el siguiente mensaje:

.. code-block:: console

    Obtaining a new certificate
    Performing the following challenges:
    dns-01 challenge for cloud.carpet4you.site
    dns-01 challenge for ftp.corp.carpet4you.site
    dns-01 challenge for nas.corp.carpet4you.site
    dns-01 challenge for www.carpet4you.site

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    NOTE: The IP of this machine will be publicly logged as having requested this
    certificate. If you're running certbot in manual mode on a machine that is not
    your server, please ensure you're okay with that.

    Are you OK with your IP being logged?
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    (Y)es/(N)o: y


Nos proporcionará el *challenge*. Debemos añadir el registro tipo TXT para superar el reto.

.. code-block:: console

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Please deploy a DNS TXT record under the name
    _acme-challenge.cloud.carpet4you.site with the following value:

    WTQAiXp_8WWagHsgWr0zbtUfM8JLzGU3YTyppeRe4ss

    Before continuing, verify the record is deployed.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue


Pulsamos Enter y se nos mostrarán los siguientes retos, para los siguientes dominios:

.. code-block:: console

    Please deploy a DNS TXT record under the name
    _acme-challenge.ftp.corp.carpet4you.site with the following value:

    KZCH_bizmFToeL80CO9ZB8xNQrnkVKi124L8eVKS82I

    Before continuing, verify the record is deployed.
    (This must be set up in addition to the previous challenges; do not remove,
    replace, or undo the previous challenge tasks yet. Note that you might be
    asked to create multiple distinct TXT records with the same name. This is
    permitted by DNS standards.)

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue

    Please deploy a DNS TXT record under the name
    _acme-challenge.nas.corp.carpet4you.site with the following value:

    moHQsqoKoCtJWuRdlsE4ZVf27M_5sC8PGXjT3g6FYxI

    Before continuing, verify the record is deployed.
    (This must be set up in addition to the previous challenges; do not remove,
    replace, or undo the previous challenge tasks yet. Note that you might be
    asked to create multiple distinct TXT records with the same name. This is
    permitted by DNS standards.)

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue
    
    Please deploy a DNS TXT record under the name
    _acme-challenge.www.carpet4you.site with the following value:

    JKLQaxpDRPVFB_oIMQgU5Thir78RJ49w2_BHmu7KUr8

    Before continuing, verify the record is deployed.
    (This must be set up in addition to the previous challenges; do not remove,
    replace, or undo the previous challenge tasks yet. Note that you might be
    asked to create multiple distinct TXT records with the same name. This is
    permitted by DNS standards.)

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue


Pasados unos segundos, el sistema comprueba si los registros han sido añadidos:

.. code-block:: console

    Press Enter to Continue
    Waiting for verification...
    Cleaning up challenges

    IMPORTANT NOTES:
    - Congratulations! Your certificate and chain have been saved at:
    /etc/letsencrypt/live/www.carpet4you.site/fullchain.pem
    Your key file has been saved at:
    /etc/letsencrypt/live/www.carpet4you.site/privkey.pem
    Your cert will expire on 2022-01-25. To obtain a new or tweaked
    version of this certificate in the future, simply run certbot
    again. To non-interactively renew *all* of your certificates, run
    "certbot renew"
    - If you like Certbot, please consider supporting our work by:

    Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
    Donating to EFF:                    https://eff.org/donate-le


En la carpeta ``/etc/letsencrypt/live/www.carpet4you.site/`` tendremos los certificados y demás:

.. code-block:: console
    
    root@lets-encrypt-1:/etc/letsencrypt/live/www.carpet4you.site# ll
    total 12
    drwxr-xr-x 2 root root 4096 Oct 27 07:14 ./
    drwx------ 5 root root 4096 Oct 27 07:14 ../
    -rw-r--r-- 1 root root  692 Oct 27 07:14 README
    lrwxrwxrwx 1 root root   43 Oct 27 07:14 cert.pem -> ../../archive/www.carpet4you.site/cert1.pem
    lrwxrwxrwx 1 root root   44 Oct 27 07:14 chain.pem -> ../../archive/www.carpet4you.site/chain1.pem
    lrwxrwxrwx 1 root root   48 Oct 27 07:14 fullchain.pem -> ../../archive/www.carpet4you.site/fullchain1.pem
    lrwxrwxrwx 1 root root   46 Oct 27 07:14 privkey.pem -> ../../archive/www.carpet4you.site/privkey1.pem


¡Estos son los certificados!