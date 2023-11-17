# -*- coding: utf-8 -*-

import spacy.cli
from spacy.matcher import Matcher
import syllapy
import random

# Descarga el modelo de procesamiento de lenguaje natural en español
spacy.cli.download("es_core_news_sm")
nlp = spacy.load("es_core_news_sm")

# lenguaje natural en inglés --> spacy.cli.download("en_core_web_sm")

# Lee haikus desde un archivo de texto
#Lee los haikus desde un archivo de texto llamado "database.txt" y almacena el texto en la variable haikus_data.
with open("database.txt", "r", encoding="utf-8") as file:
    haikus_data = file.read()

#  Crea objetos Matcher para buscar patrones específicos de palabras en el texto.
#  Utiliza los objetos Matcher para buscar patrones de grupos de palabras (2, 3 y 4 palabras) en el texto de los haiku

# Grupo de 2 palabras
matcher2w = Matcher(nlp.vocab)
pattern = [{"POS": {"IN": ["NOUN", "ADV", "ADJ", "ADP"]}},
        {"POS": {"IN": ["VERB", "NOUN"]}}]
matcher2w.add("2words", [pattern])

# Grupo de 3 palabras
matcher3w = Matcher(nlp.vocab)
pattern = [{"POS": {"IN": ["NOUN", "ADV", "ADJ", "VERB", "ADP"]}},
        {"IS_ASCII": True, "IS_PUNCT": False},
        {"POS": {"IN": ["VERB", "NOUN", "ADV", "ADJ"]}}]
matcher3w.add("3words", [pattern])

# Grupo de 4 palabras
matcher4w = Matcher(nlp.vocab)
pattern = [{"POS": {"IN": ["NOUN", "ADV", "ADJ", "VERB", "ADP"]}},
        {"IS_ASCII": True, "IS_PUNCT": False},
        {"IS_ASCII": True, "IS_PUNCT": False},
        {"POS": {"IN": ["VERB", "NOUN", "ADV", "ADJ"]}}]
matcher4w.add("4words", [pattern])

# Identificar patrones en los datos de los haikus
doc = nlp(haikus_data)
matches2w = matcher2w(doc)
matches3w = matcher3w(doc)
matches4w = matcher4w(doc)

# Itera sobre los resultados de Matcher, cuenta las sílabas y almacena las líneas en las listas lines_5_syll y lines_7_syll si cumplen con la regla de sílabas.
lines_5_syll = []
lines_7_syll = []

# En spaCy, cuando se procesa un texto con nlp(texto), el resultado es un objeto Doc que contiene una secuencia de tokens.
#En este bucle, for token in span: itera sobre cada token en el span 
# (un fragmento del texto que coincide con el patrón definido por el Matcher). 
# Luego, se utiliza token.text para acceder al texto de cada token y contar las sílabas de cada palabra en el span.

for match_id, start, end in matches2w + matches3w + matches4w:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]

    syllable_count = 0

    for token in span:
        syllable_count += syllapy.count(token.text)
    if syllable_count == 5:
        if span.text not in lines_5_syll:
            lines_5_syll.append(span.text)
    if syllable_count == 7:
        if span.text not in lines_7_syll:
            lines_7_syll.append(span.text)

# Solicitar al usuario que ingrese el tema
tema_usuario = input("Ingrese el tema del haiku: ")

# Verificar si hay opciones disponibles antes de intentar elegir aleatoriamente
if lines_5_syll and lines_7_syll and lines_5_syll:
    # Generar e imprimir un haiku
    print("{0}\n{1}\n{2}".format(random.choice(lines_5_syll), random.choice(lines_7_syll), random.choice(lines_5_syll)))
else:
    print("No se encontraron patrones para el tema proporcionado. Intenta con otro tema.")
