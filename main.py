#from model.scrapper import data,full_data
import pandas as pd
from datetime import date

from model.scrapper import main

#link='https://www.zonaprop.com.ar/inmuebles-venta-neuquen.html'
#link= 'https://www.zonaprop.com.ar/inmuebles-venta-capital-federal.html'
#link='https://www.zonaprop.com.ar/inmuebles-venta-mendoza.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-mendoza.html'
#link= 'https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-capital-federal.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-buenos-aires-costa-atlantica.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-gba-norte.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-gba-oeste.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-buenos-aires-fuera-de-gba.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-neuquen.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-cordoba.html'
#link='https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-rio-negro.html'
#link= 'https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-mendoza.html'
#link= 'https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-neuquen.html'
link= 'https://www.zonaprop.com.ar/inmuebles-alquiler-temporal-entre-rios.html'

start_index = link.find("/", link.find("/", link.find("/") + 1) + 1) + 1
end_index = link.find(".", start_index)
result = link[start_index:end_index]
print(result)

venta=main(link)

df=pd.DataFrame(venta[0]) # creating the dataframes from each category
df1=pd.DataFrame(venta[1])                         


today = date.today()
d1 = today.strftime("%Y%m%d")
df.to_csv(f'./csv/{d1}zonaprops_{result}.csv', encoding='utf-8', index=False)
df1.to_csv(f'./csv/{d1}zonaprops_exclusive_{result}.csv', encoding='utf-8', index=False)

