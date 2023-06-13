from model.scrapper import data,full_data
import pandas as pd
from datetime import date



venta=full_data()



df=pd.DataFrame(venta) # creating the dataframes from each category


today = date.today()
d1 = today.strftime("%Y%m%d")
df.to_csv(f'./csv/{d1}zonaprops_venta_caba.csv', encoding='utf-8', index=False)

