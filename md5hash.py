# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:44:53 2018

@author: t.andreev
"""

import hashlib
import pandas as pd

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


tel_dataframe = pd.read_excel(r"C:\Users\t.andreev\Телефоны.xlsx", header = 0)
tel_list = str(tel_dataframe[tel_dataframe.columns[0]].values.tolist())

hash_list = []

for i in range(len(tel_list)):
    hash_tel = computeMD5hash(tel_list[i])
    hash_list.append(hash_tel)

hash_seria = pd.Series(hash_list)
hash_seria.to_csv("Hash_numbers.csv", encoding='cp1251', index = False)