#!/usr/bin/env python
# coding: utf-8

import os
import re
from flair.data import Sentence
from flair.models import SequenceTagger

# Cargar el modelo
tagger = SequenceTagger.load("flair/ner-spanish-large")

# Diccionario para limpiar etiquetas que no quieres
clean_unicode = {
    "B-ORG": "O",
    "B-MISC": "O",
    "B-PER": "O",
    "I-ORG": "O",
    "I-MISC": "O",
    "I-PER": "O"
}

# Carpeta con los textos de entrada
folder = 'corpus/corpus_test'

# Carpeta donde guardar los resultados
output_dir = os.path.join(folder, 'corpus_test_out')
os.makedirs(output_dir, exist_ok=True)  # crea la carpeta si no existe

# Procesar cada archivo .txt en la carpeta
for f in os.listdir(folder):
    if f.endswith('.txt'):
        txt_path = os.path.join(folder, f)
        label, ext = os.path.splitext(f)

        # Leer texto original
        try:
            with open(txt_path, encoding='utf-8') as t:
                text = t.read()
        except Exception as e:
            print(f"Error leyendo {txt_path}: {e}")
            continue

        # Normalizar el texto
        text_normalized = " ".join(text.split())
        sentence = Sentence(text_normalized)

        # Predecir entidades
        tagger.predict(sentence)

        # Convertir etiquetas a formato BIO
        for entity in sentence.get_spans('ner'):
            prefix = 'B-'
            for token in entity:
                token.set_label('ner-bio', prefix + entity.tag)
                prefix = 'I-'

        # Construir salida en texto
        output = ""
        for token in sentence:
            output += str(token.get_label('ner-bio')) + "\n"

        # Aplicar regex para limpiar
        result = re.sub(
            r"([A-Z]\w+\[[0-9]+\]:\s\")([A-Za-z0-9 .,?!:¿¡…'*´ `’‘℣Đ=æǝ°>\—\-\_–\(\)\¬\«\»;~óòáàâíìñéèúüùäëïöÀÁÉÈÊËÍÌÎÏÑÓÒÔÖÚÙÛÜ\"]+)(\"\s→\s)([A-Z-]*)(\s\([0-9 .]*\))",
            r"\2 \4",
            output
        )

        # Reemplazar etiquetas no deseadas
        for c in clean_unicode:
            result = re.sub(c, clean_unicode[c], result)

        # Ruta de salida
        out_path = os.path.join(output_dir, f'{label}.txt')

        # Guardar resultado
        try:
            with open(out_path, 'w', encoding='utf-8') as x:
                x.write(result)
        except Exception as e:
            print(f"Error escribiendo {out_path}: {e}")
