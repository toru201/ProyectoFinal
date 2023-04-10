# ProyectoFinal
Nombre: Omar Guzmán
Fecha: 11.04.2023

Descripción del Proyecto:

El proyecto es sobre una aplicación que permite a los vendedores de Coca Cola poder registrar los clientes a los cuales se les ha vendido un producto, así como también tener una base de datos de todos los productos de la compañía y el stock que se maneja. Es un CMR en construcción, la idea es que en un futuro se pueda incluir los productos que nos han comprado nuestros clientes, incluso anexar la factura o boleta de compras anteriores.

La URL para acceder al proyecto es: http://127.0.0.1:8000/AppCoder/index/

Caso de Prueba 1: Creación de usuarios

Mediante la página de inicio, podemos entrar a la página de registro de usuario URL: http://127.0.0.1:8000/AppCoder/register/ donde podemos ingresar un username, email y contraseña. Una vez ingresemos estos datos, podemos posteriormente logearnos con nuestro usuario y contraseña, en el URL: http://127.0.0.1:8000/AppCoder/login/

Caso de Prueba 2: Creación de clientes

Una vez nos hemos logeado como usuario en la URL http://127.0.0.1:8000/AppCoder/login/ podemos crear clientes en nuestra base de datos mediante la URL: http://127.0.0.1:8000/AppCoder/clientes/, con su nombre, apellido y correo electrónico.

Caso de Prueba 3: Edición de clientes

Una vez ya hemos creado los clientes mediante el paso anterior, tenemos una herramienta que nos permite hacer un CRUD completo de estos clientes en el URL: http://127.0.0.1:8000/AppCoder/mostrar_clientes/, aquí se listarán todos los clientes creados con sus respectivos datos. Mediante los botones "Editar" o "Eliminar" podemos manipular los datos del cliente que necesitemos corregir o eliminar. Tambien podemos listar todos los productos de nuestra base de datos y tenemos disponible un CRUD en el URL: http://127.0.0.1:8000/AppCoder/mostrar_codigos/
