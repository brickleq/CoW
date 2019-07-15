#%%
# Dependencies
import datetime as dt
import pandas as pd
from pymongo import *
from mongoengine import *

# Connect to database
connect('moo', host='localhost', port=27017)

#%%
class country_codes(Document):
    StateAbb = StringField(required=True)
    CCode = IntField(required=True)
    StateNme = StringField(required=True)
    updated = DateTimeField(default=dt.datetime.utcnow)

countryCodes = pd.read_csv("COW country codes.csv")

for i in range(len(countryCodes)):
    post = country_codes(
    StateAbb = str(countryCodes['StateAbb'][i]),
    CCode = str(countryCodes['CCode'][i]),
    StateNme = str(countryCodes['StateNme'][i])
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + i)
#%%
#%%
midloca_2_0 = pd.read_csv('midloc2.0/MIDLOCA_2.0.csv', encoding='ISO-8859-1')
midloca_2_0.head()
columns = midloca_2_0.columns.to_list()
# print(columns)
# for column in columns:
#    print(column + ' = IntField()')
# for column in columns:
#     print(column + ' = int(midloca_2_0[\'' + column + '\'][i]),')

class midloc_a(Document):
    _id = IntField(required=True)
    year = IntField(required=True)
    dispnum = IntField(required=True)
    location = StringField(required=False)
    measuringpoint = StringField(required=False, default='')
    longitude = FloatField(required=False, default='')
    latitude = FloatField(required=False)
    coordinates = PointField(required=False)
    precision = IntField(required=True)
    howobtained = StringField(required=False)
    precision_comment = StringField(required=False)
    general_comment = StringField(required=False)
    priogrid_cell = FloatField(required=False)
    midloc11_location = StringField(required=False)
    midloc11_midlocmeasuringpoint = StringField(required=False)
    midloc11_latitude = FloatField(required=False)
    midloc11_longitude = FloatField(required=False)
    midloc11_precision = IntField(required=False)
    updated = DateTimeField(required=True, default=dt.datetime.utcnow)
    meta = {'strict': False}

for i in range(len(midloca_2_0)):
    if midloca_2_0['midloc2_precision'][i] == -99:
        post = midloc_a(
            _id = int(midloca_2_0['dispnum'][i]),
            year = int(midloca_2_0['year'][i]),
            dispnum = int(midloca_2_0['dispnum'][i]),
            # location = str(midloca_2_0['midloc2_location'][i]),
            # measuringpoint = str(midloca_2_0['midloc2_measuringpoint'][i]),
            # longitude = float(midloca_2_0['midloc2_xlongitude'][i]),
            # latitude = float(midloca_2_0['midloc2_ylatitude'][i]),
            # coordinates = [midloca_2_0['midloc2_xlongitude'][i], midloca_2_0['midloc2_ylatitude'][i]],
            precision = int(midloca_2_0['midloc2_precision'][i]),
            # howobtained = str(midloca_2_0['midloc2_howobtained'][i]),
            # precision_comment = str(midloca_2_0['midloc2_precision_comment'][i]),
            # general_comment = str(midloca_2_0['midloc2_general_comment'][i]),
            # priogrid_cell = midloca_2_0['priogrid_cell'][i],
            # midloc11_location = str(midloca_2_0['midloc11_location'][i]),
            # midloc11_midlocmeasuringpoint = str(midloca_2_0['midloc11_midlocmeasuringpoint'][i]),
            # midloc11_latitude = float(midloca_2_0['midloc11_latitude'][i]),
            # midloc11_longitude = float(midloca_2_0['midloc11_longitude'][i]),
            # midloc11_precision = float(midloca_2_0['midloc11_precision'][i]),
    )
    else:
        post = midloc_a(
            _id = int(midloca_2_0['dispnum'][i]),
            year = int(midloca_2_0['year'][i]),
            dispnum = int(midloca_2_0['dispnum'][i]),
            location = str(midloca_2_0['midloc2_location'][i]),
            measuringpoint = str(midloca_2_0['midloc2_measuringpoint'][i]),
            longitude = float(midloca_2_0['midloc2_xlongitude'][i]),
            latitude = float(midloca_2_0['midloc2_ylatitude'][i]),
            coordinates = [midloca_2_0['midloc2_xlongitude'][i], midloca_2_0['midloc2_ylatitude'][i]],
            precision = int(midloca_2_0['midloc2_precision'][i]),
            howobtained = str(midloca_2_0['midloc2_howobtained'][i]),
            precision_comment = str(midloca_2_0['midloc2_precision_comment'][i]),
            general_comment = str(midloca_2_0['midloc2_general_comment'][i]),
            priogrid_cell = midloca_2_0['priogrid_cell'][i],
            midloc11_location = str(midloca_2_0['midloc11_location'][i]),
            midloc11_midlocmeasuringpoint = str(midloca_2_0['midloc11_midlocmeasuringpoint'][i]),
            midloc11_latitude = float(midloca_2_0['midloc11_latitude'][i]),
            midloc11_longitude = float(midloca_2_0['midloc11_longitude'][i]),
            midloc11_precision = float(midloca_2_0['midloc11_precision'][i]),
        )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + str(i))
