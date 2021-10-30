############################
Servicio Rsync automatizado 
############################

En el enunciado del ejercicio se nos solicita que la tarea de sincronización Rsync se ejecute de forma automática cada 15 minutos. 

Para hacerlo programaremos una tarea cron. 

| Si tuviéramos instalado Rsync en una máquina "limpia", sin OpenMediaVault por encima, deberíamos:
|   1) Utilizar una clave SSH para autenticarnos contra Rsync.
|   2) Programar una tarea *cron* para la ejecución de la sincronización de forma automatizada. 

Lamentablemente, después de intentarlo, no funcionaba nada, por lo que se decide:

| Crear una carpeta compartida:
|   - A la que solo se pueda acceder desde el equipo concreto.
|   - A la que solo pueda acceder un usuario determinado.
|   - Para la que no se necesite una contraseña en el acceso. 
|   - Como seguridad adicional, no se podrá descargar contenido de esta carpeta; solo añadir contenido a este. 

Configuración Rsync
======================

Configuraremos la carpeta de la siguiente forma:

.. image :: ../images/nas/nas42-rsync.png
   :width: 500
   :align: center
   :alt: Añadir clave púb
|br|






.. |br| raw:: html

   <br />