**************************
Cálculo potencia del SAI
**************************

Viendo el plano del CPD Bruselas nos percatamos de la gran cantidad de equipos que puede alojar:



.. image :: images/ASIR2.SYAD.P1.2.png
   :width: 500
   :align: center
   :alt: Plano del CPD
|br|

Cálculo del número de equipos
=============================

Cada zona en naranja tiene espacio para 3 racks estandar. Serán racks de 42U x 19 pulgadas, aproximadamente 2 metros de alto por 50cm de ancho. 

Con un sencillo cálculo podemos obtener la cifra de hasta 72 racks que podemos tener funcionando en el CPD. La sección *D* de los racks [#nota1]_ contará con los equipos de conectividad y balanceo de carga entre los servidores. La comunicación con el exterior se realiza en los *border routers*, situados en la planta sótano del edificio.

En este momento se estima que únicamente se está utilizando aproximadamente la mitad del espacio. Por tanto tenemos unos 35 racks que asegurar. 

Aunque estos racks tienen hasta 42U para el despliegue de equipos,se están utilizando 30, evitando situar los equipos en las posiciones inferiores para evitar que las trabajadoras y trabajadores tengan que agacharse y mantener posiciones poco ergonómicas. 

 .. important ::
    Por tanto tenemos 35 racks y 30 Us = 1050 U disponibles 

No todos los equipos ocupan 1U, unos 300 aproximadamente ocupan 2U, los dedicados al almacenamiento en Hadoop. Los resultados son: 600U ocupadas por 300 equipos dedicados al almacenamiento, 350U con 350 equipos dedicados al procesamiento y 100U ocupadas por 100 equipos dedicados a la interconexión.

Cálculo de la potencia de los equipos
======================================

En la elección de los dispositivos se ha tenido en cuenta la eficiencia y el consumo energético. 

Se toma una media de 200W por equipo. Los switches y equipos de conectividad consumen menos que los equipos de almacenamiento, y estos a su vez menos que los equipos de procesamiento.

 .. important ::

      Tenemos por tanto 200W * 750 equipos = 150 000 W


Cálculo de la capacidad necesaria de respaldo
==============================================

El objetivo de est CPD es estar siempre operativo. En cualquier caso, la empresa puede permitirse durante un espacio limitado del tiempo la pérdida de un CPD sin que esto afecte a las operaciones visibles de la empresa. El SLO [#nota2]_ es del 100%, pero el SLA [#nota3]_ acordado con la ejecutiva de la empresa es menor, del 99,5%. Tener un SLA del 99,5% significa no estar más de 1,8 días fuera de servicio en un periodo de 1 año natural.

Sin embargo, gracias a la característica distribuida de la empresa y a nuestro sistema de control DNS podríamos redirigir algunos servicios a otro CPD mientras dure la incidencia en un CPD dado. 

Los servicios internos podrían verse afectados, sobre todo los menos cruciales. El objetivo crucial es que la parte visible de la empresa (web, portales de relaciones con clientes) no se vea afectado y la diferencia de rendimiento sea mínima. 

Por tanto, la capacidad energética de respaldo se ha calculado para alimentar los sistemas durante aproximadamente 3h para los equipos de conectividad principal y *critical* (gestión interna, gestión de grabaciones y red interna).  

Para el resto de equipos, con mantenimiento de 1h hora la empresa ha calculado que será suficiente. 

En primera instancia se ha pensado en las soluciones UPS de AEG, de la gama PROTECT 4. Esta gama está especialmente pensado para Data Centers e infraestructuras crítcas. Como curiosidad, son los que utilizan en el provedor de servicios de hosting alemán Strato [#nota4]_ .

Si se utilizara esta gama sería necesario instalarlos en una sala especialmente dedicada en el sotáno, debido a su peso (más de 3 toneladas) y sus dimensiones (2100x1915x960 mm, Ancho, Alto, Fondo). 


 .. important ::

    Por tanto, calculamos que:
    * 1h de actividad para un armario no crítico. Resistencia calculada de 200W * 30U = 6000W.  
    * 3h de actividad para un armario crítico. Resistencia calculada de 200W * 20U = 4000W.


.. rubric:: Notas al pie de página

.. [#nota1] Cada conjunto de 3 racks está identificado por un código único, que no solo lo identifica a nivel de CPD, sino de toda la empresa. De esta forma *S-BRU-2-C1* significa *Servidor, en CPD BRUselas, sala 2, sección C, conjunto 1*. En Bilbao la nomenclatura es similar, cambiando *BRU* por *BIO*, que es el distintivo del aeropuerto de la ciudad. 
.. [#nota2] *Service Level Objective*, Objetivo de nivel de servicio. Lo que se espera que el servicio esté disponible.
.. [#nota3] *Service Level Agreement*, Acuerdo de nivel de servicio. Aunque se utiliza en acuerdos comerciales, en Carpet4You la utilizamos para definir el mínimo de tiempo que debe estar completamente operativo el CPD.
.. [#nota4] En `esta página <https://www.aegps.com/en/technology/references/strato/>`_ se puede obtener la referencia del cliente.

.. |br| raw:: html

   <br />
