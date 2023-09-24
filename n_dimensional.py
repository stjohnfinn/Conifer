#!/usr/bin/env python

import numpy as np
import pandas as pd

#
# LOAD DATA
#

DATA_DIR = 'data'
DATA_FILE = 'neo_v2.csv'
DATA_FILEPATH = f'{DATA_DIR}/{DATA_FILE}'

data = pd.read_csv(DATA_FILEPATH, header=0)