#%%
MIDA_4_3 = pd.read_csv("MID 4.3/MIDA 4.3.csv")
# columns = MIDA_4_3.columns.to_list()
# print(columns)
# for column in columns:
#   print(column + ' = str(MIDA_4_3[\'' + column + '\'][i]),')
# for column in columns:
#     print(column + ' = str(MIDA_4_3.' + column + '[i]),')

# for column in columns:
#    print(column + ' = IntField()')
#%%
class mid_a(DynamicDocument):
    dispnum3 = IntField()
    dispnum4 = IntField()
    stday = IntField()
    stmon = IntField()
    styear = IntField()
    endday = IntField()
    endmon = IntField()
    endyear = IntField()
    outcome = IntField()
    settle = IntField()
    fatality = IntField()
    fatalpre = IntField()
    maxdur = IntField()
    mindur = IntField()
    hiact = IntField()
    hostlev = IntField()
    recip = IntField()
    numa = IntField()
    numb = IntField()
    link1 = IntField()
    link2 = IntField()
    link3 = IntField()
    ongo2010 = IntField()
    version = FloatField()
    updated = DateTimeField(required=True, default=dt.datetime.utcnow)
    meta = {'strict': False}

for i in range(len(MIDA_4_3)):
    post = mid_a(
        dispnum3 = int(MIDA_4_3.dispnum3[i]),
        dispnum4 = int(MIDA_4_3.dispnum4[i]),
        stday = int(MIDA_4_3.stday[i]),
        stmon = int(MIDA_4_3.stmon[i]),
        styear = int(MIDA_4_3.styear[i]),
        endday = int(MIDA_4_3.endday[i]),
        endmon = int(MIDA_4_3.endmon[i]),
        endyear = int(MIDA_4_3.endyear[i]),
        outcome = int(MIDA_4_3.outcome[i]),
        settle = int(MIDA_4_3.settle[i]),
        fatality = int(MIDA_4_3.fatality[i]),
        fatalpre = int(MIDA_4_3.fatalpre[i]),
        maxdur = int(MIDA_4_3.maxdur[i]),
        mindur = int(MIDA_4_3.mindur[i]),
        hiact = int(MIDA_4_3.hiact[i]),
        hostlev = int(MIDA_4_3.hostlev[i]),
        recip = int(MIDA_4_3.recip[i]),
        numa = int(MIDA_4_3.numa[i]),
        numb = int(MIDA_4_3.numb[i]),
        link1 = str(MIDA_4_3.link1[i]),
        link2 = str(MIDA_4_3.link2[i]),
        link3 = str(MIDA_4_3.link3[i]),
        ongo2010 = int(MIDA_4_3.ongo2010[i]),
        version = float(MIDA_4_3.version[i]),
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + str(i))
#%%
MIDB_4_3 = pd.read_csv("MID 4.3/MIDB 4.3.csv")
MIDB_4_3.head()
columns = MIDB_4_3.columns.to_list()
print(columns) # ['dispnum3', 'dispnum4', 'stabb', 'ccode', 'stday', 'stmon', 'styear', 'endday', 'endmon', 'endyear', 'sidea', 'revstate', 'revtype1', 'revtype2', 'fatality', 'fatalpre', 'hiact', 'hostlev', 'orig', 'version']

for column in columns:
    print(column + ' = int(MIDB_4_3[\'' + column + '\'][i]),')
for column in columns:
   print(column + ' = IntField()')

