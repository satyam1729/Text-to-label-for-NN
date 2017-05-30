#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:06:46 2017

@author: satyam
"""

import theano
import theano.tensor as T
import numpy as np

class LPC_synthesis(object):
    '''the function realized here is x[i]=param[0]*x[i-param.shape[0]]
    '''
    def __init__(self,res,par):
        self.residue=res
        self.param=par
        self.x=T.zeros(self.residue.shape[0]+self.param.shape[0])
        for i in range(self.param.shape[0],self.residue.shape[0]+self.param.shape[0]):
            self.x=T.set_subtensor(self.x[i],T.dot(self.param[::-1],self.x[i-self.param.shape[0]:i])+self.residue[i-self.param.shape[0]])

p=np.arange(4, dtype=theano.config.floatX)
r=np.arange(10, dtype=theano.config.floatX)
synthesizer=LPC_synthesis(r,p)

f=theano.function([],synthesizer.x)
print(f())