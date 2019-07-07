#%%
# Dependencies
import datetime as dt
import pandas as pd
from pymongo import *
from mongoengine import *

#%%

connect('moo', host='localhost', port=27017)
