import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series


consumer_complaints =  pd.read_csv('complaints_dec_2014.csv')

print(consumer_complaints.head())
