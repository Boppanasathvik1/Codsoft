import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from collections import namedtuple
import ydata_profiling as pandas_profiling  # Use ydata_profiling instead of pandas_profiling
from IPython.display import display
#Load dataset
df = pd.read_csv('/kaggle/input/imdb-india-movies/IMDb Movies India.csv', encoding='latin1')
# Display the first few rows of the dataset
df.head()
# Generate a Pandas Profiling Report for initial data exploration
report = pandas_profiling.ProfileReport(df)
display(report)