#%%
class MIDB(Document):
    dispnum3 = IntField()
    dispnum4 = IntField()
    stabb = StringField()
    ccode = IntField()
    stday = IntField()
    stmon = IntField()
    styear = IntField()
    endday = IntField()
    endmon = IntField()
    endyear = IntField()
    sidea = IntField()
    revstate = IntField()
    revtype1 = IntField()
    revtype2 = IntField()
    fatality = IntField()
    fatalpre = IntField()
    hiact = IntField()
    hostlev = IntField()
    orig = IntField()
    version = StringField()
    datetime = DateTimeField(default=dt.datetime.now)
    meta = {'strict': False}

for i in range(len(MIDB_4_3)):
    post = MIDB(
        dispnum3 = int(MIDB_4_3['dispnum3'][i]),
        dispnum4 = int(MIDB_4_3['dispnum4'][i]),
        stabb = str(MIDB_4_3['stabb'][i]),
        ccode = int(MIDB_4_3['ccode'][i]),
        stday = int(MIDB_4_3['stday'][i]),
        stmon = int(MIDB_4_3['stmon'][i]),
        styear = int(MIDB_4_3['styear'][i]),
        endday = int(MIDB_4_3['endday'][i]),
        endmon = int(MIDB_4_3['endmon'][i]),
        endyear = int(MIDB_4_3['endyear'][i]),
        sidea = int(MIDB_4_3['sidea'][i]),
        revstate = int(MIDB_4_3['revstate'][i]),
        revtype1 = int(MIDB_4_3['revtype1'][i]),
        revtype2 = int(MIDB_4_3['revtype2'][i]),
        fatality = int(MIDB_4_3['fatality'][i]),
        fatalpre = int(MIDB_4_3['fatalpre'][i]),
        hiact = int(MIDB_4_3['hiact'][i]),
        hostlev = int(MIDB_4_3['hostlev'][i]),
        orig = int(MIDB_4_3['orig'][i]),
        version = str(MIDB_4_3['version'][i]),
        datetime = dt.datetime.now
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + str(i))
#%%
MIDI_4_3 = pd.read_csv("MID 4.3/MIDI 4.3.csv")
# MIDI_4_3.head()
# columns = MIDI_4_3.columns.to_list()
# print(columns)

# for column in columns:
#     print(column + ' = int(MIDB_4_3[\'' + column + '\'][i]),')
# for column in columns:
#    print(column + ' = IntField()')
class MIDI(Document):
    dispnum3 = IntField()
    incidnum3 = IntField()
    dispnum4 = IntField()
    incidnum4 = IntField()
    stday = IntField()
    stmon = IntField()
    styear = IntField()
    endday = IntField()
    endmon = IntField()
    endyear = IntField()
    duration = IntField()
    tbi = IntField()
    fatality = IntField()
    fatalpre = IntField()
    action = IntField()
    hostlev = IntField()
    numa = IntField()
    revtype1 = IntField()
    revtype2 = IntField()
    version = StringField()
    datetime = DateTimeField(default=dt.datetime.utcnow)
    meta = {'strict': False}

for i in range(len(MIDI_4_3)):
    post = MIDI(
        dispnum3 = int(MIDI_4_3['dispnum3'][i]),
        incidnum3 = int(MIDI_4_3['incidnum3'][i]),
        dispnum4 = int(MIDI_4_3['dispnum4'][i]),
        incidnum4 = int(MIDI_4_3['incidnum4'][i]),
        stday = int(MIDI_4_3['stday'][i]),
        stmon = int(MIDI_4_3['stmon'][i]),
        styear = int(MIDI_4_3['styear'][i]),
        endday = int(MIDI_4_3['endday'][i]),
        endmon = int(MIDI_4_3['endmon'][i]),
        endyear = int(MIDI_4_3['endyear'][i]),
        duration = int(MIDI_4_3['duration'][i]),
        tbi = int(MIDI_4_3['tbi'][i]),
        fatality = int(MIDI_4_3['fatality'][i]),
        fatalpre = int(MIDI_4_3['fatalpre'][i]),
        action = int(MIDI_4_3['action'][i]),
        hostlev = int(MIDI_4_3['hostlev'][i]),
        numa = int(MIDI_4_3['numa'][i]),
        revtype1 = int(MIDI_4_3['revtype1'][i]),
        revtype2 = int(MIDI_4_3['revtype2'][i]),
        version = str(MIDI_4_3['version'][i]),
        datetime = dt.datetime.utcnow
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + str(i))
#%%
MIDP_4_3 = pd.read_csv("MID 4.3/MIDP 4.3.csv")
MIDP_4_3.head()
columns = MIDP_4_3.columns.to_list()
print(columns)
for column in columns:
   print(column + ' = IntField()')
