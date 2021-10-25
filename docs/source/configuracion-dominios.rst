****************************************
Configuración de dominios de la empresa
****************************************

Toda la empresa se organiza en torno al dominio *Carpet4You.site*.

La web pública se encuentra en `https://carpet4you.site <https://carpet4you.site>`_.

Para los equipos internos se crean los siguientes subdominios DNS:
 * *.corp.carpet4you.site*, sobre este subdominio se organizarán los recursos de la empresa que se utilizan directamente por los empleados. Lo que podríamos identificar como una especie de *frontend*. 
 * *.people.carpet4you.site*, sobre este subdominio se alojan los equipos cliente de las trabajadoras u trabajadores, siguiendo una nomenclatura definida para identificarlos. 
 * *.int.carpet4you.site*, dentro de este subdominio se organizarán los recursos de la empresa que funcionan en una capa de abstracción inferior. 
 * Los equipos físicos de los CPD, en caso de poder ser comunicados directamente desde el exterior (entiéndase exterior como una conexión SSH, siempre asegurada, limitada y autenticada) tendrán un subdominio que coincidirá con el CPD al que pertenecen. Por ejemplo, *s25.a1.1.bru.int.carpet4you.site* pertenece al servidor número 25, del bastidor A1, en la sala 1, del CPD de Bruselas.
  