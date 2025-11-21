Este proyecto fue desarrollado por Guillermo Mundarain, estudiante de Ingeniería de Sistemas, para la materia Programación 5 con el profesor Elías Vargas el 7 de noviembre de 2025, y consiste en una API REST construida con Django y Django REST Framework que permite registrar y consultar temperaturas por ciudad, con autenticación por token mediante el endpoint /api-token-auth/, vistas protegidas para crear, actualizar y eliminar registros, y una vista pública en /api/temperatures/ para consultar los datos; el proyecto está configurado con .gitignore para excluir archivos sensibles como db.sqlite3, .env y __pycache__, cuenta con pruebas automatizadas en temperatures/tests.py, y se instala clonando el repositorio, creando un entorno virtual, instalando dependencias con pip, ejecutando migraciones y corriendo el servidor con runserver; la documentación se genera con drf-yasg y se visualiza en Swagger UI y Redoc, con capturas incluidas en la carpeta docs/ que muestran los endpoints disponibles , la ejecución de un GET , la creación de un registro con POST , la eliminación con DELETE , y la documentación técnica en Redoc , además de ejemplos de respuesta JSON como:
[
  {
    "id": 1,
    "city": "Caracas",
    "temperature": "29.50",
    "last_updated": "2025-11-09T12:14:20.706122-04:00"
  }
]

