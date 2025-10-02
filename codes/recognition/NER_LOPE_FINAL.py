#!/usr/bin/env python
# coding: utf-8

from flair.data import Sentence 
from flair.models import SequenceTagger
tagger = SequenceTagger.load("ner_bertSpanish_fineTuning3/final-model.pt")
import re
import os

clean_unicode = {
    "B-ORG": "O",
    "B-MISC": "O",
    "B-PER": "O",
    "I-ORG": "O",
    "I-MISC": "O",
    "I-PER": "O"  
}


folder = 'corpus/corpus_full_clean'

for f in os.listdir(folder):
    if f.endswith('.txt'):
        txt_path = os.path.join(folder, f)
        label, ext = os.path.splitext(f)
        with open(txt_path, encoding='utf-8') as t:
            text = t.read()
            text_normalized = " ".join(text.split())
            sentence = Sentence(text_normalized)
            tagger.predict(sentence)
            for entity in sentence.get_spans('ner'):
                prefix = 'B-'
                for token in entity:
                    token.set_label('ner-bio', prefix + entity.tag)
                    prefix = 'I-'
            output = ""        
            for token in sentence:
                output += str(token.get_label('ner-bio'))
                output += "\n"
            result = re.sub(r"([A-Z]\w+\[[0-9]+\]:\s\")([A-Z a-z 0-9 .,?!:¿¡…\'\*´ `’‘℣Đ=æǝ°>\—\-\_–\(\)\¬\«\»;~óòáàâíìñéèúüùäëïöÀÁÉÈÊËÍÌÎÏÑÓÒÔÖÚÙÛÜ\"\"]+)(\"\s→\s)([A-Z-]*)(\s\([0-9 .]*\))", r"\2 \4", output)
            for c in clean_unicode:
                result = re.sub(c, clean_unicode[c], result)
            with open ('corpus/corpus_full_out/' + label + '.txt', 'w', encoding='utf-8') as x:
                x.write(result)

