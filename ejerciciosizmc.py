# -*- coding: utf-8 -*-
"""EjerciciosIZMC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CUlm_4ZOh4SPkr7J_cGT5XbTGj0wWDcf
"""

from google.colab import files

import pandas as pd
import io
import numpy as np

uploaded = files.upload()

uploaded

dataframe = pd.read_csv(io.StringIO(uploaded['Evidencia2 - Inventario (3).csv'].decode('latin-1')))

dataframe

dataframe.info()

dataframe.size

dataframe.index

dataframe.dtypes