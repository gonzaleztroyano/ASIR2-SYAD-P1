*******************************************
Direccionamiento IP de la empresa (general)
********************************************

Rangos de IP asignados
=======================
Rangos públicos
---------------
La empresa dispone de una serie de rangos IP asignados por el RIR RIPE. Esto permite la conectividad indenpendiente y segura. La gestión propia asegura la optimización máxima de las rutas. 
Carpet4You dispone del AS número 88757. Este *Autonomous Number* tiene una serie de rangos IP asignados:

* Rangos IPv6:
    
    * Rango /48 1 --> 2001:db8:3c4d::/48 usado para el CPD de Bilbao 
    * Rango /48 2 --> 2001:db8:3c4e::/48 usado para el CPD de Bélgica
    * Rango /48 3 --> 2001:db8:3c4f::/48 en reserva, se planea utilizar subsegmentos para la conectividad hacia Internet de las sedes y experimentación del equipo de I+D+i


.. Attention::
     Nótese que los rangos IPv6 no son enrutables en Internet y corresponde y son subrangos del rango dedicado por IANA para la confección de documentación.

* Rango en IPv4: 100.65.65.0. Subdividido
+------------------+---------------------+-------------------------------+-----------------+
| Dirección de red | Usado en            | Rango de IPs utilizable       | IP de Broadcast |
+==================+=====================+===============================+=================+
| 100.65.65.0      | CPD Bilbao          |100.65.65.1 - 100.65.65.62     | 100.65.65.63    |
+------------------+---------------------+-------------------------------+-----------------+
| 100.65.65.64     | CPD Bélgica         |100.65.65.65 - 100.65.65.126   | 100.65.65.127   |
+------------------+---------------------+-------------------------------+-----------------+
| 100.65.65.128    | Reserva             |100.65.65.129 - 100.65.65.190  | 100.65.65.191   |
+------------------+---------------------+-------------------------------+-----------------+
| 100.65.65.192    | Reserva             | 100.65.65.193 - 100.65.65.254 | 100.65.65.255   |
+------------------+---------------------+-------------------------------+-----------------+


.. Attention::
     Nótese que el rango de IPv4 no es enrutable en Internet y corresponde al rango de las IPs asigadas a los Internet Service Providers (IPS) para el uso de CG-NAT.


Rangos privados
---------------

Los rangos privados están recogidos en el `RFC1918 <https://datatracker.ietf.org/doc/html/rfc1918>`_ de la Internet Engineering Task Force. 

En el caso de Carpet4You, se ha decicido utilizar el rango privado 10.0.0.0/8 para direccionamiento IP interno. La amplitud de este rango permite a la empresa crecer, mantener subredes dedicadas por sede y no tener problemas a futuro. 

+--------------------------+-------------------------------------------------+
| Dirección de red y VLANs |                     Usado en                    |
+==========================+=================================================+
| **10.201.0.0/16**        | **Sede Badajoz (B1)**                           |
|  * 10.201.0XX.0/24       |  * Rangos utilizados para Management            |
|  * 10.201.1XX.0/24       |  * Rangos utilizados para los diferentes dptos. |
|  * 10.201.2XX.0/24       |  * Direcciones internas para servidores         |
+--------------------------+-------------------------------------------------+
| **10.202.0.0/16**        | **Sede Bilbao (B2)**                            |
|  * 10.202.0XX.0/24       |  * Rangos utilizados para Management            |
|  * 10.202.1XX.0/24       |  * Rangos utilizados para los diferentes dptos. |
|  * 10.202.2XX.0/24       |  * Direcciones internas para servidores         |
+--------------------------+-------------------------------------------------+
| **10.203.0.0/16**        | **Sede Bruselas (B3)**                          |
|  * 10.203.0XX.0/24       |  * Rangos utilizados para Management            |
|  * 10.203.1XX.0/24       |  * Rangos utilizados para los diferentes dptos. |
|  * 10.203.2XX.0/24       |  * Direcciones internas para servidores         |
+--------------------------+-------------------------------------------------+
| **10.204.0.0/16**        | **Sede Bergen (B4)**                            |
|  * 10.204.0XX.0/24       |  * Rangos utilizados para Management            |
|  * 10.204.1XX.0/24       |  * Rangos utilizados para los diferentes dptos. |
|  * 10.204.2XX.0/24       |  * Direcciones internas para servidores         |
+--------------------------+-------------------------------------------------+
| **10.205.0.0/16**        | **Trabajadores Remotos**                        |
|  * 10.205.1.0/24         |  * Trabajadores Remotos en Rusia                |
|  * 10.205.2.0/24         |  * Trabajadores Remotos en Minsk                |
|  * 10.205.4.0/24         |  * Trabajadores Remotos en Reino Unido          |
|  * 10.205.201.0/24       |  * Trabajadores Remotos asignados a sede B1     |
|  * 10.205.202.0/24       |  * Trabajadores Remotos asignados a sede B2     |
|  * 10.205.203.0/24       |  * Trabajadores Remotos asignados a sede B3     |
|  * 10.205.204.0/24       |  * Trabajadores Remotos asignados a sede B4     |
+--------------------------+-------------------------------------------------+


Conectividad física para las sedes
===================================

Conexión entre sedes
--------------------


.. image :: images/ASIR2.SYAD.P1.3.Mapa.svg
   :width: 500
   :align: center
   :alt: Mapa de Europa con las sedes y conexiones
|br|

.. note::

    Si accedes a esta documentación desde la versión PDF, el GIF es accesible desde `este enlace <https://github.com/gonzaleztroyano/ASIR2-SYAD-P1/blob/main/docs/source/images/ASIR2.SYAD.P1.3.Mapa.svg>`_

|br|
    
.. note::
    El color rojo simboliza trabajadoras y trabajadores remotos. 
    Las líneas discontínuas simbolizan conexiones utilizando infraestructura de Internet pública. 
    Las líneas contínuas son líneas dedicadas.

Para las conexiones entre sedes se contratan fibras oscuras con diferentes proveedores:
 * Para la conexión entre Bajadoz (BJZ) y Bilbao (BIO) el proveedor es `Correos Telecom <https://www.correostelecom.com/servicios>`_.
 * Para la conexión entre Bilbao (BIO) y Bruselas (BRU); así como entre Bruselas (BRU) y Bergen (BGO) está contratada con el proveedor `Colt <https://www.colt.net/es/product/dark-fibre/>`_.


.. |br| raw:: html

   <br />
