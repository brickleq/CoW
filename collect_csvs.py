#%%
import io
import requests
import os
import pandas as pd
import tempfile
from urllib.request import urlopen
if sys.version_info >= (3, 6):
    import zipfile
else:
    import zipfile36 as zipfile
from zipfile import ZipFile
# %%
csv_urls = [['states2016.csv','http://www.correlatesofwar.org/data-sets/state-system-membership/states2016'],
 ['majors2016.csv','http://www.correlatesofwar.org/data-sets/state-system-membership/majors2016'],
 ['system2016.csv','http://www.correlatesofwar.org/data-sets/state-system-membership/system2016'],
 ['Non-StateWarData_v4.0.csv','http://www.correlatesofwar.org/data-sets/COW-war/non-state-war-data-1'],
 ['Intra-StateWarData_v4.1.csv','http://www.correlatesofwar.org/data-sets/COW-war/intra-state-war-data-v4-1'],
 ['Inter-StateWarData_v4.0.csv','http://www.correlatesofwar.org/data-sets/COW-war/inter-state-war-data'],
 ['Extra-StateWarData_v4.0.csv','http://www.correlatesofwar.org/data-sets/COW-war/extra-state-war-data'],
 ['MIDLOCA_2_0.csv','http://www.correlatesofwar.org/data-sets/MIDLOC/midloca-2.0/at_download/file'],
 ['MIDLOCI_2_0.csv','http://www.correlatesofwar.org/data-sets/MIDLOC/midloci-2.0/at_download/file'],
 ['MIDLOC_1.1.csv','http://www.correlatesofwar.org/data-sets/militarized-interstate-dispute-locations-v1-1/MIDLOC_1.1.csv/at_download/file'],
 ['WRP_national.csv','http://www.correlatesofwar.org/data-sets/world-religion-data/wrp-national-data-1/at_download/file'],
 ['WRP_regional.csv','http://www.correlatesofwar.org/data-sets/world-religion-data/wrp-regional-data/at_download/file'],
 ['WRP_global.csv','http://www.correlatesofwar.org/data-sets/world-religion-data/wrp-global-data/at_download/file'],
 ['Diplomatic_Exchange_2006v1.csv','http://www.correlatesofwar.org/data-sets/diplomatic-exchange/diplomatic-exchange-v2006-1-data/at_download/file','Data of diplomatic exchange']]
