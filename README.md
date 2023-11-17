## Haikus

Este código en Python utiliza la biblioteca *Spacy* para procesar y analizar *haikus en español*. A continuación una descrición del código:

- Descarga y carga del modelo de procesamiento de lenguaje natural:
  -   Descarga el modelo preentrenado en español para procesamiento de lenguaje natural (NLP) utilizando Spacy.

- Lectura de haikus desde un archivo de texto:
  - Lee haikus almacenados en un archivo de texto llamado "database.txt" y almacena el texto en la variable haikus_data.
    
-  Creación de objetos Matcher para patrones específicos de palabras:
  -  Utiliza Spacy Matcher para buscar patrones de palabras en los haikus.
  -  Define patrones para grupos de 2, 3 y 4 palabras, especificando las partes del discurso (POS) y otras condiciones.

- Identificación de patrones en los datos de los haikus:
  - Procesa los haikus con Spacy y utiliza los objetos Matcher para identificar coincidencias de patrones de 2, 3 y 4 palabras.
    
 - Conteo de sílabas y almacenamiento de líneas que cumplen con las reglas:
   - Itera sobre los resultados del Matcher, cuenta las sílabas de cada palabra en las líneas coincidentes y almacena las líneas que cumplen con la regla de sílabas en listas separadas para líneas de 5 y 7 sílabas.

- Interacción con el usuario:
- Solicita al usuario que ingrese el tema del haiku.

- Generación aleatoria de un haiku:
  - Verifica la disponibilidad de opciones antes de intentar elegir aleatoriamente.
  - Si hay líneas de 5 y 7 sílabas disponibles, genera e imprime un haiku aleatorio utilizando estas líneas. Si no hay opciones, muestra un mensaje indicando que no se encontraron patrones para el tema proporcionado.
    
El código utiliza Spacy y un Matcher para analizar haikus en español, identifica patrones de palabras específicos, cuenta las sílabas y genera haikus aleatorios basados en las líneas que cumplen con las reglas establecida.

Se requiere instalar las siquientes librerias

```
python m pip install upgrade pip setuptools
pip install spacy
pip install syllapy
python m spacy download es_core_news_sm
```
