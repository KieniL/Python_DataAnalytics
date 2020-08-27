import pandas as pd
import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass
    
#import all necessary csv files
url_list = ["http://data.statistik.gv.at/data/OGD_f0760ext_OD_PkwGZL_1.csv", #data
    "http://data.statistik.gv.at/data/OGD_f0760ext_OD_PkwGZL_1_HEADER.csv", #header
    "http://data.statistik.gv.at/data/OGD_f0760ext_OD_PkwGZL_1_C-J59-0.csv", #automarken
    "http://data.statistik.gv.at/data/OGD_f0760ext_OD_PkwGZL_1_C-A10-0.csv", #datum
    "http://data.statistik.gv.at/data/OGD_f0760ext_OD_PkwGZL_1_C-EK7-0.csv" #fahrzeugtyp
]

# empty lists to store the filenames and the dataframes
filename_list = ["data", "header", "marke", "datum", "typ"]
#Own key for filename (same name as filenames but without .csv)
dataframes = {}

warnings.simplefilter('ignore',InsecureRequestWarning)
# Using for loop 
	
#Create the csv
for i in range(len(url_list)):
    open(filename_list[i]+".csv", 'wb').write(requests.get(url_list[i], verify=False).content)

#Read csv and add to dataframe
for i in range(len(filename_list)):
    dataframes[filename_list[i]] = pd.read_csv(filename_list[i]+".csv", sep=";", header=0)


#ToDo REplace first column with Automarke
#ToDo Replace Second Column with date
#ToDo Replace Third Column with Type