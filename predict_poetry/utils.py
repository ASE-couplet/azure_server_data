#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os

VOCAB_SIZE = 6000
SEP_TOKEN = 0
PAD_TOKEN = 5999

import sys
sys.path.append("/home/site/wwwroot/predict_poetry")
root = "/home/site/wwwroot/predict_poetry"
DATA_RAW_DIR = os.path.join(root, 'data/raw')
DATA_PROCESSED_DIR = os.path.join(root, 'data/processed')
DATA_SAMPLES_DIR = os.path.join(root, 'data/samples')
MODEL_DIR = os.path.join(root, 'model')
LOG_DIR = os.path.join(root, 'log')


if not os.path.exists(DATA_PROCESSED_DIR):
    os.mkdir(DATA_PROCESSED_DIR)
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)


def embed_w2v(embedding, data_set):
    embedded = [[embedding[x] for x in sample] for sample in data_set]
    return embedded


def apply_one_hot(data_set):
    applied = [[to_categorical(x, num_classes=VOCAB_SIZE)[0] for x in sample] for sample in data_set]
    return applied


def apply_sparse(data_set):
    applied = [[[x] for x in sample] for sample in data_set]
    return applied


def pad_to(lst, length, value):
    for i in range(len(lst), length):
        lst.append(value)
    
    return lst


def uprint(x):
    print(repr(x).decode('unicode-escape'), end=' ')


def uprintln(x):
    print(repr(x).decode('unicode-escape'))


def is_CN_char(ch):
    return ch >= '\u4e00' and ch <= '\u9fa5'


def split_sentences(line):
    sentences = []
    i = 0
    for j in range(len(line)+1):
        if j == len(line) or line[j] in ['，', '。', '！', '？', '、']:
            if i < j:
                sentence = ''.join(filter(is_CN_char, line[i:j]))
                sentences.append(sentence)
            i = j+1
    return sentences

