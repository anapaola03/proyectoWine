# Proyecto Wine API

Este proyecto proporciona una API Flask para acceder a datos sobre vinos y realizar análisis de clustering.

## Configuración y Ejecución del Contenedor Docker

Asegúrate de tener Docker instalado en tu máquina.

1. Clona este repositorio:
   ```bash
   git clone https://github.com/anapaola03/proyectoWine.git

   Navega al directorio del proyecto
   Construye la imagen del contenedor Docker
   Ejecuta el contenedor:
2. Acceso a la API
Una vez que el contenedor está en ejecución, puedes acceder a la API a través de http://localhost:5000.

3. Obtener Datos del Vino
Ruta: /get_wine_data
Método: GET
Descripción: Obtiene datos sobre vinos en formato JSON.
Ejecutar Análisis y Clustering
Ruta: /run_analysis
Método: GET
Descripción: Realiza análisis y clustering de los datos. Retorna un mensaje de éxito y una imagen de resultados.
