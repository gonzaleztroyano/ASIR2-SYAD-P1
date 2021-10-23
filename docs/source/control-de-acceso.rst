************************
Control de Acceso físico
************************

Sistema de grabación
====================
Para el sistema de grabación de las oficinas se utilizará el sistema de **Unifi Protect Cameras** . Se puede obtener más información sobre este sistema en `esta página <https://ui.com/camera-security>`__.
Una de las características más importantes de este sistema radica en la funcionalidad de autoalojar el controlador y las grabaciones. Esto permite tener control total sobre la infraestructura. Además, de esta forma no tenemos tráfico externo en este sentido. 
El departamento legal, por la alta inversión que realiza el departamento de I+D+i de la empresa nos aconsejó que las imágenes de los laboratorios de alfombras no salieran al exterior. 

Cámaras de vídeo
-----------------
Para la oficina de Bélgica se instalarán 40 cámaras de vídeo.
Se utilizarán diferentes modelos:

* 15 Cámaras del modelo *AI 360*. La información se encuentra disponible en `este enlace <https://eu.store.ui.com/collections/unifi-protect/products/unifi-protect-ai-360-beta>`__ y el dataset `aquí <https://dl.ubnt.com/ds/uvc-ai-360_ds>`__. Este modelo será utilizando para la grabación de vestíbulos y zonas de paso, gracias a su vista panorámica. También se instalarán en las salas de proceso de datos, 2 por sala. 
* 2 Cámaras del modelo *G4 Pro*, para la grabación de pasillos entre las salas de proceso de datos. La información se encuentra disponible en `este enlace <https://eu.store.ui.com/collections/unifi-protect-cameras/products/unifi-protect-g4-pro-camera>`__ y el dataset `aquí <https://www.ui.com/downloads/datasheets/unifi/UVC-G4-PRO_DS.pdf>`__.
* 5 Cámaras del modelo *G4 PTZ*. La información se encuentra disponible en `este enlace <https://eu.store.ui.com/collections/unifi-protect/products/unifi-protect-g4-ptz>`__ y el dataset `aquí <https://dl.ubnt.com/ds/uvc-g4-ptz-ds.pdf>`__. Se eligen estas cámaras para la grabación exterior gracias a su capacidad de zoom x22, movimiento de lente, etc. Se situará una cámara en cada esquina del edificio, así como una adicional en el control de acceso 1.  

Gestión de grabaciones
-----------------------
La gestión de grabaciones se guardará en dos ubicaciones distintas como provisión de redunancia. Las grabacones serán guardadas durante 30 días en el centro y las grabaciones de los últimos 14 serán enviadas a través de conexión privada que la compañía tiene contratada (al menos) a otra sede de la empresa. 

En todas las oficinas se dispone de un armario especial, marca *Rittal*, modelo *Micro Data Center Level E*. Más información en `este enlace <https://www.rittal.com/es-es/product/list/variations.action?categoryPath=/PG0001/PG0800ITINFRA1/PGRP5189ITINFRA1/PG1635ITINFRA1/PG1640ITINFRA1/PRO16554ITINFRA&productID=PRO16554>_`. En este se guardarán los equipos más importantes de la red. Por un lado, el sistema de gestión de grabaciones. Y los border routers que conectan los diferentes switches primarios de las salas. Estos border routers estarán conectados con dos 2 ISPs Tier 1, al menos. Y si la construcción lo permite, mediante canales exteriores distintos. 

El hardware que alojará las grabaciones de las cámaras es el propio de la marca *Unifi*, el nombre del producto es *Unifi Protect Network Video Recorder Pro*. Hay disponible más información sobre dicho artículo en `este enlace <https://store.ui.com/collections/surveillance/products/unifi-protect-network-video-recorder-pro>`_. 

Con los discos de 8TB ya tenidos en cuenta el sistema de gestión y alojamiento de grabaciones tiene un coste aproximado de 1.500€. 

Coste del sistema de grabaciones
--------------------------------
+----------------+----------+---------------+--------------+
|    Producto    | Cantidad | Precio/Unidad | Precio total |
+================+==========+===============+==============+
| Cámaras AI 360 |    15    |      249,00 € |   3 735,00 € |
+----------------+----------+---------------+--------------+
|     G4 Pro     |     2    |      379,00 € |     758,00 € |
+----------------+----------+---------------+--------------+
|     G4 PTZ     |     5    |    1 509,00 € |   7 545,00 € |
+----------------+----------+---------------+--------------+
|     NVR Pro    |     1    |    1 500,00 € |   1 500,00 € |
|      + HDD     |          |               |              |
+----------------+----------+---------------+--------------+

Sistema de control de personas interior
======================================
El sistema de control de acceso es producido por la misma empresa que las cámaras. El nombre comercial es *Unifi Access*. 

