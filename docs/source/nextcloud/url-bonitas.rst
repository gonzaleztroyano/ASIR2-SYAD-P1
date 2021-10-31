################################
Eliminar *index.php* de las URL
################################

Activamos dos módulos de Apache:

.. code-block:: console

    sudo a2enmod rewrite
    sudo a2enmod env

En el archivo ``/var/www/nextcloud/config/config.php``

.. code-block::

    'overwrite.cli.url' => 'https://cloud.carpet4you.site/',
    'htaccess.RewriteBase' => '/',

Ejecutamos:

.. code-block:: console

    sudo -u www-data php /var/www/nextcloud/occ maintenance:update:htaccess


Ahora ya podemos ver la URL sin "index.php" en la misma:

.. image :: ../images/nextcloud/nc-12.png
   :width: 500
   :align: center
|br|

.. |br| raw:: html

   <br />