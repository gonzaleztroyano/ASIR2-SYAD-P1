*******************************************
Integridad de la información de la empresa
*******************************************

A la web de la empresa (`Carpet4You.site <https://carpet4you.site>`_) se ha subido un documento (plano_CPD.pdf).

Lo primero que hacemos es obtener el archivo, esto normalmente se hace antes de crear subirlo a la web, pero al estar en un máquina virtual es así más sencillo

.. code-block:: console
    pablo@carpet:~$ curl https://carpet4you.site/images/plano_CPD.pdf -o plano_CPD.pdf

Una vez lo tenemos debemos generar las sumas de comprobación, utilizando los diferentes sistemas que tenemos para ello. 

Realización de sumas de comprobación
=====================================

Suma de comprobación MD5
------------------------

.. code-block:: console

    pablo@carpet:~$ md5sum plano_CPD.pdf 
    a68fed06b2892d8d3de98f6a11f61414  plano_CPD.pdf


Suma de comprobación SHA256
---------------------------

.. code-block:: console

    pablo@carpet:~$ sha256sum plano_CPD.pdf 
    2e4dd97fb037c115938022556020da86080656c85df963c24f1260489cf2e261  plano_CPD.pdf

Suma de comprobación SHA512
---------------------------
.. code-block:: console

    pablo@carpet:~$ sha512sum plano_CPD.pdf 
    1ec7ac99fa424a958e8f046f31aff6b524aa80cb860111ac2d0480f0282ec2bad8af35cee85cdde57708a5f2049b02e82628ec2b28ac7a6b194b7b6f7cabf0b1  plano_CPD.pdf



Una vez generados los *checksums*, también llamados *sumas de comprobación*, *huellas digitales* o *sumas de verificación* debemos subirlo a la web. 

A continuación se recogen las sumas en esta página web:

+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Método de generación |                                                           Suma generada                                                          |
+======================+==================================================================================================================================+
|          MD5         | a68fed06b2892d8d3de98f6a11f61414                                                                                                 |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
|        SHA256        | 2e4dd97fb037c115938022556020da86080656c85df963c24f1260489cf2e261                                                                 |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
|        SHA512        | 1ec7ac99fa424a958e8f046f31aff6b524aa80cb860111ac2d0480f0282ec2bad8af35cee85cdde57708a5f2049b02e82628ec2b28ac7a6b194b7b6f7cabf0b1 |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+