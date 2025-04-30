# Water Data – External Sources
This folder is for storing water-related datasets from https://www.ine.es/dynt3/inebase/index.htm?padre=8709&capsel=8710

## :zap: Note 
I do **not** inculde the raw data in this repository as it does not belong to me. Please download the data from the sources linked above.
Download the data one by one, click in 'consultar todo' and download the data in csv separated by ";"

## :construction: Folder Structure
- `raw/`: Unmodified files.
- `processed/`: Files loaded into postgres.

## :arrow_down: Data sources
I am downloading each dataset in the raw folder with the same name and i am adding the metric used in the datasets. So an example of a name i am using is like: `Captación realizada por la propia empresa por comunidades y ciudades autónomas, tipo de captación y periodo. - miles_m3.csv`

### 1 Suministro y saneamentio del agua
- Indicadores sobre el suministro de agua por comunidades y ciudades autónomas
- Volumen de agua disponible (potabilizada y no potabilizada) por comunidades y ciudades autónomas, tipo de indicador y periodo.
- Volumen de agua suministrada a la red por comunidades y ciudades autónomas, tipo de indicador y periodo.
- Distribución de agua registrada por comunidades y ciudades autónomas, grupos de usuarios e importe y periodo.
- Distribución de agua registrada, usuario y periodo.
- Recogida y tratamiento de las aguas residuales por comunidades y ciudades autónomas, tipo de indicador y periodo.
- Destino de las aguas residuales tratadas por comunidades y ciudades autónomas, lugar de destino y periodo
- Usos del agua reutilizada por comunidades y ciudades autónomas, tipo de uso y periodo
- Destino de los lodos generados por comunidades y ciudades autónomas, tipo de destino y periodo
### 2 Indicadores sobre el agua
- Indicadores sobre el suministro de agua por comunidades y ciudades autónomas
- Descarga ficheros Información tabla Indicadores sobre las aguas residuales por comunidades y ciudades autónomas
- Descarga ficheros Información tabla Indicadores economicos por comunidades y ciudades autónomas
- Descarga ficheros Información tabla Indicadores estructurales de la red por comunidades autónomas

# :rotating_light: Run script to clean data
```
python data_formatter.py
```
This will clean data, it will merge the df into one, with ceuta as region_code=18 and Total NAciona =00. As well creates a csv with region_code, region to insert in the database.