# for url in csv_urls:
#     print(url)
#%%
zip_urls = [['Dyadid_Interstate_War_Dataset.zip','http://www.correlatesofwar.org/data-sets/COW-war/dyadic-inter-state-war-dataset/at_download/file'],
['MID_4_3.zip','http://www.correlatesofwar.org/data-sets/MIDs/mid-level-v4-3-data-files/at_download/file'],
['Incident-level.zip','http://www.correlatesofwar.org/data-sets/MIDs/incident-level/at_download/file'],
['MIDS_210.zip','http://www.correlatesofwar.org/data-sets/MIDs/mid-v-2.1/at_download/file'],
['MID_2.1EE.zip','http://www.correlatesofwar.org/data-sets/MIDs/mid-v-2.1ee/at_download/file'],
['NMC_5_0.zip','http://www.correlatesofwar.org/data-sets/national-material-capabilities/nmc-v5-1/at_download/file'],
['NMC_5_0-wsupplementary.zip','http://www.correlatesofwar.org/data-sets/national-material-capabilities/nmc-v5-supplemental/at_download/file'],
['NMC_Summplement_v4_0.csv.zip','http://www.correlatesofwar.org/data-sets/national-material-capabilities/nmc-supplement-v4-csv/at_download/file'],
['version4.1_csv.zip','http://www.correlatesofwar.org/data-sets/formal-alliances/alliances-data-csv-zip/at_download/file','Alliances data.csv ZIP'],
['http://www.correlatesofwar.org/data-sets/territorial-change/territorial-change-data-1816-2018/at_download/file','Territorial Change Data 1816-2018'],
['DirectContiguity320.zip','http://www.correlatesofwar.org/data-sets/direct-contiguity/direct-contiguity-v3-2/at_download/file','Direct Contiguity (v3.2)'],
['ColonialContiguity310.zip','http://www.correlatesofwar.org/data-sets/colonial-dependency-contiguity/colonial-dependency-contiguity-v3-1/at_download/file','Colonial/Dependency Contiguity (v3.1)'],
['IGO_igounit_v3.zip','http://www.correlatesofwar.org/data-sets/IGOs/igo_igounit_v3.zip/at_download/file','Intergovernmental Organizations - IGO-year level (v3)'],
['IGO_stateunit_v3.zip','http://www.correlatesofwar.org/data-sets/IGOs/igo_stateunit_v3.zip/at_download/file','Intergovernmental Organizations - country-year level (v3)'],
['dyadic_formatv3.zip','http://www.correlatesofwar.org/data-sets/IGOs/igo_dyadunit_v3.zip/at_download/file','Intergovernmental Oganizations - dyad-year level (v3)'],
['IGO_igounity_v2.3.zip','http://www.correlatesofwar.org/data-sets/IGOs/IGO_igounit_v2.3.zip/at_download/file','Data on IGOs from 1815-2005, at the IGO-year level. Contains one record per IGO-year (with years listed at 5 year intervals through 1965, and annually thereafter).'],
['IGO_stateunit_v2.3.zip','http://www.correlatesofwar.org/data-sets/IGOs/IGO_stateunit_v2.3.zip/at_download/file','Data on IGOs from 1815-2005, at the country-year level. Contains one record per country-year (with years listed at 5 year intervals through 1965, and annually thereafter).'],
['IGO_dyadunit_csv_v2.3.zip','http://www.correlatesofwar.org/data-sets/IGOs/igo_dyadunit_csv_v2-3.zip/at_download/file','Data on IGOs from 1815-2005, at the dyad-year level. Contains one record per dyad-year (with years listed at 5 year intervals through 1965, and annually thereafter).'],
['COW_Trade_4.0.zip','http://www.correlatesofwar.org/data-sets/bilateral-trade/cow_trade_4.0/at_download/file','International Trade, 1870-2014 (v4.0)'],
['COW_Trade_3.0.zip','http://www.correlatesofwar.org/data-sets/bilateral-trade/cow_trade_3.0/at_download/file','International Trade (v3.0)'],
['COW_Trade_2.01.zip','http://www.correlatesofwar.org/data-sets/bilateral-trade/cow_trade_2.01/at_download/file','International Trade (v2.01)'],
['kinne_dca.zip','http://www.correlatesofwar.org/data-sets/defense-cooperation-agreement-dataset/dcad-1980-2011-1/at_download/file','Zip file containing the DCAD dyadic and main data in .csv format and the codebook.']]

for zip in zip_urls:
    url = zip[1]
    response = requests.get(url, stream=True)
    archive = ZipFile(io.BytesIO(response.content))
    print(archive.namelist())

#%%
try:
    os.mkdir('Resources')
except:
    pass
# for url in zip_urls:
#     print(url)
#%%
no_luck = 0
for csv in csv_urls:
    try:
        filename = str(url[0])
        path = 'Resources/' + filename
        data = pd.read_csv(csv[1])
        data.to_csv(path)
        print('Success saving ' + filename + '\n')
    except: 
        print('ERROR saving ' + filename + '... trying again....')
        try: 
            filename = str(url[0])
            path = 'Resources/' + filename
            data = pd.read_csv(csv[1], encoding='ISO-8859-1')
            data.to_csv(path)
            print('Success saving ' + filename + '\n')
        except:
            print('Sorry, NO LUCK saving ' + filename + '.')
            no_luck += 1
print('\nSuccessfully saved ' + str(len(csv_urls)-no_luck) + ' CSV files.') 
if no_luck > 0:
    print('Failed to save ' + str(no_luck) + ' files in CSV format. Please download them manually to the /Resources/ folder.')