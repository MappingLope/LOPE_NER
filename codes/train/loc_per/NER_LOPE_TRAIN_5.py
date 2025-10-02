#!/usr/bin/env python
# coding: utf-8


from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
import torch, gc

columns = {0: 'text', 1: 'ner'}
data_folder = 'corpus/corpus_train/loc_per'
corpus: Corpus = ColumnCorpus(data_folder, columns, train_file='train.txt', test_file='test.txt', dev_file='dev.txt')
label_type = 'ner'
label_dict = corpus.make_label_dictionary(label_type=label_type, add_unk=False)

embeddings = TransformerWordEmbeddings(
    model='MMG/xlm-roberta-large-ner-spanish',
    layers='-1',
    subtoken_pooling='first',
    fine_tune=True,
    use_context=True
)

tagger = SequenceTagger(
    hidden_size=256,
    embeddings=embeddings,
    tag_dictionary=label_dict,
    tag_type='ner',
    use_crf=False,
    use_rnn=False,
    reproject_embeddings=False
)

trainer = ModelTrainer(tagger, corpus)

gc.collect()
torch.cuda.empty_cache()

trainer.fine_tune(
    'ner_fineTuning_5',
    learning_rate=5.0e-6,
    mini_batch_size=4,
    mini_batch_chunk_size=1,
    max_epochs=20,
    embeddings_storage_mode='gpu'
)