for column in columns:
    print(column + ' = int(MIDP_4_3[\'' + column + '\'][i]),')
class MIDP(Document):
    dispnum3 = IntField()
    incidnum3 = IntField()
    dispnum4 = IntField()
    incidnum4 = IntField()
    stabb = StringField()
    ccode = IntField()
    stday = IntField()
    stmon = IntField()
    styear = IntField()
    endday = IntField()
    endmon = IntField()
    endyear = IntField()
    insidea = IntField()
    sidea = IntField()
    fatality = IntField()
    fatalpre = IntField()
    action = IntField()
    hostlev = IntField()
    revtype1 = IntField()
    revtype2 = IntField()
    version = StringField()
    datetime = DateTimeField(default=dt.datetime.utcnow)
    meta = {'strict': False}

for i in range(len(MIDP_4_3)):
    post = MIDP(
        dispnum3 = int(MIDP_4_3['dispnum3'][i]),
        incidnum3 = int(MIDP_4_3['incidnum3'][i]),
        dispnum4 = int(MIDP_4_3['dispnum4'][i]),
        incidnum4 = int(MIDP_4_3['incidnum4'][i]),
        stabb = str(MIDP_4_3['stabb'][i]),
        ccode = int(MIDP_4_3['ccode'][i]),
        stday = int(MIDP_4_3['stday'][i]),
        stmon = int(MIDP_4_3['stmon'][i]),
        styear = int(MIDP_4_3['styear'][i]),
        endday = int(MIDP_4_3['endday'][i]),
        endmon = int(MIDP_4_3['endmon'][i]),
        endyear = int(MIDP_4_3['endyear'][i]),
        insidea = int(MIDP_4_3['insidea'][i]),
        sidea = int(MIDP_4_3['sidea'][i]),
        fatality = int(MIDP_4_3['fatality'][i]),
        fatalpre = int(MIDP_4_3['fatalpre'][i]),
        action = int(MIDP_4_3['action'][i]),
        hostlev = int(MIDP_4_3['hostlev'][i]),
        revtype1 = int(MIDP_4_3['revtype1'][i]),
        revtype2 = int(MIDP_4_3['revtype2'][i]),
        version = str(MIDP_4_3['version'][i]),
        datetime = dt.datetime.utcnow
    )
    try:
        post.save()
    except:
        print('There was an error posting document ' + str(i))

#%%
midloci_2_0 = pd.read_csv('midloc2.0/MIDLOCI_2.0.csv', encoding='ISO-8859-1')
midloci_2_0.head()
columns = midloci_2_0.columns.to_list()
print(columns)
for column in columns:
   print(column + ' = IntField()')
for column in columns:
    print(column + ' = int(midloci_2_0[\'' + column + '\'][i]),')
class midloci(DynamicDocument):
    # year = IntField()
    dispnum = IntField()
    incidnum = IntField()
    midloc2_location = StringField()
    midloc2_measuringpoint = StringField()
    midloc2_xlongitude = FloatField()
    midloc2_ylatitude = FloatField()
    midloc2_precision = IntField()
    # onset = IntField()
    # midloc2_howobtained = StringField()
    # midloc2_precision_comment = StringField()
    # midloc2_general_comment = StringField()
    # priogrid_cell = IntField()
    # midloc11_location = StringField()
    # midloc11_midlocmeasuringpoint = StringField()
    # midloc11_latitude = FloatField()
    # midloc11_longitude = FloatField()
    # midloc11_precision = FloatField()
    datetime = DateTimeField(default=dt.datetime.utcnow)
    meta = {'strict': False}

for i in range(len(midloci_2_0)):
    post = midloci(
        year = int(midloci_2_0['year'][i]),
        dispnum = int(midloci_2_0['dispnum'][i]),
        incidnum = int(midloci_2_0['incidnum'][i]),
        midloc2_location = str(midloci_2_0['midloc2_location'][i]),
        midloc2_measuringpoint = str(midloci_2_0['midloc2_measuringpoint'][i]),
        midloc2_xlongitude = float(midloci_2_0['midloc2_xlongitude'][i]),
        midloc2_ylatitude = float(midloci_2_0['midloc2_ylatitude'][i]),
        midloc2_precision = int(midloci_2_0['midloc2_precision'][i]),
        # onset = int(midloci_2_0['onset'][i]),
        # midloc2_howobtained = str(midloci_2_0['midloc2_howobtained'][i]),
        # midloc2_precision_comment = str(midloci_2_0['midloc2_precision_comment'][i]),
        # midloc2_general_comment = str(midloci_2_0['midloc2_general_comment'][i]),
        # priogrid_cell = str(midloci_2_0['priogrid_cell'][i]),
        # midloc11_location = str(midloci_2_0['midloc11_location'][i]),
        # midloc11_midlocmeasuringpoint = str(midloci_2_0['midloc11_midlocmeasuringpoint'][i]),
        # midloc11_latitude = float(midloci_2_0['midloc11_latitude'][i]),
        # midloc11_longitude = float(midloci_2_0['midloc11_longitude'][i]),
        # midloc11_precision = float(midloci_2_0['midloc11_precision'][i]),
        datetime = dt.datetime.utcnow
    )
    try:
        post.save()
    except:
        print('There was an error posting document ' + str(i))
