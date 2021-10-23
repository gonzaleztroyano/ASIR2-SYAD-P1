*************
Criptografía
*************

Ejercicio 4.1
=============
*Genera un par de claves asimétricas de un empleado que tendrá tu nombre, apellidos y tu correo electrónico de gmail. Captura la pantalla el comando utilizado y el resultado obtenido.*

.. note::

   Se utilizará el correo pablo@carpet4you.site	en vez de mi dirección personal de Gmail. 

Para generar un par de claves asimétricas debemos seguir las siguientes instrucciones:

.. code-block:: console
    
    pablo@carpet:~$ gpg --gen-key
    gpg (GnuPG) 2.2.12; Copyright (C) 2018 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    gpg: keybox '/home/pablo/.gnupg/pubring.kbx' created
    Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

    GnuPG needs to construct a user ID to identify your key.

    Real name: Pablo González
    Email address: pablo@carpet4you.site
    You are using the 'utf-8' character set.
    You selected this USER-ID:
        "Pablo González <pablo@carpet4you.site>"

    Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    gpg: /home/pablo/.gnupg/trustdb.gpg: trustdb created
    gpg: key 48CF9B50966CC9B7 marked as ultimately trusted
    gpg: directory '/home/pablo/.gnupg/openpgp-revocs.d' created
    gpg: revocation certificate stored as '/home/pablo/.gnupg/openpgp-revocs.d/D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7.rev'
    public and secret key created and signed.

    pub   rsa3072 2021-10-23 [SC] [expires: 2023-10-23]
        D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7
    uid                      Pablo González <pablo@carpet4you.site>
    sub   rsa3072 2021-10-23 [E] [expires: 2023-10-23]

Para ver las clave generada podemos utilzar el siguiente comando:

.. code-block:: console
    
    pablo@carpet:~$ gpg -k
    gpg: checking the trustdb
    gpg: marginals needed: 3  completes needed: 1  trust model: pgp
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: next trustdb check due at 2023-10-23
    /home/pablogontroya/.gnupg/pubring.kbx
    --------------------------------------
    pub   rsa3072 2021-10-23 [SC] [expires: 2023-10-23]
        D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7
    uid           [ultimate] Pablo González <pablo@carpet4you.site>
    sub   rsa3072 2021-10-23 [E] [expires: 2023-10-23]


Ejercicio 4.2
=============
*Genera un par de claves asimétricas que servirán para tu empresa que tendrá como datos el nombre de tu empresa y el correo electrónico del administrador de tu empresa. Captura la pantalla el comando utilizado y el resultado obtenido.*

Para generar un par de claves asimétricas ejecutar el comando siguiente. El comando nos pedirá el nombre y el correo electrónico que queremos utilizar para la generación. También la clave simétrica que protegerá la clave privada. 

.. code-block:: console
    
    gpg gen-key
    [...]
    public and secret key created and signed.

    pub   rsa3072 2021-10-23 [SC] [expires: 2022-01-21]
        0171E7FC0657E4CCFAEC3C23164857A2CDB61EEC
    uid                      Carpet4You Management (Las mejores alfombras del universo) <info@carpet4you.site>
    sub   rsa3072 2021-10-23 [E] [expires: 2022-01-21]


Ejercicio 4.3
=============
*Muestra las claves privadas de tu empleado y de tu empresa. Captura la pantalla el comando utilizado y el resultado obtenido.*

Para ver las claves privadas que tenemos en nuestro *keyring* debemos ejecutar el siguiente comando:

.. code-block:: console
    
    pablo@carpet:~$ gpg -k
    gpg: checking the trustdb
    gpg: marginals needed: 3  completes needed: 1  trust model: pgp
    gpg: depth: 0  valid:   2  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 2u
    gpg: next trustdb check due at 2022-01-21
    /home/pablogontroya/.gnupg/pubring.kbx
    --------------------------------------
    pub   rsa3072 2021-10-23 [SC] [expires: 2023-10-23]
        D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7
    uid           [ultimate] Pablo González <pablo@carpet4you.site>
    sub   rsa3072 2021-10-23 [E] [expires: 2023-10-23]

    pub   rsa3072 2021-10-23 [SC] [expires: 2022-01-21]
        0171E7FC0657E4CCFAEC3C23164857A2CDB61EEC
    uid           [ultimate] Carpet4You Management (Las mejores alfombras del universo) <info@carpet4you.site>
    sub   rsa3072 2021-10-23 [E] [expires: 2022-01-21]



Ejercicio 4.4 y 4.5
===================

