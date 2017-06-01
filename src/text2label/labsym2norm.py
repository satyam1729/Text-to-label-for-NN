#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:49:21 2017

@author: satyam
converts the hts symboled labels to normalized binary
"""
import os
from os import listdir
from os.path import isfile, join

from label_normalisation import HTSLabelNormalisation
from silence_remover import SilenceRemover

from min_max_norm import MinMaxNormalisation

# the new class for label composition and normalisation

label_normaliser = HTSLabelNormalisation(question_file_name='/home/satyam/code/summer-2017/TTS/data/HTS-demo_CMU-ARCTIC-SLT/data/questions/questions_qst001.hed', add_frame_features=False, subphone_feats='none')
#add_feat_dim = sum(cfg.additional_features.values())
#lab_dim = label_normaliser.dimension + add_feat_dim + cfg.appended_input_dim
#logger.info('Input label dimension is %d' % lab_dim)
#suffix=str(lab_dim)
lab_dim=label_normaliser.dimension

in_label_align_file_list=[]
binary_label_file_list=[]
nn_label_file_list=[]
nn_label_norm_file_list=[]
prompt_label_path='/home/satyam/code/summer-2017/TTS/data/HTS-demo_CMU-ARCTIC-SLT/data/prompt-labels'
binary_label_path='/home/satyam/code/summer-2017/TTS/data/HTS-demo_CMU-ARCTIC-SLT/data/binary-labels'
nn_label_path='/home/satyam/code/summer-2017/TTS/data/HTS-demo_CMU-ARCTIC-SLT/data/nn-labels'
nn_label_norm_path='/home/satyam/code/summer-2017/TTS/data/HTS-demo_CMU-ARCTIC-SLT/data/nn-labels-norm'
#os.mkdir(binary_label_path)
#os.mkdir(nn_label_path)
#os.mkdir(nn_label_norm_path)
for f in listdir(prompt_label_path):
    if isfile(join(prompt_label_path,f)):
        in_label_align_file_list.append(join(prompt_label_path,f))
        binary_label_file_list.append(join(binary_label_path,f))
        nn_label_file_list.append(join(nn_label_path,f))
        nn_label_norm_file_list.append(join(nn_label_norm_path,f))
        
#print in_label_align_file_list
#print binary_label_file_list
#print nn_label_file_list
#print nn_label_norm_file_list


label_normaliser.perform_normalisation(in_label_align_file_list, binary_label_file_list, label_type="state_align")
remover = SilenceRemover(n_cmp = lab_dim, silence_pattern = ['*-sil+*'  ], label_type="state_align", remove_frame_features = True, subphone_feats = 'none') 
remover.remove_silence(binary_label_file_list, in_label_align_file_list, nn_label_file_list)
min_max_normaliser = MinMaxNormalisation(feature_dimension = lab_dim, min_value = 0.01, max_value = 0.99)
