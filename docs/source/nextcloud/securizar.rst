################################
Securizar Nextcloud con SSL/TLS
################################

Descargamos los certificados:

.. code-block:: console

    sudo mkdir /etc/certificados
    cd /etc/certificados
    wget https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/public/cert-letsencrypt/fullchain1.pem
    wget https://raw.githubusercontent.com/gonzaleztroyano/ASIR2-SYAD-P1/main/public/cert-letsencrypt/privkey1.pem

Modificaremos el archivo

Modificamos el archivo ``/etc/apache2/sites-available/nextcloud.conf`` para que tenga el siguiente contenido:

.. code-block:: 

    <IfModule mod_ssl.c>
    <VirtualHost *:80>
    DocumentRoot /var/www/nextcloud/
    ServerName  cloud.carpet4you.site

    <Directory /var/www/nextcloud/>
        Require all granted
        AllowOverride All
        Options FollowSymLinks MultiViews

        <IfModule mod_dav.c>
        Dav off
        </IfModule>
    </Directory>
    RewriteEngine on
RewriteCond %{SERVER_NAME} =cloud.carpet4you.site
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>



En el archivo ``/etc/apache2/sites-available/nextcloud-le-ssl.conf`` añadimos:

.. code-block:: 
                                               
    <IfModule mod_ssl.c>
        <VirtualHost *:443>
        DocumentRoot /var/www/nextcloud/
        ServerName  cloud.carpet4you.site

        <Directory /var/www/nextcloud/>
            Require all granted
            AllowOverride All
            Options FollowSymLinks MultiViews

            <IfModule mod_dav.c>
            Dav off
            </IfModule>
        </Directory>

    SSLCertificateFile /etc/letsencrypt/live/cloud.carpet4you.site/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/cloud.carpet4you.site/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf
    </VirtualHost>
    </IfModule>


.. note::

    Se ha utilizado certbot para la obtención del certificado Let's Encrypt y para la configuración de Apache. 


Ya podemos acceder a la paǵina mediante SSL:

.. image :: ../images/nextcloud/nc-11.png
   :width: 500
   :align: center
|br|

.. |br| raw:: html

   <br />