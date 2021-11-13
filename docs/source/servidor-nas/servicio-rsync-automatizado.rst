############################
Servicio Rsync automatizado 
############################

En el enunciado del ejercicio se nos solicita que la tarea de sincronización Rsync se ejecute de forma automática cada 15 minutos. 


| Para hacerlo debemos: 
| 1) Utilizar una clave SSH para autenticarnos contra Rsync.
| 2) Programar una tarea *cron* para la ejecución de la sincronización de forma automatizada. 

Generar clave SSH
==================

Por motivos de seguridad **no vamos a usar la misma clave SSH**. Por motivos intrínsecos a la ejecución del comando (debe ejecutarse de forma automática, sin interacción del usuario) la clave no debe tener contraseña simétrica. 

**Desde el cliente**, vamos a generarla. uando nos pida introducir contraseña, haremos clic en Intro para no fijar ninguna:

.. code-block:: console
    
    pablo@cliente:~$ ssh-keygen -t rsa

La guardaremos en ~/.ssh/backup

Copiar clave pública a servidor
================================

Como ya hemos visto en el apartado de *Servicio SSH autenticado con clave pública-privada*, ocurren cosas raras al intentar añadir las claves de un usuario desde la GUI web. 

Iniciando en el propio servidor (mediante SSH, por ejemplo), añadimos la clave publica al archivo ``/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/.ssh/authorized_keys``. Después de copiarla tendremos, al menos, dos clave:

* La clave pública para el inicio SSH "típico". 
* La clave pública que utilizaremos para la autenticación contra Rsync. 

Veamos un ejemplo:

.. code-block:: console

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+cdESzhtIoTq0xWrUeQNYg6VkMOg1cNj7TDC+fXXIPdj10TFmitQ7if5PgcyOVPccEJ9TF2+lCcAbgPSNxUjptY+IjV39exucVUN1hdRRxxBQOl6YDiG4CND5oMUqyHFzYR7Oornh+hkaw89MOzRU/K9xRsYoRmrK8BeYE4gxsyeCA5vNf8Z2imukgOF3u7/zvQF3Z4oZYkGG2X8qFlgS1bfmwZ7kjT0JFjtEd6+gIUUuZpI0s3SOpX815doJQS0gSHFJj4Qo9MhjvnIVVd1Og0arZsKXysCZnEKQuFYEVWmH7dcWgIDH2aHeZ9LtEO7JcBu1DblYwgcFqiF8T0mP 

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDayMy/MPci3iiY+bVSuB7/AnkdmxcijnefOAY1hfdOmI5xz7f/I6DJ/xdkskqhXOl0OgB2kyOnaIys6drCC1+rNyOTuWemg/Hn8XRgcudGWmyMQ8XYUwrWyitGHa2LTdHAiLM0i1LX67svACVWInAS7MPCn02uIfr5eBzH3moQoTjsVlvcLj4pnUAVQPgDqqI1nf6huKmzJprwQkmaoozJ93/YF7+hJ6eakeFOSrD/ZvaWb+zDdC+RdM3qwOe669iIhiK7O9lwLf7NCuhvXo1eqkMGj+Ocf9OnyNWUKzdqdEqAELV7mioU2qgE8vq+WtYb/eODTgGzys/TfXCn7m+B user@server-carpet



Probar conexión a carpeta
===========================

Para comprobar si funciona Rsync debemos generar algunos archivos y después comprobar si se copian.

.. code-block:: console

    user@cliente:~$ sudo rsync -avRh -e "ssh -i /home/user/.ssh/backup"  prueba/ user@nas.corp.carpet4you.site:/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/

Este es el resultado:

.. image :: ../images/nas/nas44-rsync.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|


Tarea cron
===========

Añadiremos la tarea crontab con el siguiente comando:

.. code-block:: console

    user@cliente:~$ sudo su #Necesitamos que la tarea la ejecute root
    user@cliente:~$ crontab -e

    # En el archivo que se nos abre añadimos el siguiente comando:
        */15 * * * * sudo rsync -aRh -e "ssh -i /home/user/.ssh/backup"  /home/user/prueba user@nas.corp.carpet4you.site:/srv/dev-disk-by-id-md-name-nas-RAID5Carpet4You/home/user/

Comprobación cron
==================

Crearemos algún archivo en la carpeta prueba y veremos si se copia en el servidor.

.. tip::

    | Puede ser útil cambiar el cron para que se ejecute cada minuto durante las pruebas.
    | Para configurar la programación de cron, `esta página <https://crontab.guru/every-15-minutes>`_ es muy útil.

**¡Funciona!**

.. image :: ../images/nas/nas45-rsync.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|

Limitar acceso desde IP cliente
=================================

Como medida de seguridad adicional, limitaremos el uso de la clave pública. Indicaremos que únicamente se pueda utilizar desde el equipo cliente. Para identificar al equipo usaremos su clave pública. 

.. code-block:: console

    from="192.168.56.109" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDayMy/MPci3iiY+bVSuB7/AnkdmxcijnefOAY1hfdOmI5xz7f/I6DJ/xdkskqhXOl0OgB2kyOnaIys6drCC1+rNyOTuWemg/Hn8XRgcudGWmyMQ8XYUwrWyitGHa2LTdHAiLM0i1LX67svACVWInAS7MPCn02uIfr5eBzH3moQoTjsVlvcLj4pnUAVQPgDqqI1nf6huKmzJprwQkmaoozJ93/YF7+hJ6eakeFOSrD/ZvaWb+zDdC+RdM3qwOe669iIhiK7O9lwLf7NCuhvXo1eqkMGj+Ocf9OnyNWUKzdqdEqAELV7mioU2qgE8vq+WtYb/eODTgGzys/TfXCn7m+B user@server-carpet

.. admonition:: Solo para valientes

    Cabe la posibilidad de restringir, mediante otra anotación en el archivo ``authorized_keys``, qué comandos puede ejecutar el usuario. 

.. |br| raw:: html

   <br />
