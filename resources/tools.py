#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:26:47 2018

@author: thomas IceMobile
"""

import pandas as pd
import numpy as np
import os
import warnings


class Normalizer():
    """Map any data to the (consecutive) iinterval [0 to N) (integers)

    Input type can be any (string, int, float, categorial)..

    Examples:
        
    >>> user_ids=['a','c', 'x']
    >>> user_hasher= Normalizer(user_ids)
    >>> user_hasher.external_to_internal('c')
    1

    >>> user_hasher.external_to_internal(user_hasher.internal_to_external(1))
    1

    >>> list(user_hasher.internal_to_external([1,2]))
    ['c', 'x']

    Args:
        i: ..
        key:
        keys: ..

    Returns:
        mapped output
    """

    def __init__(self, keys):   
        self.real_keys=np.unique(keys)
        self.hash_keys=np.array(range(0,len(keys)))
        self.lookup=dict(zip(self.real_keys, self.hash_keys))

    def internal_to_external(self, i):
        return self.real_keys[i]

    def external_to_internal(self, key):
        return self.lookup[key]
    
    def external_to_internals(self, keys):
        return np.array([self.lookup[k] for k in keys])

    def apply(self,df_column):
        return df_column.apply(lambda x: self.external_to_internal(x))
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod() 

     
