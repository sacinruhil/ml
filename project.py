# -*- coding: utf-8 -*-
"""project deep

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ls4Mdz4B38px1JcQoT070NePPvS5RHYT
"""

# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

print("my big b VIkash")

import csv
import requests

CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)