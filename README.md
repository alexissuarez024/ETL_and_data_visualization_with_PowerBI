# Appol Proyect
En este trabajo se realizaron procesos de ETL con pandas hacia un origen de datos "Appol_Datos_Origen" el cual representa las ventas durante los años 2019, 2020,2021 de una empresa ficticia y parodica relacionada a la tecnología.

[Link para interactuar con el tablero ](https://app.powerbi.com/view?r=eyJrIjoiZWU4NGM5OTgtMjFlNS00NWQ1LWI3Y2ItOTJmYmJkNTc2NzNhIiwidCI6IjA1NzFiYTFiLTViMzAtNGNlNi1hNGU0LWM0ZGM4NDUwMDJlMSIsImMiOjR9 "Link del tablero ")

### Origen de datos y procesado
El procesado de la data se realizo en el  notebook "cleaning_dataset_appol", alli encontrara las distintas transformaciones que serian necesarias para el posterior análisis. Resumiendolo contiene renombramiento de columnas, creación de columnas en base a una misma, casteo de datos y dropeo de columnas.

### El set utilizado

Una vez procesado el origen y aplicado transformaciones, se generan un set final "appol_clean_final". Al dejarlo listo para el analisis, trabajamos sobre el supuesto de que se solicita alojarlo en la base de datos ubicada en el servicio de RDS de AWS.

### La carga
Se realizo mediante un script de python "appol.py" y en el se encuentra el proceso que se realizo para poder cargarlo a la base de datos.
Y un script de configuración "config.py" que aloja el codigo para utilizar la conexión al servicio de BDD de AWS. Se trabajo con variables de entorno para resguardar los datos de la cuenta y para poder usar dichas variables se utilizó la libreria "python-dotenv"

Librerias utilizadas y que se encuentran en requeriments.txt:
- pandas
- psycopg2
- dotenv

### Analisis
Para esto se realizo un dashboard en Power BI en donde se utilizaron medias como:
- Margen
- Utilidad
- Totalidad de gastos e ingresos

Se destaca que en los 3 años de ventas se obtuvo una utilidad de $671M y un margen del 19 casi 20%.
Donde lideran en consumo tecnológico, América y Asia en 1er y 2do lugar correspondientemente y 3ro Europa muy por detras.
Destacando que tan solo en América, Estados Unidos representa más de la mitad ($165M) de su utilidad ($262M). Dispositivos como PC y Celulares le aportaron una utilidad de $96M con un margen de tan solo 19% al contrario como de aplicaciones, tv, música que le aportaron un margen de 40% en una utilidad de $68M.

### Imagen del tablero

![](https://github.com/alexissuarez024/ETL_and_data_visualization_with_PowerBI/blob/main/img/tablero.png)
