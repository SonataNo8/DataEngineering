import pandas as pd
data=pd.read_csv("Congress_White_House.csv")

#Let's target Employment status and salary
cols_to_drop=['Employee Name','Pay Basis','Position Title']

data.drop(columns=cols_to_drop,inplace=True)
data_status=pd.get_dummies(data['Employee Status'])
data_final=pd.concat([data, data_status],axis=1)
data_final.drop(columns='Employee Status',inplace=True)
