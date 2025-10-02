# Mapping Lope: A Cartographic Exploration of the Comedia Nueva (NER) 🌍

_Mapping Lope: A Cartographic Exploration of the Comedia Nueva_ (2025–2027) is a Swiss National Science Fund (SNSF) project, in collaboration with PROLOPE (Unversitat Autònoma de Barcelona), that uses Digital Humanities tools to analyze the use of place names (toponyms) in Lope de Vega’s plays. Combining Philology, Literary Geography, and machine learning, it aims to reassess the link between theater genres and geography, and to explore how toponyms reflect the political and cultural context of Lope’s time. Through automated extraction of place names, interactive maps, graphs, and statistics, the project offers new insights into the role of space in Spanish Golden Age drama.

This repository contains the datasets and the scripts we have used to train our NER model with the [Flair](https://github.com/flairNLP/flair) framework, as well as the results. This model is based on the one developed by the members of the project [Desenrollando el cordel](https://github.com/DesenrollandoElCordel/pliegos-ner), and has been applied to detect the toponyms in the corpus of the _Comedia Nueva_, by Lope de Vega (359 plays). Many thanks to Elina Leblanc and Pauline Jacsont for their help and support!

Statistics showing the number of works in which each (standardised) place name is mentioned, and the total number of occurrences in the whole corpus, can be [found here](https://github.com/MiguelBetti/Lope_ner/blob/main/csv/Estadisticas.csv).

The final map is available [here](https://miguelbetti.github.io/Lope_peripleo/#/?/?/?/mode=points)

## ***Training - Fine-tuning***
The scripts we used for the fine-tuning of our model can be found [here](https://github.com/MappingLope/LOPE_NER/tree/main/codes).

The default Spanish NER model of Flair has been tested on 10 [random texts](https://github.com/MappingLope/LOPE_NER/tree/main/corpus/corpus_test). We then fine-tuned several open source models. The detailed results can be found [here](https://github.com/MappingLope/LOPE_NER/tree/main/results/).

1. The[bert-spanish-cased-finetuned-ner](https://huggingface.co/mrm8488/bert-spanish-cased-finetuned-ner) model (developped by Manuel Romero):

| 20 epochs     | Precision | Recall | F1-score |
|---------------|-----------|--------|----------|
| LOC           | 0.9710    | 0.9437 | 0.9571   |

2. The [xlm-roberta-large-ner-spanish](https://huggingface.co/MMG/xlm-roberta-large-ner-spanish), which gave us our best model:

| 20 epochs     | Precision | Recall | F1-score |
|---------------|-----------|--------|----------|
| LOC           | 0.9718    | 0.9718 | 0.9718   |

3. And the [mlm-spanish-roberta-base](https://huggingface.co/MMG/mlm-spanish-roberta-base) model:


| 20 epochs    | Precision | Recall | F1-score |
|--------------|-----------|--------|----------|
| LOC          | 0.9577    | 0.9577 | 0.9577   |

We also trained the NER models on a version of the corpus annotated with both location and person entities. However, this led to a light decrease in performance. The example below shows the output produced by ... model in this setting:

| 20 epochs	   | Precision | Recall | F1-score |
|--------------|-----------|--------|----------|
| PER          |  0.8424   | 0.8634 | 0.8528   |
| LOC          |  0.8929   | 0.8446 | 0.8681   |


To train the models, we have used the [Baobab HPC cluster](https://www.unige.ch/eresearch/en/services/hpc/) of the University of Geneva.


## ***Results***

The texts of our corpus have been annotated with the [BIO format](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) for the place names using this [script](https://github.com/MiguelBetti/Lope_ner/blob/main/NER_LOPE.py). To develop different maps with the place names, we transformed these results into several CSV files:

- Extraction of the place names, with [ner2csv.py](https://github.com/MiguelBetti/Lope_ner/blob/main/tools/ner2csv.ipynb).
- Enrichment of the [CSV file]() with information extracted from [Artelope](https://artelope.uv.es/basededatos/index.php) (title of the plays, genre, subgenre, publication date, etc.) and from Wikidata thanks to *Open Refine* (Wikidata identifier, geographical coordinates, type of place, normalised names).
- Conversion in JSON to create a map with [Peripleo](https://github.com/britishlibrary/peripleo) with the [csv2json.py](https://github.com/MiguelBetti/Lope_ner/blob/main/tools/csv2json.ipynb) script developped by Elina Leblanc. The code and datasets are available [here](https://github.com/MiguelBetti/Lope_peripleo).