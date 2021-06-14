import requests
import xml.etree.ElementTree as ET
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from funciones import *

## se hace el request de CHILE
url_chile = "https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_CHL.xml"
resp_chile = requests.get(url_chile)
content_chile = resp_chile.content

## se hace el request de NZL
url_nzl = "https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_NZL.xml"
resp_nzl = requests.get(url_nzl)
content_nzl = resp_nzl.content

## se hace el request de ZAF
url_zaf = "https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_ZAF.xml"
resp_zaf = requests.get(url_zaf)
content_zaf = resp_zaf.content

## se hace el request de ESP
url_esp = "https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_ESP.xml"
resp_esp = requests.get(url_esp)
content_esp = resp_esp.content

## se hace el request de NLD
url_nld = "https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_NLD.xml"
resp_nld = requests.get(url_nld)
content_nld = resp_nld.content

## se hace el request de SWE
url_swe = "https://storage.googleapis.com/tarea-4.2021-1.tallerdeintegracion.cl/gho_SWE.xml"
resp_swe = requests.get(url_swe)
content_swe = resp_swe.content


root_chl = ET.fromstring(content_chile)
root_nzl = ET.fromstring(content_nzl)
root_zaf = ET.fromstring(content_zaf)
root_esp = ET.fromstring(content_esp)
root_nld = ET.fromstring(content_nld)
root_swe = ET.fromstring(content_swe)

roots = [root_chl, root_esp, root_nld, root_nzl, root_swe, root_zaf]

headers = ['GHO', 'COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'Display', 'Numeric', 'Low',
           'High']

df_list = []
df_dic = {'GHO': [], 'COUNTRY': [], 'SEX': [], 'YEAR': [], 'GHECAUSES': [], 'AGEGROUP': [],
          'Display': [], 'Numeric': [], 'Low': [], 'High': []}


for root in roots:
    for child in root:
        row_list = [None]*10
        for child2 in child:
            if child2.tag in headers:
                idx = headers.index(child2.tag)
                df_dic[child2.tag].append(child2.text)
                row_list[idx] = child2.text

        df_list.append(row_list)

for row in df_list:
    if row[0] in ['Number of under-five deaths', 'Number of infant deaths', 'Number of deaths']:
        row[7] = eliminar_decimales(row[7])
        row[8] = eliminar_decimales(row[8])
        row[9] = eliminar_decimales(row[9])
    elif row[0] in ['Mortality rate attributed to unintentional poisoning (per 100 000 population)',
                    'Crude suicide rates (per 100 000 population)']:
        row[7] = de_rate_a_popuilation(row[7], row[1])

df = pd.DataFrame(df_list, columns=headers)
pd.set_option('display.max_columns', None)

gc = gspread.service_account(filename='credenciales.json')
sh = gc.open_by_key('1Z6NEkGUYJPoMbbhUVNJ8kU4W6jqcK92FQ7frI4A0b00')
worksheet = sh.get_worksheet(0)

set_with_dataframe(worksheet, df)
