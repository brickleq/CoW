# # To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import datetime as dt
import pandas as pd
from datetime import datetime
from pymongo import *
from mongoengine import *

from config import database, username, password, authentication_source, replicaset, host, port

# Connect to database with MongoEngine
disconnect()
# connect(database, username=username, password=password, authentication_source=authentication_source, replicaset=replicaset, host=host, port=port)
connect('cow-local')


#%%
class country_codes(Document):
    _id = IntField(required=True)
    _StateAbb = StringField(required=True)
    _CCode = IntField(required=True)
    StateNme = StringField(required=True)
    updated = DateTimeField(default=datetime.utcnow)
#%%
countryCodes = pd.read_csv("/Users/pbl/Repos/CoW/Resources/COW country codes.csv")
countryCodes.head()

#%%
for i in range(len(countryCodes)):
    post = country_codes(
    _id = i,
    _StateAbb = str(countryCodes['StateAbb'][i]),
    _CCode = str(countryCodes['CCode'][i]),
    StateNme = str(countryCodes['StateNme'][i])
    )
    try:
        post.save()
        print('Success posting record ' + str(i))
    except: 
        print('ERROR posting document ' + str(i))

#%%
system2016 = pd.read_csv('/Users/pbl/Repos/CoW/Resources/system2016.csv')
system2016.head()
#%%
len(system2016['ccode'].unique())
#%%
class System2016(Document):
    _id = IntField(required=True)
    stateabb = ReferenceField(country_codes, required=True)
    ccode = IntField(required=True)
    year = IntField(required=True)
    version = IntField(required=True)
    updated = DateTimeField(default=datetime.utcnow)

for i in range(len(system2016)):
    year = str(system2016['year'][i])
    post = System2016(
        _id = i,
        stateabb = system2016['stateabb'][i],
        ccode = system2016['ccode'][i],
        year = year,
        version = system2016['version'][i]
    )
    try:
        post.save()
        print('Success posting document ' + str(i))
    except: 
        print('ERROR posting document ' + str(i))
#%%
states2016 = pd.read_csv('/Users/pbl/Repos/CoW/Resources/states2016.csv')
states2016.head()

#%%
class States2016(Document):
    _id = IntField(required=True)
    stateabb = StringField(required=True)
    ccode = IntField(required=True)
    statenme = StringField(required=False)
    styear = IntField(required=True)
    stmonth = IntField(required=False)
    stday = IntField(required=False)
    endyear = IntField(required=True)
    endmonth = IntField(required=False)
    endday = IntField(required=False)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    version = IntField(required=True)
    updated = DateTimeField(default=datetime.utcnow)

#%%
for i in range(len(states2016)):
    styear = states2016['styear'][i]
    stmonth = states2016['stmonth'][i]
    stday = states2016['stday'][i]
    endyear = states2016['endyear'][i]
    endmonth = states2016['endmonth'][i]
    endday = states2016['endday'][i]
    #startDate = datetime.strptime((str(styear) + '-' + str(stmonth) + '-' + str(stday)), '%Y/%m/%d')
    startDate = str(styear) + '-' + str(stmonth) + '-' + str(stday)
    endDate = str(endyear) + '-' + str(endmonth) + '-' + str(endday)
    startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    #print(startDate,endDate) 
    post = States2016(
        _id = i,
        stateabb = states2016['stateabb'][i],
        ccode = states2016['ccode'][i],
        statenme = states2016['statenme'][i],
        styear = styear,
        stmonth = stmonth,
        stday = stday,
        endyear = endyear,
        endmonth = endmonth,
        endday = endday,
        startDate = startDate,
        endDate = endDate,
        version = states2016['version'][i]
        )
    try:
        post.save()
        print('Success posting document ' + str(i))
    except: 
        print('ERROR posting document ' + str(i))

#%%
outcome = {
    1:'Victory for side A', 
    2:'Victory for side B',
    3:'Yield by side A',
    4:'Yield by side B',
    5:'Stalemate',
    6:'Compromise',
    7:'Released',
    8:'Unclear',
    9:'Joins ongoing war',
    -9:'Missing'}

class Outcome(EmbeddedDocument):
    _id = IntField()
    outcome = StringField()


