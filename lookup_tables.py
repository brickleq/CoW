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

# Settlement of dispute
settle = {
    1:'Negotiated',
    2:'Imposed',
    3:'None',
    4:'Unclear',
    -9:'Missing'}

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

hostlev = {
    1:'No militarized action',
    2:'Threat to use force',
    3:'Display of force',
    4:'Use of force',
    5:'War'
}

ongo2010 = {
    0:'concluded before 6/30/2010',
    1:'continuing as of 6/30/2010'
}

revtype1 = {
    0:'Not applicable',
    1:'Territory',
    2:'Policy',
    3:'Regime/government',
    4:'Other',
    -9:'Missing'
}

revtype2 = {
    0:'Not applicable',
    1:'Territory',
    2:'Policy',
    3:'Regime/government',
    4:'Other',
    -9:'Missing'
}