#%%
Interstate_War_Data_4_0 = pd.read_csv('Inter-StateWarData_v4.0.csv')
Interstate_War_Data_4_0.head()

columns = Interstate_War_Data_4_0.columns.to_list()
# print(columns)

# for column in columns:
#     print(column + ' = int(Interstate_War_Data_4_0[\'' + column + '\'][i]),')
# for column in columns:
#    print(column + ' = IntField()')

class InterStateWarData(DynamicDocument):
    WarNum = IntField()
    WarName = StringField()
    WarType = IntField()
    ccode = IntField()
    StateName = StringField()
    Side = IntField()
    StartMonth1 = IntField()
    StartDay1 = IntField()
    StartYear1 = IntField()
    EndMonth1 = IntField()
    EndDay1 = IntField()
    EndYear1 = IntField()
    StartMonth2 = IntField()
    StartDay2 = IntField()
    StartYear2 = IntField()
    EndMonth2 = IntField()
    EndDay2 = IntField()
    EndYear2 = IntField()
    TransFrom = IntField()
    WhereFought = IntField()
    Initiator = IntField()
    Outcome = IntField()
    TransTo = IntField()
    BatDeath = IntField()
    Version = FloatField()
    datetime = DateTimeField(default=dt.datetime.utcnow)
    meta = {'strict': False}

for i in range(len(Interstate_War_Data_4_0)):
    post = InterStateWarData(
        WarNum = int(Interstate_War_Data_4_0['WarNum'][i]),
        WarName = str(Interstate_War_Data_4_0['WarName'][i]),
        WarType = int(Interstate_War_Data_4_0['WarType'][i]),
        ccode = int(Interstate_War_Data_4_0['ccode'][i]),
        StateName = str(Interstate_War_Data_4_0['StateName'][i]),
        Side = int(Interstate_War_Data_4_0['Side'][i]),
        StartMonth1 = int(Interstate_War_Data_4_0['StartMonth1'][i]),
        StartDay1 = int(Interstate_War_Data_4_0['StartDay1'][i]),
        StartYear1 = int(Interstate_War_Data_4_0['StartYear1'][i]),
        EndMonth1 = int(Interstate_War_Data_4_0['EndMonth1'][i]),
        EndDay1 = int(Interstate_War_Data_4_0['EndDay1'][i]),
        EndYear1 = int(Interstate_War_Data_4_0['EndYear1'][i]),
        StartMonth2 = int(Interstate_War_Data_4_0['StartMonth2'][i]),
        StartDay2 = int(Interstate_War_Data_4_0['StartDay2'][i]),
        StartYear2 = int(Interstate_War_Data_4_0['StartYear2'][i]),
        EndMonth2 = int(Interstate_War_Data_4_0['EndMonth2'][i]),
        EndDay2 = int(Interstate_War_Data_4_0['EndDay2'][i]),
        EndYear2 = int(Interstate_War_Data_4_0['EndYear2'][i]),
        TransFrom = Interstate_War_Data_4_0['TransFrom'][i],
        WhereFought = int(Interstate_War_Data_4_0['WhereFought'][i]),
        Initiator = int(Interstate_War_Data_4_0['Initiator'][i]),
        Outcome = int(Interstate_War_Data_4_0['Outcome'][i]),
        TransTo = int(Interstate_War_Data_4_0['TransTo'][i]),
        BatDeath = int(Interstate_War_Data_4_0['BatDeath'][i]),
        Version = float(Interstate_War_Data_4_0['Version'][i]),
        datetime = dt.datetime.utcnow
    )
    try:
        post.save()
    except: 
        print('There was an error posting document ' + str(i))

    
#%%
