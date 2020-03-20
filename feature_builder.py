import json
from datetime import datetime

def format_date(day, month, year):
    if day > 0:
        date = f'{year}-{month}-{day}'
        date = datetime.strptime(date, '%Y-%m-%d')
        return date.isoformat()
    else:
        date = f'{year}-{month}'
        date = datetime.strptime(date, '%Y-%m')
        return date.isoformat()

def incident_feature(dispnum3, incidnum3, x, y, stday, stmon, styear, endday, endmon, endyear): #duration, fatality, action, hostlev, numa
    start_date = format_date(stday, stmon, styear)
    end_date = format_date(endday, endmon, endyear)
    dict = {
        'type':'Feature',
        'geometry': {
            'type':'Point',
            'coordinates': [x, y]
        },
        'properties': {
            'incidnum3':incidnum3,
            'dispnum3':dispnum3,
            'start_date':start_date,
            'end_date':end_date 
        }
    }
    return json.dumps(dict)