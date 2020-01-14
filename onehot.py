import pandas as pd
import numpy as np

df = pd.read_csv("df/property.csv")
# encode property type (one hot encoding)
property_type = df["property_type"]
# create columns for  "property_type" dummy variables
pType = pd.get_dummies(df.property_type)
pType.rename(columns={1.0:'type_1',
                    2.0:'type_2',
                    3.0:'type_3',
                    4.0 : 'type_4',
                    5.0 : 'type_5',
                    6.0 : 'type_6'}, 
                 inplace=True)
# print all columns including type
# merged = pd.concat([df,pType],axis='columns')

pStatus = pd.get_dummies(df.property_status)
pStatus.rename(columns={0.0: 'status_1',
                    1.0: 'status_2',
                    2.0: 'status_3',
                    3.0 :  'status_4',
                    4.0 :  'status_5',
                    5.0 :  'status_6'}, 
                 inplace=True)

pPack = pd.get_dummies(df.property_package)
pPack.rename(columns={1.0:'pack_1',
                    2.0:'pack_2',
                    3.0:'pack_3',
                    4.0 : 'pack_4',
                    5.0 : 'pack_5',
                    6.0 : 'pack_6'}, 
                 inplace=True)

pDesign = pd.get_dummies(df.property_design)
pDesign.rename(columns={0.0: 'design_1',
                    1.0: 'design_2',
                    2.0: 'design_3',
                    3.0 :  'design_4',
                    4.0 :  'design_5',
                    5.0 :  'design_6'}, 
                 inplace=True)

pProx = pd.get_dummies(df.property_proximity)
pProx.rename(columns={0.0: 'prox_1',
                    1.0: 'prox_2',
                    2.0: 'prox_3',
                    3.0 :  'prox_4',
                    4.0 :  'prox_5',
                    5.0 :  'prox_6'}, 
                 inplace=True)

pLifeSupport = pd.get_dummies(df.property_life_support)
pLifeSupport.rename(columns={0.0: 'life_support_1',
                    1.0: 'life_support_2',
                    2.0: 'life_support_3',
                    3.0 :  'life_support_4',
                    4.0 :  'life_support_5',
                    5.0 :  'life_support_6'}, 
                 inplace=True)

pService = pd.get_dummies(df.property_service)
pService.rename(columns={0.0: 'service_1',
                    1.0: 'service_2',
                    2.0: 'service_3',
                    3.0 :  'service_4',
                    4.0 :  'service_5',
                    5.0 :  'service_6'}, 
                 inplace=True)

pArea = pd.get_dummies(df.area_id)

# property_bedrooms (data not good man)
# pBedrooms = pd.get_dummies(df.property_bedrooms)
# pBedrooms.rename(columns={0.0: 'bedroom_1',
#                     1.0: 'bedroom_2',
#                     2.0: 'bedroom_3',
#                     3.0 :  'bedroom_4',
#                     4.0 :  'bedroom_5',
#                     5.0 :  'bedroom_6'}, 
#                  inplace=True)

pEmployee = pd.get_dummies(df.employee_id)

# object for all encoded df
dummies = pd.concat([pType,pStatus,pPack,pDesign,pProx,pLifeSupport,pService,pArea,pEmployee],axis='columns')
# convert dummies to new csv
dummies.to_csv(r'D:\bukitvista\encode\df\ready\property_dummies.csv')