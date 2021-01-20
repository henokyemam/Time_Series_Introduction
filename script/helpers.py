#Modules 
from __future__ import absolute_import, division, print_function, unicode_literals
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import os
import sys
from datetime import datetime
import pandas as pd
from download import download

import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go
# Set notebook mode to work in offline
pyo.init_notebook_mode()
from statsmodels.graphics.tsaplots import plot_acf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False


#helper functions
def convert_to_date(x):
    return datetime.strptime(x, '%Y %m %d %H')

def parse(x):
    return datetime.strptime(x, '%m/%d/%Y')
