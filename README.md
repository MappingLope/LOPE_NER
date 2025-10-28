# Mapping Lope: A Cartographic Exploration of the Comedia Nueva (NER) 🌍

_Mapping Lope: A Cartographic Exploration of the Comedia Nueva_ (2025-2027) is a post-doctoral research project supported by a [Postdoc.Mobility grant](https://data.snf.ch/grants/grant/235122) from the Swiss National Science Foundation (SNSF). It is being carried out by Miguel Betti at the PROLOPE Group (Universitat Autònoma de Barcelona) under the supervision of Prof. Sònia Boadas (Thal-IA - UAB).

Combining Philology, Literary Geography, and machine learning, the project uses Digital Humanities tools to analyze the use of place names (toponyms) in Lope de Vega’s plays. It aims to reassess the link between theater genres and geography, and to explore how toponyms reflect the political and cultural context of Lope’s time. Through the automated extraction of place names, as well as the creation of interactive maps, graphs, and statistical analyses, the project offers new insights into the role of space in Spanish Golden Age drama.

This repository contains the datasets and the scripts we have used to train our NER model with the [Flair](https://github.com/flairNLP/flair) framework, as well as the results. This model is based on the one developed by the members of the project [Desenrollando el cordel](https://desenrollandoelcordel.unige.ch/exist/apps/projet-cordel/inicio.html), directed by Prof. Constance Carta, and has been applied to detect the toponyms in the corpus of the _Comedia Nueva_, by Lope de Vega (364 plays). Many thanks to Elina Leblanc and Pauline Jacsont for their help and support!


## ***Training - Fine-tuning***
The scripts we used for the fine-tuning of our model can be found [here](https://github.com/MappingLope/LOPE_NER/tree/main/codes).

The default Spanish NER model of Flair has been tested on 10 [random texts](https://github.com/MappingLope/LOPE_NER/tree/main/corpus/corpus_test).  We then fine-tuned several open-source models using a dataset of 7,300 annotated sentences, including 719 location entities (LOC). Detailed results can be found [here](https://github.com/MappingLope/LOPE_NER/tree/main/results/).

1. [bert-spanish-cased-finetuned-ner](https://huggingface.co/mrm8488/bert-spanish-cased-finetuned-ner) model:

| 20 epochs     | Precision | Recall | F1-score |
|---------------|-----------|--------|----------|
| LOC           | 0.9710    | 0.9437 | 0.9571   |

2. [xlm-roberta-large-ner-spanish](https://huggingface.co/MMG/xlm-roberta-large-ner-spanish) model, our best-performing model:

| 20 epochs     | Precision | Recall | F1-score |
|---------------|-----------|--------|----------|
| LOC           | 0.9718    | 0.9718 | 0.9718   |

3. [mlm-spanish-roberta-base](https://huggingface.co/MMG/mlm-spanish-roberta-base) model:


| 20 epochs    | Precision | Recall | F1-score |
|--------------|-----------|--------|----------|
| LOC          | 0.9577    | 0.9577 | 0.9577   |

We also trained the NER models on a subset of the corpus annotated with both location (LOC) and person (PER) entities (7,300 sentences, including 4,326 PER and 841 LOC). However, this multi-entity setting led to a slight decline in performance. This reduction can be attributed mainly to the increased complexity of the task, semantic ambiguity in some entities, and class imbalance—particularly the predominance of PER over LOC, which also characterizes the full corpus.

The results below, obtained using the xlm-roberta-large-ner-spanish model, reflect performance under these conditions:

| 20 epochs	   | Precision | Recall | F1-score |
|--------------|-----------|--------|----------|
| PER          |  0.8812   | 0.9067 | 0.8938   | 
| LOC          |  0.8000   | 0.8235 | 0.8116   |


Model training was performed on the [Baobab HPC cluster](https://www.unige.ch/eresearch/en/services/hpc/) of the University of Geneva.


## ***Results***

The texts of our corpus have been annotated with the [BIO format](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) for the place names using this [script](https://github.com/MappingLope/LOPE_NER/blob/main/codes/recognition/loc/NER_LOPE_RECOGNITION.py). To develop different maps with the place names, we transformed these results into several CSV files:

- Extraction of the place names, with [ner2csv.py](https://github.com/MappingLope/LOPE_NER/blob/main/tools/ner2csv.ipynb).
- Enrichment of the [CSV file](https://github.com/MappingLope/LOPE_NER/blob/main/data/NER_LOPE.csv) with information extracted from [Artelope](https://artelope.uv.es/basededatos/index.php) (title of the plays, genre, subgenre, publication date, etc.) and from Wikidata thanks to *Open Refine* (Wikidata identifier, geographical coordinates, type of place, normalised names).
- Conversion in JSON to create a map with [Peripleo](https://github.com/britishlibrary/peripleo) with the [csv2json.py](https://github.com/MappingLope/LOPE_NER/blob/main/tools/csv2json.ipynb) script developped by Elina Leblanc.


Statistics showing the number of works in which each (standardised) place name is mentioned, and the total number of occurrences in the whole corpus, can be found [here](https://github.com/MappingLope/LOPE_NER/blob/main/data/STATS.csv).

Please explore our [map](https://mappinglope.github.io/peripleo-lope)! (old version: 330 plays; currently working on the new one with 364 plays)