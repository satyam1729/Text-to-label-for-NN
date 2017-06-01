#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:49:21 2017

@author: satyam
"""

from label_normalisation import HTSLabelNormalisation
from silence_remover import SilenceRemover

from min_max_norm import MinMaxNormalisation

# the new class for label composition and normalisation

label_normaliser = HTSLabelNormalisation(question_file_name='/home/satyam/code/summer-2017/merlin/misc/questions/questions-radio_dnn_416.hed', add_frame_features=False, subphone_feats='none')
#add_feat_dim = sum(cfg.additional_features.values())
#lab_dim = label_normaliser.dimension + add_feat_dim + cfg.appended_input_dim
#logger.info('Input label dimension is %d' % lab_dim)
#suffix=str(lab_dim)
lab_dim=label_normaliser.dimension
in_label_align_file_list=[]
in_label_align_file_list.append('/home/satyam/code/summer-2017/merlin/egs/slt_arctic/s1/experiments/slt_arctic_demo/test_synthesis/prompt-lab/c.lab')
binary_label_file_list=[]
binary_label_file_list.append('/home/satyam/code/summer-2017/merlin/egs/slt_arctic/s1/experiments/slt_arctic_demo/duration_model/data/binary_label_416/c.lab')
nn_label_file_list=[]
nn_label_file_list.append('/home/satyam/code/summer-2017/merlin/egs/slt_arctic/s1/experiments/slt_arctic_demo/duration_model/data/nn_no_silence_lab_416/c.lab')
nn_label_norm_file_list=[]
nn_label_norm_file_list.append('/home/satyam/code/summer-2017/merlin/egs/slt_arctic/s1/experiments/slt_arctic_demo/duration_model/data/nn_no_silence_lab_norm_416/c.lab')
label_normaliser.perform_normalisation(in_label_align_file_list, binary_label_file_list, label_type="state_align")
remover = SilenceRemover(n_cmp = lab_dim, silence_pattern = ['*-sil+*'  ], label_type="state_align", remove_frame_features = True, subphone_feats = 'none')
remover.remove_silence(binary_label_file_list, in_label_align_file_list, nn_label_file_list)
min_max_normaliser = MinMaxNormalisation(feature_dimension = lab_dim, min_value = 0.01, max_value = 0.99)
