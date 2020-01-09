import pandas as pd
filepaths = ['states2016.csv', 'majors2016.csv', 'system2016.csv', 'Non-StateWarData_v4.0.csv', 'Intra-StateWarData_v4.1.csv', 'Inter-StateWarData_v4.0.csv', 'Extra-StateWarData_v4.0.csv', 'MIDLOCA_2_0.csv', 'MIDLOCI_2_0.csv', 'MIDLOC_1.1.csv', 'WRP_national.csv', 'WRP_regional.csv', 'WRP_global.csv', 'Diplomatic_Exchange_2006v1.csv', 'directed_dyadic_war.csv', 'MID 4.3/MIDA 4.3.csv', 'MID 4.3/MIDB 4.3.csv', 'MID 4.3/MIDI 4.3.csv', 'MID 4.3/MIDP 4.3.csv', 'MIDI_4.01.csv', 'MIDIP_4.01.csv', 'MIDA_210.TXT', 'MIDB_210.TXT', 'MIDC_210.TXT', 'MID 2.1EE.csv', 'NMC_5_0.csv', 'NMC_5_0-wsupplementary.csv', 'NMC_Supplement_v4_0.csv', 'version4.1_csv/alliance_v4.1_by_directed.csv', 'version4.1_csv/alliance_v4.1_by_directed_yearly.csv', 'version4.1_csv/alliance_v4.1_by_dyad.csv', 'version4.1_csv/alliance_v4.1_by_dyad_yearly.csv', 'version4.1_csv/alliance_v4.1_by_member.csv', 'version4.1_csv/alliance_v4.1_by_member_yearly.csv', 'Territorial Change Data/Territorial Change Data, 1816-2018.xls', 'DirectContiguity320/contdir.csv', 'DirectContiguity320/contdird.csv', 'DirectContiguity320/contdirs.csv', 'ColonialContiguity310/contcol.csv', 'ColonialContiguity310/contcold.csv', 'ColonialContiguity310/contcols.csv', 'igo_year_formatv3.csv', 'state_year_formatv3.csv', 'dyadic_formatv3.csv', 'igounit_v2.3.csv', 'IGO_stateunit_v2.3.csv', 'IGO_dyadunit_v2.3.csv', 'COW_Trade_4.0/Dyadic_COW_4.0.csv', 'COW_Trade_4.0/National_COW_4.0.csv', 'COW_Trade_3.0/dyadic_trade_3.0.csv', 'COW_Trade_3.0/national_trade_3.0.csv', 'COW_Trade_2.01/dyadic_trade_2.01.csv', 'COW_Trade_2.01/national_trade_2.0.csv', 'kinne_dca/DCAD-v1.0-dyadic.csv', 'kinne_dca/DCAD-v1.0-main.csv']
filepaths = ['Resources/'+file for file in filepaths]
filepaths
with_errors = []
for filepath in filepaths:
    try:
        try:
            df = pd.read_csv(filepath, delimiter=',', encoding='utf-8',low_memory=False)
            #df.head()
            print('Success - ' +str(filepath))
        except:
            df = pd.read_csv(filepath, delimiter=',', encoding='ISO-8859-1',low_memory=False)
            #df.head()
            print('Success - ' +str(filepath))
    except:
        print('ERROR - ' + str(filepath))
        with_errors.append(filepath)
print()
print('Success reading ' + str(len(filepaths)-len(with_errors)) + ' files.')
print('Failed to read ' + str(len(with_errors)) + ' files.')
print()

# if len(with_errors) > 0:
#     for filepath in with_errors:
#         try: 
#             df = pd.read_excel(filepath, delimiter='.', encoding='utf-8',low_memory=False)
#             print('Success - ' +str(filepath))

#         except:
#             try:
#                 df = pd.read_excel(filepath, delimiter=' ', encoding='utf-8',low_memory=False)
#                 print('Success - ' +str(filepath))
#             except:
#                 print('ERROR - ' + str(filepath))
df = pd.read_excel('Resources/Territorial Change Data/Territorial Change Data, 1816-2018.xls')
df.head()

df = pd.read_stata('Resources/IGO_stata/igo_year_format_3.dta')
df.head()
df.to_csv('Resources/igo_year_formatv3.csv')
df = pd.read_csv('Resources/igo_year_formatv3.csv')
df.head()