*Exporta las claves privadas/públicas de tu empleado y de tu empresa a archivos que se entregaran con el proyecto. Por cada uno de ellos se tendrán los archivos ClavePublicaNombreApellidos.key que contendrá la clave pública y ClavePrivadaNombreApellidos.key que contendrá la clave privada del usuario y ClavePublicaNombreEmpresa.key y ClavePrivadaNombreEmpresa.key de las empresas.*

Para exportar las claves públicas:

.. code-block:: console
    
    pablo@carpet:~$ gpg --armor --output ClavePublicaPabloGonzalez.key --export D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7

    pablo@carpet:~$ gpg --armor --output ClavePublicaCarpet4You.key --export 0171E7FC0657E4CCFAEC3C23164857A2CDB61EEC


Para exportar las claves privadas (nos pedirá la clave simétrica):

.. code-block:: console
    
    pablo@carpet:~$ gpg --armor --output ClavePrivadaPabloGonzalez.key --export-secret-keys D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7
    
    pablo@carpet:~$ gpg --armor --output ClavePrivadaCarpet4You.key --export-secret-keys 0171E7FC0657E4CCFAEC3C23164857A2CDB61EEC



Ejercicio 4.6
=============

*En el moodle del instituto en el apartado del proyecto estarán las claves públicas y privadas de un tercer empleado genérico que tienes que importar al anillo de tu servidor de usuarios. Captura la pantalla el comando utilizado y el resultado obtenido.*

Una vez descargadas desde el Aula Virtual las claves, debemos extraer los .key del archivo comprimido tar.gz:

.. code-block:: console
    
    pablo@carpet:~$ tar -xf 'ClavesPublicayPrivada Empleado genérico .tar.gz'



.. warning::
    
    Se ha producido un error al importar la clave pública. Parece que ocupa 0 bytes:
    
    .. code-block:: console
        
        pablo@carpet:~$ ls -lah
        -rwxr-xr-x 1 pablo pablo 5241 Nov 11  2019 PrivateKeyEmpleadoGenerico.key
        -rwxr-xr-x 1 pablo pablo    0 Nov 11  2019 PublicKeyEmpleadoGenerico.key
   

Ejercicio 4.7
=============
*Cifra un fichero con el texto “Hola Mundo” y encriptarlo con el empleado genérico. Captura la pantalla el comando utilizado y el resultado obtenido. Entrega el fichero encriptado.*

.. code-block:: console
    
    pablo@carpet:~$ echo "Hola Mundo" > Empleado-PabloGonzález.txt
    pablo@carpet:~$ gpg -a -r pablo@carpet4you.site --encrypt Empleado-PabloGonzález.txt
    
    pablo@carpet:~$ ll E*
        -rw-r--r-- 1 pablogontroya pablogontroya  11 Oct 23 23:03 Empleado-PabloGonzález.txt
        -rw-r--r-- 1 pablogontroya pablogontroya 736 Oct 23 23:04 Empleado-PabloGonzález.txt.asc



Ejercicio 4.8
=============
*Desencripta el fichero. Captura la pantalla el comando utilizado y el resultado obtenido.*

Para desencriptar el fichero debemos utilizar el comando que podemos ver a continuación. Nos pedirá la clave simétrica de la clave privada. 

.. code-block:: console
    
    pablo@carpet:~$ gpg --decrypt Empleado-PabloGonzález.txt.asc 
    gpg: encrypted with 3072-bit RSA key, ID 8D27C3D26858C7E2, created 2021-10-23
        "Pablo González <pablo@carpet4you.site>"
    Hola Mundo



Ejercicio 4.9
=============
*Firma digitalmente con la clave asimétrica de tu empresa el fichero que has subido a la web en el anterior ejercicio creando una firma separada del archivo. Sube la firma y la clave pública a tu web junto a los hash para que un usuario pueda comprobar la autoría del fichero. Captura la pantalla el comando utilizado y el resultado obtenido.*

.. code-block:: console
    
    pablo@carpet:~$ gpg --output plano_CPD.pdf.sign --sign plano_CPD.pdf



Para verificar la firma del archivo podemos ejecutar:

.. code-block:: console
    
    pablo@carpet:~$ gpg --verify plano_CPD.pdf.sign 
    gpg: Signature made Sat 23 Oct 2021 11:19:36 PM CEST
    gpg:                using RSA key D5AA1DFFB6A4557305CECF4148CF9B50966CC9B7
    gpg: Good signature from "Pablo González <pablo@carpet4you.site>" [ultimate]
    gpg: WARNING: not a detached signature; file 'plano_CPD.pdf' was NOT verified!

