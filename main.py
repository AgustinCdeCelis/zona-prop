from model.scrapper import data,full_data
import pandas as pd
from datetime import date



venta=full_data()



df=pd.DataFrame(venta[0]) # creating the dataframes from each category
df1=pd.DataFrame(venta[1])                         
#df_definite= pd.concat([df,df1],axis=0)

today = date.today()
d1 = today.strftime("%Y%m%d")
df.to_csv(f'./csv/{d1}zonaprops_venta_caba.csv', encoding='utf-8', index=False)
df1.to_csv(f'./csv/{d1}zonaprops_exclusiveventa_caba.csv', encoding='utf-8', index=False)

