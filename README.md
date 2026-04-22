# Urban Grocers API

## Descripción
Este proyecto contiene pruebas automatizadas para la API de Urban Grocers, específicamente para el endpoint encargado de crear kits para un usuario.

El objetivo es validar distintos escenarios de entrada para el campo "name" y comprobar si la API se comporta de acuerdo con la documentación.

## Qué se está probando
Se cubren los siguientes escenarios:

- Nombre válido con 1 carácter
- Nombre válido con 511 caracteres
- Nombre vacío (debería devolver error)
- Nombre con más caracteres de los permitidos (512)
- Uso de caracteres especiales
- Uso de espacios en el nombre
- Valores numéricos como texto
- Falta del parámetro "name"
- Tipo de dato incorrecto (número en lugar de string)
  
## Qué se usó
- Python
- Pytest
- Requests

## Cómo correr los tests
1. Instalar dependencias: 
pip install pytest requests
2. Ejecutar las pruebas:
pytest create_kit_name_kit_test.py

## Estructura del proyecto
- configuration.py → URLs y endpoints de la API
- data.py → Cuerpos de las solicitudes
- sender_stand_request.py → Funciones para enviar requests
- create_kit_name_kit_test.py → Casos de prueba
- README.md → Documentación del proyecto
- .gitignore → Archivos ignorados
