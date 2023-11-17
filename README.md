## Haikus

Este código Python hace uso de **Modelos de Lenguaje con Aprendizaje Profundo (LLM's)**, específicamente la biblioteca **Spacy**, para procesar y analizar **haikus en españo**l. Utiliza técnicas de **tokenizació**n para dividir el texto en unidades lingüísticas más pequeñas llamadas **tokens**, los cuales son luego utilizados para aplicar patrones específicos en el texto mediante **objetos Matcher**. Estos patrones, diseñados para identificar **grupos de 2, 3 y 4 palabras** con ciertas características gramaticales, permiten el análisis de estructuras en los haikus. Además, el código realiza un conteo de sílabas en las palabras de las líneas coincidentes con los patrones y almacena aquellas que cumplen con las reglas establecidas en listas separadas. Finalmente, el **usuario puede ingresar un tema para el haiku**, y el programa genera aleatoriamente un haiku utilizando las líneas previamente seleccionadas que cumplen con las reglas de sílabas. Este enfoque demuestra cómo las **técnicas de procesamiento de lenguaje natural y tokenización** pueden ser implementadas en Python para realizar análisis lingüísticos avanzados y generar contenido poético. A continuación una descripción del código:

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

Se requiere instalar las siguientes librerias

```
python m pip install upgrade pip setuptools
pip install spacy
pip install syllapy
python m spacy download es_core_news_sm
```
