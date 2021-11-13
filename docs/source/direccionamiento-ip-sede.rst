******************************
Direccionamiento IP de la sede
******************************

Tal y como podemos ver en `el cuadro de IPs <https://syad.gonzaleztroyano.es/direccionamiento-ip-empresa.html#rangos-privados>`_ de la página de direccionamiento IP de toda la empresa, a la sede de bruselas le corresponde el siguiente rango:

+--------------------------+-------------------------------------------------+
| Dirección de red y VLANs |                     Usado en                    |
+==========================+=================================================+
| **10.203.0.0/16**        | **Sede Bruselas (B3)**                          |
|  * 10.203.0XX.0/24       |  * Rangos utilizados para Management            |
|  * 10.203.1XX.0/24       |  * Rangos utilizados para los diferentes dptos. |
|  * 10.203.2YY.XXX/32     |  * Direcciones internas para servidores         |
+--------------------------+-------------------------------------------------+


En tanto a los requisitos mínimos, tenemos el siguiente mapa de red proporcionado en las instrucciones de la práctica:

.. image :: images/ip1.png
    :align: center
    :width: 400
    :alt: Mapa de red proporcionado.


Hardware de red
===============

Toda la infraestructura de la red de la sede estará compuesta por equipos de la gama *Unifi*, del fabricante Ubiquiti Networks. 

Al igual que las cámaras y el control de acceso, toda la infraestructura es gestionable desde un único panel web. 

Las funcionalidades de los equipos Unifi son equiparables a los archiconocidos *Cisco*. Una de las mayores diferencias radica en el menor precio de adquisción y mayor facilidad de mantenimiento. Los switches de Unifi trabajan a nivel 3, por lo que pueden enrutar tráfico de varias redes sin necesidad de switch.

Otra de las opciones a bajarar era *Sophos*, pero las licencias anuales son prohibitibas. 

.. note ::

    Es posible que Unifi no sea suficientemente potente en comparación con otras soluciones. Por ejemplo, en el análisis de tráfico encriptado. 
    
    Si la decisión final fuera mía, tuviera presupuesto y tiempo para conocer la solución me decantaría por la solución de Cisco Meraki. Combina la sencillez de Unifi con la potencia tradicional de Cisco. 


VLANs - Management
====================

Tal y como podemos ver en el cuadro anterior, tenemos disponibles IPs entre 10.203.001.0/16 hasta 10.203.099.0/16 para management. 

Por comodidad, trabajaremos con redes /24. Entendemos como *Management* las direcciones necesarias para servicios internos: el propio equipamiento de red, teléfonos VoIP, cámaras y resto de equipamiento. 

Las VLAN definidas para management son:

 * **VLAN10**, rango IP 10.203.010.0/24. En esta red se incluirán los dispositivos de red. 
 * **VLAN11-20**, rangos IP 10.203.011.0/24 - 10.203.020.0/24. Se incluirán en estos rangos los teléfonos VoIP. Se reservará un subrango para cada departamento. 
 * **VLAN25**, rango IP 10.203.025.0/24. Se incluirán en esta red el hardware de control de acceso. 
 * **VLAN30**, rango IP 10.203.030.0/24. Se inclurán en este rango de IP las cámaras de seguridad. 
 * **VLAN50**, rango IP 10.203.050.0/24. A este rango pertenecerán los dispositivos de casting hacia TV y proyectores con capacidad inalámbrica.
 * **VLAN99**, rango IP 203.099.0/24. Este rango estará dedicado a los invitados. 
 


VLANs - Empleadas y empleados
==============================

Tal y como podemos ver en el cuadro anterior, tenemos disponibles IPs entre 10.203.100.0/16 hasta 10.203.199.0/16 para los equipos de empleadas y empleados. 

A tener en cuenta: todos los departamentos tienen menos de 250 empleados/equipos. En caso de tener más empleados que IPs disponibles en un red tipo C, se utilizarán dos o más redes. 

Todas las empleadas y empleados tendrán a su disposición una red inalámbrica para la conxión d sus dispositivos móviles y portátiles si lo tuvieran. 


Siendo ``Y`` un número de departamento se crean las siguientes VLANs

 * **VLAN1YY**, 10.203.1YY.0/24. A estas VLANs se conectarán los equipos propiedad de la empresa. 
 * **VLAN1(YY+50)**, 10.203.1(YY+50).0/24. A estas VLANs se conectarán los equipos propiedad de la empleada o empleado (BYOD). 



VLANs - Servicios internos
==========================

Tal y como podemos ver en el cuadro anterior, tenemos disponibles IPs entre 10.203.200.0/16 hasta 10.203.250.0/16 para sericios internos. Se define 250 en tercer byte para que sea más secillo.

Se define la **VLAN222**, con rango de IP 10.203.222.0/24 para la zona DMZ. En ella se localizan el servidor MySQL, el servidor Apache, el servidor DNS, el servidor OwnCloud y los futuros servidores o equipos que cumplan la característica de estar detrás de la DMZ. 

En cualquier caso, que estén dentro de algo que llamemos *DMZ* no significa que tengan todos los pueros abiertos. De hecho, por seguridad, solo tendán abiertos los estrictamente necesarios. 

Se define la **VLAN203**, con rango de IP 10.203.203.0/24 para los equipos servidor que no estén dentro de la DMZ. Entre estos equipos figuran el servidor Windows (para AD y actualizaciones entre otros), así como el servidor Linux (APT-Cacher entre otros). También se incluye en esta VLAN el servidor NAS. 

.. note::
    Se entiende que no es necesario indicar cada IP para cada equipo de la red. 

    La puerta de enlace tendrá una IP primaria (la de *management*) dentro de la VLAN10. A su vez, tendrá la primera IP en cada VLAN. 

