#%%
# Dependencies
import datetime as dt
import pandas as pd
from pymongo import *
from mongoengine import *

# Connect to database
connect('moo', host='localhost', port=27017)

#%%
class COW_country_codes(Document):
    StateAbb = StringField(required=True)
    CCode = StringField(required=True)
    StateNme = StringField(required=True)
    timestamp = DateTimeField(default=dt.datetime.now)

countryCodes = pd.read_csv("COW country codes.csv")

for i in range(len(countryCodes)):
    post = CountryCodes(
    StateAbb = str(countryCodes['StateAbb'][i]),
    CCode = str(countryCodes['CCode'][i]),
    StateNme = str(countryCodes['StateNme'][i])
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + i)

#%%
MIDA_4_3 = pd.read_csv("MID 4.3/MIDA 4.3.csv")
# columns = MIDA_4_3.columns.to_list()
# print(columns)
# for column in columns:
#   print(column + ' = str(MIDA_4_3[\'' + column + '\'][i]),')
# for column in columns:
#     print(column + ' = str(MIDA_4_3.' + column + '[i]),')

# for column in columns:
#    print(column + ' = StringField')
#%%
class MIDA(Document):
    dispnum3 = StringField()
    dispnum4 = StringField()
    stday = StringField()
    stmon = StringField()
    styear = StringField()
    endday = StringField()
    endmon = StringField()
    endyear = StringField()
    outcome = StringField()
    settle = StringField()
    fatality = StringField()
    fatalpre = StringField()
    maxdur = StringField()
    mindur = StringField()
    hiact = StringField()
    hostlev = StringField()
    recip = StringField()
    numa = StringField()
    numb = StringField()
    link1 = StringField()
    link2 = StringField()
    link3 = StringField()
    ongo2010 = StringField()
    version = StringField()
    timestamp = DateTimeField(default=dt.datetime.now)

for i in range(len(MIDA_4_3)):
    post = MIDA(
        dispnum3 = str(MIDA_4_3.dispnum3[i]),
        dispnum4 = str(MIDA_4_3.dispnum4[i]),
        stday = str(MIDA_4_3.stday[i]),
        stmon = str(MIDA_4_3.stmon[i]),
        styear = str(MIDA_4_3.styear[i]),
        endday = str(MIDA_4_3.endday[i]),
        endmon = str(MIDA_4_3.endmon[i]),
        endyear = str(MIDA_4_3.endyear[i]),
        outcome = str(MIDA_4_3.outcome[i]),
        settle = str(MIDA_4_3.settle[i]),
        fatality = str(MIDA_4_3.fatality[i]),
        fatalpre = str(MIDA_4_3.fatalpre[i]),
        maxdur = str(MIDA_4_3.maxdur[i]),
        mindur = str(MIDA_4_3.mindur[i]),
        hiact = str(MIDA_4_3.hiact[i]),
        hostlev = str(MIDA_4_3.hostlev[i]),
        recip = str(MIDA_4_3.recip[i]),
        numa = str(MIDA_4_3.numa[i]),
        numb = str(MIDA_4_3.numb[i]),
        link1 = str(MIDA_4_3.link1[i]),
        link2 = str(MIDA_4_3.link2[i]),
        link3 = str(MIDA_4_3.link3[i]),
        ongo2010 = str(MIDA_4_3.ongo2010[i]),
        version = str(MIDA_4_3.version[i]),
        timestamp = dt.datetime.now
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + i)
#%%
MIDB = pd.read_csv("MID 4.3/MIDB 4.3.csv")
MIDB.head()

MIDI = pd.read_csv("MID 4.3/MIDI 4.3.csv")
MIDI.head()

MIDP = pd.read_csv("MID 4.3/MIDP 4.3.csv")
MIDP.head()


#%%
# client = MongoClient('localhost', 27017)
# db = client.moo

MIDA_4_3.head()


#%%
MIDA_4_3.dispnum3[0]

#%%
