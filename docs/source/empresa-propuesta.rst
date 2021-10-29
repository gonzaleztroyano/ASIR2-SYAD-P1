***************************
Empresa ficticia propuesta
***************************

Para esta práctica se propone la empresa de venta y limpieza de alfombras de lujo "Carpet4You". 
Esta empresa, con sede en un pequeño pueblo de Badajoz, empezó su actividad a mediados de los años 80 y ha ido ampliando su mercado nacional e internacional, llegando a vender las alfombras del Burj Khalifa, embajadas rusas de todo el mundo. Además, las alfombras de Carpet4You se encuentran el el 20% de las casas de Noruega, con un claro aumento en las ventas que los analistas prevén durante los próximos 12 años a tenor del 12% interanual. 

Sedes de la empresa
====================

* La **sede central/operativa** de la empresa está en el pueblo de El Carrascalejo, en Badajoz. Para este sede trabajan en torno a 700 personas, siendo aproximadamente 100 de ellas trabajadores *full-remote*.
* La **sede técnica** de la empresa está situada en Bilbao. Desde esta oficina se coordinan todas las operaciones IT a nivel internacional y dispone de uno de los Centros de Proceso de Datos de la empresa. Esta sede emplea a unas 200 personas.
* La sede de **Bruselas** (Bélgica) se dedica a las ventas por todo el centro y Este de Europa. Trabajan unas 150 personas en esta sede.
* La sede de **Bergen** (Noruega) se encarga de coordinar las ventas de todo el norte de Europa. La temperatura de los paises nórdicos hace necesaria la compra de alfombras a gran escala. 
* En tanto a los trabajadores *remotos*, aunque están distribuidos por el mundo, su área de acción se reduce a:

    * 15 empleados por toda Rusia. 
    * 10 empleados en Reino Unido e Irlanda.
    * 5 empleados en Minsk, Bielorrusia.

Ubicaciones de Proceso de Datos
================================

Centros de Proceso de Datos (CPD)
----------------------------------
La empresa dispone de 2 grandes centros de datos en Europa, aunque tiene salas de proceso en todas las sedes de la empresa. 

El CPD más importante se encuentra situado en una ubicación secreta en la ciudad de Bilbao. La Directiva de la empresa eligió esta ciudad pues es centro de interconexión global con cables submarinos como `MAREA <https://www.xataka.com/otros/cable-submarino-que-conecta-bilbao-eeuu-consigue-nuevo-record-26-2-tbps-transferencia>`__. Además, esta cuidad moderna provee de ingenieros recién graduados con ganas de aprender y ayudar a una gran empresa como Carpet4You a crecer. 

Puntos de Presencia (POPs)
---------------------------
Debido a la  característica distribuida de la empresa necesitamos tener puntos de presencia más allá de estos dos CPDs. 
La empresa dispondrá de salas de procesamiento de datos locales en cada una de sus sedes. En estas salas de proceso de datos se dispondrá de todo el *hardware* necesario para la conectividad de la sede, así como herramientas locales de compartición de archivos. 

Para la página web se utilizan los servicios del proveedor Cloudflare, con presencia en más de 200 ciudades, lo que asegura a la empresa una velocidad excelente en la carga de la página web pública. 

Nube pública
------------
Se utiliza la zona de Londres de Google Cloud Platform para alojar los sistemas de acceso remoto para los trabajadores en Reino Unido. Se ha elegido contratar servicios de nube pública debido a que el proceso de datos de mayor intensidad se produce en los centros propios y las necesidades técnicas son demasiado elevadas como para desplegar un equipo propio.

Control de acceso a la red
----------------------------
Si bien la empresa dispone de conexiones y usuarios VPN, se están migrando ciertas aplicaciones a Cloudflare Access, que permite gestión centralizada de los servicios de gestión de identidad. De esta forma, se evita tráfico local de VPN (que no suele ser eficiente). También se cachean los recursos estáticos en *border*. 


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

Dominio de la empresa
=====================
La empresa utiliza el dominio *carpet4you.site*