#%%
# Settlement of dispute
settle = {
    1:'Negotiated',
    2:'Imposed',
    3:'None',
    4:'Unclear',
    -9:'Missing'}

class Settle(EmbeddedDocument):
    _id = IntField()
    settle = StringField()


#%%
# Fatality level of dispute
fatality = {
    0:{'Fatality level of dispute':'None','min':0,'max':0},
    1:{'Fatality level of dispute':'1-25 deaths','min':1,'max':25},
    2:{'Fatality level of dispute':'26-100 deaths','min':26,'max':100},
    3:{'Fatality level of dispute':'101-250 deaths','min':101,'max':250},
    4:{'Fatality level of dispute':'251-500 deaths','min':251,'max':500},
    5:{'Fatality level of dispute':'501-999 deaths','min':501,'max':999},
    6:{'Fatality level of dispute':'>999 deaths','min':1000,'max':float('inf')},
    9:{'Fatality level of dispute':'Missing','min':0,'max':float('inf')}
}
class Fatality(EmbeddedDocument):
    _id = IntField()
    fatality = StringField()
    max = IntField()
    min = IntField()

#%%

# HiAct
# Highest action in dispute [bracketed numbers refer to corresponding hostility level]:
hiact = {
    0:{'Highest action in dispute':'No militarized action','Hostility level':1},
    1:{'Highest action in dispute':'Threat to use force','Hostility level':2},
    2:{'Highest action in dispute':'Threat to blockade','Hostility level':2},
    3:{'Highest action in dispute':'Threat to occupy territory','Hostility level':2},
    4:{'Highest action in dispute':'Threat to declare war','Hostility level':2},
    5:{'Highest action in dispute':'Threat to use CBR weapons','Hostility level':2},
    6:{'Highest action in dispute':'Threat to join war','Hostility level':2}, # double check hostility level--missing in code book
    7:{'Highest action in dispute':'Show of force','Hostility level':3},
    8:{'Highest action in dispute':'Alert','Hostility level':3},
    9:{'Highest action in dispute':'Nuclear alert','Hostility level':3},
    10:{'Highest action in dispute':'Mobilization','Hostility level':3},
    11:{'Highest action in dispute':'Fortify border','Hostility level':3},
    12:{'Highest action in dispute':'Border violation','Hostility level':3},
    13:{'Highest action in dispute':'Blockade','Hostility level':4},
    14:{'Highest action in dispute':'Occupation of territory','Hostility level':4},
    15:{'Highest action in dispute':'Seizure','Hostility level':4},
    16:{'Highest action in dispute':'Attack','Hostility level':4},
    17:{'Highest action in dispute':'Clash','Hostility level':4},
    18:{'Highest action in dispute':'Declaration of war','Hostility level':4},
    19:{'Highest action in dispute':'Use of CBR weapons','Hostility level':4},
    20:{'Highest action in dispute':'Begin interstate war','Hostility level':5},
    21:{'Highest action in dispute':'Join interstate war','Hostility level':5},
    -9:{'Highest action in dispute':'Missing','Hostility level':-9}
}

class HiAct(EmbeddedDocument):
    _id = IntField()
    hiact = StringField()
    hostlev = IntField()

#%%
hostlev = {
    1:'No militarized action',
    2:'Threat to use force',
    3:'Display of force',
    4:'Use of force',
    5:'War'
}

class HostLev(EmbeddedDocument):
    _id = IntField()
    hostlev = StringField()



#%%
Ongo2010 = {
    0:'concluded before 6/30/2010',
    1:'continuing as of 6/30/2010'
}

class Ongo2010(EmbeddedDocument):
    _id = IntField()
    ongo2010 = StringField()

#%%
revtype1 = {
    0:'Not applicable',
    1:'Territory',
    2:'Policy',
    3:'Regime/government',
    4:'Other',
    -9:'Missing'
}

class RevType1(EmbeddedDocument):
    _id = IntField()
    revtype1 = StringField()

revtype2 = {
    0:'Not applicable',
    1:'Territory',
    2:'Policy',
    3:'Regime/government',
    4:'Other',
    -9:'Missing'
}

class RevType2(EmbeddedDocument):
    _id = IntField()
    revtype2 = StringField()
    

#%%


#%%
