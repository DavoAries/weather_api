Este proyecto fue desarrollado por Guillermo Mundarain, Estudiante de Ingenieria de Sistemas, para la materia Programación 5 con el profesor Elías Vargas, el 7 de noviembre de 2025. 

Consiste en una API REST construida con Django y Django REST Framework que permite registrar y consultar temperaturas por ciudad, con autenticación por token mediante el endpoint /api-token-auth/, vistas protegidas para crear, actualizar y eliminar registros, y una vista pública en /api/temperatures/ para consultar los datos. 
Se puede probar localmente creando un usuario con create_user, obteniendo el token con curl, y realizando peticiones autenticadas con el encabezado Authorization: Token <tu_token>. 
El proyecto está configurado con .gitignore para excluir archivos sensibles como db.sqlite3, .env y __pycache__, y cuenta con pruebas automatizadas en temperatures/tests.py. 
Para instalarlo, se recomienda clonar el repositorio, crear un entorno virtual, instalar dependencias con pip, ejecutar migraciones, iniciar el servidor con runserver, y probar los endpoints desde el navegador o terminal.
El código está organizado en módulos limpios, con rutas definidas en weather_api/urls.py y lógica en temperatures/views.py, y está listo para ser extendido o desplegado en producción.
