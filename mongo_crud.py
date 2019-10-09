# # To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import pandas as pd
from datetime import datetime, date
from pymongo import *
from mongoengine import *

# from config import database, username, password, authentication_source, replicaset, host, port

# Connect to database with MongoEngine

# connect(database, username=username, password=password, authentication_source=authentication_source, replicaset=replicaset, host=host, port=port)
connect('cow')

#%%
system2016 = pd.read_csv('Resources/system2016.csv')
system2016.head()

#%%
class System2016(Document):
    _id = IntField(required=True)
    stateabb = StringField(required=True)
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
states2016 = pd.read_csv('Resources/states2016.csv')
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
    startDate = str(styear) + '-' + str(stmonth) + '-' + str(stday)
    endDate = str(endyear) + '-' + str(endmonth) + '-' + str(endday)
    startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date() 
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
majors2016 = pd.read_csv('Resources/majors2016.csv')
majors2016.head()
#%%
class Majors2016(Document):
    _id = IntField(required=True)
    stateabb = StringField(required=True)
    ccode = IntField(required=True)
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

for i in range(len(majors2016)):
    styear = majors2016['styear'][i]
    stmonth = majors2016['stmonth'][i]
    stday = majors2016['stday'][i]
    endyear = majors2016['endyear'][i]
    endmonth = majors2016['endmonth'][i]
    endday = majors2016['endday'][i]
    startDate = str(styear) + '-' + str(stmonth) + '-' + str(stday)
    endDate = str(endyear) + '-' + str(endmonth) + '-' + str(endday)
    startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date() 
    post = Majors2016(
        _id = i,
        stateabb = majors2016['stateabb'][i],
        ccode = majors2016['ccode'][i],
        styear = styear,
        stmonth = stmonth,
        stday = stday,
        endyear = endyear,
        endmonth = endmonth,
        endday = endday,
        startDate = startDate,
        endDate = endDate,
        version = majors2016['version'][i]
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
midloca = pd.read_csv('Resources/midloc2.0/MIDLOCA_2.0.csv', encoding='ISO-8859-1')
midloca.head()

# #%%
# columns = midloca.columns.tolist()
# for column in columns:
#     print(column) # + ' = ' + 'Field()')
# if len(midloca['dispnum']) == len(midloca['dispnum'].unique()): print("All values are unique.")
#midloca.head()

#%%
class MIDLOCA(Document):
    year = IntField()
    dispnum = IntField(required=True, primary_key=True)
    midloc2_location = StringField()
    midloc2_measuringpoint = StringField()
    midloc2_xlongitude = FloatField()
    midloc2_ylatitude = FloatField()
    midloc2_coordinates = GeoPointField()
    midloc2_precision = IntField()
    midloc2_howobtained = StringField()
    midloc2_precision_comment = StringField()
    midloc2_general_comment = StringField()
    priogrid_cell = IntField()
    midloc11_location = StringField()
    midloc11_midlocmeasuringpoint = StringField()
    midloc11_latitude = FloatField()
    midloc11_longitude = FloatField()
    midloc11_coordinates = GeoPointField()
    midloc11_precision = IntField()
    updated = DateTimeField(required=True, default=datetime.utcnow)

#%%
for i in range(len(midloca)):
    post = MIDLOCA(
        year = int(midloca['year'][i]),
        dispnum = int(midloca['dispnum'][i]),
        midloc2_location = str(midloca['midloc2_location'][i]),
        midloc2_measuringpoint = str(midloca['midloc2_measuringpoint'][i]),
        midloc2_xlongitude = float(midloca['midloc2_xlongitude'][i]),
        midloc2_ylatitude = float(midloca['midloc2_ylatitude'][i]),
        midloc2_coordinates = [float(midloca['midloc2_xlongitude'][i]), float(midloca['midloc2_ylatitude'][i])],
        midloc2_precision = int(midloca['midloc2_precision'][i]),
        midloc2_howobtained = str(midloca['midloc2_howobtained'][i]),
        midloc2_precision_comment = str(midloca['midloc2_precision_comment'][i]),
        midloc2_general_comment = str(midloca['midloc2_general_comment'][i]),
        priogrid_cell = midloca['priogrid_cell'][i],
        midloc11_location = str(midloca['midloc11_location'][i]),
        midloc11_midlocmeasuringpoint = str(midloca['midloc11_midlocmeasuringpoint'][i]),
        midloc11_latitude = float(midloca['midloc11_latitude'][i]),
        midloc11_longitude = float(midloca['midloc11_longitude'][i]),
        midloc11_coordinates = [float(midloca['midloc11_longitude'][i]), float(midloca['midloc11_latitude'][i])],
        midloc11_precision = midloca['midloc11_precision'][i]
    )
    try:
        post.save()
    except:
        failures += 1
        pass
print("Only " + str(failures) + " documents failed to post!")

#%%
for i in range(len(midloca)):
    post = MIDLOCA(
        year = midloca['year'][i],
        dispnum = midloca['dispnum'][i],
        midloc2_location = midloca['midloc2_location'][i],
        midloc2_measuringpoint = midloca['midloc2_measuringpoint'][i],
        midloc2_xlongitude = midloca['midloc2_xlongitude'][i],
        midloc2_ylatitude = midloca['midloc2_ylatitude'][i],
        midloc2_coordinates = [midloca['midloc2_xlongitude'][i], midloca['midloc2_ylatitude'][i]],
        midloc2_precision = midloca['midloc2_precision'][i],
        midloc2_howobtained = midloca['midloc2_howobtained'][i],
        midloc2_precision_comment = midloca['midloc2_precision_comment'][i],
        midloc2_general_comment = midloca['midloc2_general_comment'][i],
        priogrid_cell = midloca['priogrid_cell'][i],
        midloc11_location = midloca['midloc11_location'][i],
        midloc11_midlocmeasuringpoint = midloca['midloc11_midlocmeasuringpoint'][i],
        midloc11_latitude = midloca['midloc11_latitude'][i],
        midloc11_longitude = midloca['midloc11_longitude'][i],
        midloc11_coordinates = midloca['midloc11_longitude'][i], midloca['midloc11_latitude'][i]],
        midloc11_precision = midloca['midloc11_precision'][i]
    )
    try:
        post.save()
    except:
        failures += 1
        pass
print("Only " + str(failures) + " documents failed to post!")

#%%
#%%
disconnect()

