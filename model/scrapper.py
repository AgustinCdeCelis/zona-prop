import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException ,StaleElementReferenceException
from datetime import date


def data(products):
    cont_product=0
    product_list=[]
    for i in products:
        #cuenta producto
        cont_product+=1
        #this is the count fraction to check the scrapped elements
        print(f'{cont_product} / {len(products)} Elemento escrapeado')
        #diccionario del dato
        #fecha tabla
        today = date.today() #hold the date
        d1 = today.strftime("%Y%m%d")
        current_product={'fecha':d1,'tipo_transacción':'venta_inmueble'}
        #codigo html del producto
        codigo_html = i.get_attribute('innerHTML')
        soup=BeautifulSoup(codigo_html,'html.parser')
        
        #precio producto
        precio= soup.find('div',attrs={'data-qa':'POSTING_CARD_PRICE'}).text
        
        current_product['precio_inmueble']=precio
        #data explicita del inmueble
        try:
            data= soup.find('div',attrs={'data-qa':'POSTING_CARD_FEATURES'})
            sub_cats=data.find_all('span')
            datos=''
            for u in sub_cats:
            
                datos+=u.text+' '
            
            current_product['datos']= datos
        except:
            current_product['datos']=None
        
        #direccion=soup.find('div',class_='sc-ge2uzh-0 eXwAuU')
        #print(direccion)
        

        barrio= soup.find('div',attrs={'data-qa':'POSTING_CARD_LOCATION'}).text
        
        current_product['barrio']=barrio
        try:
            expensas= soup.find('div',attrs={'data-qa':'expensas'}).text
            
            current_product['expensas']=expensas
        except:
            current_product['expensas']=None
        try:
            descripcion= soup.find('div',attrs={'data-qa':'POSTING_CARD_DESCRIPTION'}).text
            
            current_product['descripcion']=descripcion
        except:
            current_product['descripcion']=None


        product_list.append(current_product)

    return product_list

def data_important(prod):
    cont_product=0
    product_list=[]
    for i in prod:
        #cuenta producto
        cont_product+=1
        #this is the count fraction to check the scrapped elements
        print(f'{cont_product} / {len(prod)} Elemento escrapeado')
        #diccionario del dato
        #fecha tabla
        today = date.today() #hold the date
        d1 = today.strftime("%Y%m%d")
        current_product={'fecha':d1,'tipo_transacción':'venta_inmueble'}
        #codigo html del producto
        codigo_html = i.get_attribute('innerHTML')
        soup=BeautifulSoup(codigo_html,'html.parser')
        #precio inicial-->mas barato
        precio_in= soup.find('div',attrs={'data-qa':'POSTING_CARD_PRICE_FROM'}).text
        current_product['precio_inicial']=precio_in
        #precio final-->más caro
        precio_fin= soup.find('div',attrs={'data-qa':'POSTING_CARD_PRICE_TO'}).text
        current_product['precio_fin']=precio_fin
        try:
            data= soup.find('div',attrs={'data-qa':'POSTING_CARD_FEATURES'})
            sub_cats=data.find_all('span')
            datos=''
            for u in sub_cats:
            
                datos+=u.text+' '
            
            current_product['datos']= datos
        except:
            current_product['datos']=None

        amenities=soup.find_all('span',attrs={'color':'#3A0C3D'})
        datos2=''
        for y in amenities:

            datos+=y.text+' '

        direccion=soup.find('a',attrs={'data-qa':'POSTING_CARD_LOCATION'}).text
        current_product['direccion']= direccion

        imagen=soup.find('img')['src']
        current_product['imagen']=imagen

        product_list.append(current_product)

    return product_list

        








def full_data():
    link = 'https://www.zonaprop.com.ar/inmuebles-venta-capital-federal.html'
    PATH= "/usr/lib/chromium-browser/chromedriver"
    s = Service(PATH)
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')  # Habilitar el modo sin cabeza
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=s)
    driver.get(link)
    driver.maximize_window()
    time.sleep(3)
    cantidad =driver.find_element(By.CSS_SELECTOR,'.sc-5z85om-2.ePSQiV').text
    numero= int(cantidad.split(' ')[0].replace('.',''))
    print(numero)
    number_pages = numero//20+1
    print(number_pages)
    


    time.sleep(2)

    full_elem= driver.find_element(By.CSS_SELECTOR,'div.postings-container')

    elementos=driver.find_elements(By.CSS_SELECTOR,'div[data-qa="posting PROPERTY"]')
    print(len(elementos))
    final_work=[]#guardo todo acá
    final_work.extend(data(elementos))

    elementos_importantes =driver.find_elements,'div[data-qa="posting DEVELOPMENT"]'
    print(elementos_importantes)


    for i in range(2,number_pages+1):
        link_modified= f'https://www.zonaprop.com.ar/inmuebles-venta-capital-federal-pagina-{i}.html'
        s = Service(PATH)

        driver = webdriver.Chrome(service=s)

        driver.get(link_modified)
        time.sleep(3)
        full_elem= driver.find_element(By.CSS_SELECTOR,'div.postings-container')

        elementos=driver.find_elements(By.CSS_SELECTOR,'div[data-qa="posting PROPERTY"]')
        final_work.extend(data(elementos))
    

        driver.quit()

    return final_work


