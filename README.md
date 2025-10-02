# Mapping Lope: A Cartographic Exploration of the Comedia Nueva (NER) 🌍

_Mapping Lope: A Cartographic Exploration of the Comedia Nueva_ (2025–2027) is a Swiss National Science Fund (SNSF) project that uses Digital Humanities tools to analyze the use of place names (toponyms) in Lope de Vega’s plays. Combining Philology, Literary Geography, and machine learning, it aims to reassess the link between theater genres and geography, and to explore how toponyms reflect the political and cultural context of Lope’s time. Through automated extraction of place names, interactive maps, graphs, and statistics, the project offers new insights into the role of space in Spanish Golden Age drama.

This repository contains the datasets and the scripts we have used to train our NER model with the [Flair](https://github.com/flairNLP/flair) framework, as well as the results. This model is based on the one developed by the members of the project [Desenrollando el cordel](https://github.com/DesenrollandoElCordel/pliegos-ner), and has been applied to detect the toponyms in the corpus of the _Comedia Nueva_, by Lope de Vega (359 plays). Statistics showing the number of works in which each (standardised) place name is mentioned, and the total number of occurrences in the whole corpus, can be [found here](https://github.com/MiguelBetti/Lope_ner/blob/main/csv/Estadisticas.csv).

Many thanks to Elina Leblanc and Pauline Jacsont for their help and support!

The final map is available [here](https://miguelbetti.github.io/Lope_peripleo/#/?/?/?/mode=points)

## ***Training - Fine-tuning***
The scripts we used for the fine-tuning of our model can be found [here](https://github.com/MappingLope/LOPE_NER/tree/main/codes).

The default Spanish NER model of Flair has been [tested](https://github.com/MappingLope/LOPE_NER/blob/main/codes/NER_TEST.py) on 10 [random texts](https://github.com/MappingLope/LOPE_NER/tree/main/corpus/corpus_test). We have then fine-tuned the [bert-spanish-cased-finetuned-ner](https://huggingface.co/mrm8488/bert-spanish-cased-finetuned-ner) model (developped by Manuel Romero), to obtein a first model. The results are available [here](https://github.com/MappingLope/LOPE_NER/tree/main/results/ner_bertSpanish_fineTuning1).

| LOC (20 epochs) | Precision | Recall | F1-score |
|---------------|-----------|--------|----------|
| Micro avg     | 0.9266    | 0.7372 | 0.8211   |
| Macro avg     | 0.9266    | 0.7372 | 0.8211   |
| Weighted avg  | 0.9266    | 0.7372 | 0.8211   |

We have also tried the [xml-roberta-large](https://huggingface.co/MMG/xlm-roberta-large-ner-spanish) model, multilingual, and the Spanish version [xlm-roberta-large-ner-spanish](https://huggingface.co/MMG/xlm-roberta-large-ner-spanish), which gave us our best model. The results are available [here](https://github.com/MappingLope/LOPE_NER/tree/main/results/ner_bertSpanish_fineTuning2) and [here](https://github.com/MappingLope/LOPE_NER/tree/main/results/ner_bertSpanish_fineTuning3).

| LOC (20 epochs) | Precision | Recall | F1-score |
|---------------|-----------|--------|----------|
| Micro avg     | 0.9533    | 0.7445 | 0.8361   |
| Macro avg     | 0.9533    | 0.7445 | 0.8361   |
| Weighted avg  | 0.9533    | 0.7445 | 0.8361   |


| LOC (20 epochs) | Precision | Recall | F1-score |
|--------------|-----------|--------|----------|
| Micro avg    | 0.9380    | 0.8832 | 0.9098   |
| Macro avg    | 0.9380    | 0.8832 | 0.9098   |
| Weighted avg | 0.9380    | 0.8832 | 0.9098   |

We also trained the NER models on a version of the corpus annotated with both location and person entities. However, this led to a decrease in performance. The example below shows the output produced by Flair’s default NER model in this setting:

|			   | Precision | Recall | F1-score |
|--------------|-----------|--------|----------|
| PER          |  0.8424   | 0.8634 | 0.8528   |
| LOC          |  0.8929   | 0.8446 | 0.8681   |


To train the models, we have used the [Baobab HPC cluster](https://www.unige.ch/eresearch/en/services/hpc/) of the University of Geneva.


## ***Results***

The texts of our corpus have been annotated with the [BIO format](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) for the place names using this [script](https://github.com/MiguelBetti/Lope_ner/blob/main/NER_LOPE.py). To develop different maps with the place names, we transformed these results into several CSV files:

- Extraction of the place names, with [ner2csv.py](https://github.com/MiguelBetti/Lope_ner/blob/main/tools/ner2csv.ipynb).
- Enrichment of the [CSV file]() with information extracted from [Artelope](https://artelope.uv.es/basededatos/index.php) (title of the plays, genre, subgenre, publication date, etc.) and from Wikidata thanks to *Open Refine* (Wikidata identifier, geographical coordinates, type of place, normalised names).
- Conversion in JSON to create a map with [Peripleo](https://github.com/britishlibrary/peripleo) with the [csv2json.py](https://github.com/MiguelBetti/Lope_ner/blob/main/tools/csv2json.ipynb) script developped by Elina Leblanc. The code and datasets are available [here](https://github.com/MiguelBetti/Lope_peripleo).