Debemos distinguir los siguientes dispositivos/partes de control:
 * Las tarjetas inteligentes. De estas dispondrán los empleados y las usarán para moverse por el centro.
 * Los lectores de tarjetas. Distinguimos dos modelos distintos:

    * El `AC Reader Pro <https://eu.store.ui.com/collections/unifi-door-access/products/unifi-access-reader-pro>`_, con pantalla y cámara integrada. Se instalará en las puertas de entrada a la sala de Control, así como en la de acceso al distribuidor de salas de proceso. Dispone de lector de tarjetas, Bluetooth para integración con la aplicación móvil de acceso, posibilidad de introducir PIN de acceso, y cámara para actuar de timbre y ser permitida la entrada por otra persona. 
    * El `AC Reader Lite <https://eu.store.ui.com/collections/unifi-door-access/products/unifi-access-reader-lite>`_, que se instalará en las puertas de entrada a las salas de proceso de datos. Uno en cada lado de la puerta de paso. Así, como en el sentido de vuelta de las salas de proceso de datos. Permite la identificación con tarjeta inteligente, así como con la aplicación móvil. 
* El `Access Hub <https://dl.ui.com/ds/ua-ds.pdf>`_, que actúa de interfaz entre el controlador de los equipos, las cerraduras y los lectores. Se conecta mediante PoE al cotrolador y el resto de equipos de una pueta a este. Desde el Access Hub son alimentados mediante PoE los lectores. 
* Todo el sistema es coordinado por el equipo *Dream Machine Pro*, que dispone de una interfaz web para la gestión y mantenimiento. En este equipo también se instalará el controlador para el sistema Wi-Fi. Tiene un coste aproximado de 500€

En el `siguiente vídeo <https://www.youtube.com/embed/wh_nPEOtLzc>`_ podemos ver cómo funciona el sistema:

.. raw:: html

    <div style="position: relative; margin: 2em; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/wh_nPEOtLzc" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

Coste del sistema de control de paso
---------------------------------------

+---------------------+----------+---------------+--------------+
|       Producto      | Cantidad | Precio/Unidad | Precio total |
+=====================+==========+===============+==============+
| Tarjetas de control |    200   |        3,00 $ |     600,00 $ |
|      de acceso      |          |               |              |
+---------------------+----------+---------------+--------------+
|      Access Hub     |     7    |      199,00 $ |   1 393,00 $ |
+---------------------+----------+---------------+--------------+
|  Access Reader Pro  |     2    |      299,00 $ |     598,00 $ |
+---------------------+----------+---------------+--------------+
|  Access Reader Lite |     7    |       99,00 $ |     693,00 $ |
+---------------------+----------+---------------+--------------+
| Unifi Dream Machine |     1    |      500,00 $ |     500,00 $ |
+---------------------+----------+---------------+--------------+


Sistema de arcos de seguridad y detectores de metales
=====================================================
La instalación y el mantenimiento de estas soluciones correrá a cargo de la empresa barcelonesa "OrcromSeguridad". Se instalará en el control de acceso 2 un conjunto de control del fabricante *Garret Metal Detectors*. En `este enlace <https://www.orcromseguridad.com/wp-content/uploads/2018/10/Integracion-Garrett-VMI.pdf>`_ se encuentra disponible un folleto publicitario con los productos que incluye el conjunto. Son los siguientes:
 * *Spectrum 6040*, que permite la inspección de mochilas y bolsos de empleados y visitantes. Se instará a los empleados a no pasar al interior con mochilas y bolsos, permitiéndolo dejar en taquillas vigiladas en el control. De esta manera se evita la sobre exposición de la empleada/o del Control, trabajadoras, trabajadores y visitantes a los rayos X, así como de sus pertenencias. En `este enlace <https://www.orcromseguridad.com/nuestros-productos/equipo-rayos-x-spectrum-6040/>`_ se puede obtener más información sobre este producto. 
 * *Garrett PD 6500i*, este arco de seguridad permite evitar el paso con objetos metálicos al interior del recinto. Desde `este enlace <https://orcromseguridad.com/wp-content/uploads/2018/08/arco-detector-Garrett-PD6500i.pdf>`_ se puede obtener más información sobre dicho producto. 

El equipo será operado por un vigilante de seguridad propio (en Carpet4You no subcontratamos/externalizamos, pues creemos en el empleo de calidad y la confianza). 

Se desconoce el precio de dicho sistema, al no ser público. 

Sistema de prevención de intrusión exterior
============================================
Para prevenir el acceso desde el exterior se combinan diferentes medidas de seguridad. 
 * Por un lado, 

Vigilancia perimetral y control interior
=========================================

