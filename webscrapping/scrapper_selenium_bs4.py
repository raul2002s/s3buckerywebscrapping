from re import L
from selenium import webdriver

#from selenium.webdriver.firefox import firefox_profile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

import sys

from bs4 import BeautifulStoneSoup
import time

def main():

    #opciones para la navegacion
    options = webdriver.FirefoxOptions()
    #options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.headless = True
    
    #ruta del binario del driver 
    #binary = FirefoxBinary('/home/rauly/.wdm/drivers/geckodriver/linux64/0.31/geckodriver/geckodriver')
    
    #firefox_browser = webdriver.Firefox(executable_path='/home/rauly/.wdm/drivers/geckodriver/linux64/0.31/geckodriver/geckodriver')
    #firefox_browser = webdriver.Firefox(firefox_binary=binary)
    firefox_browser = webdriver.Firefox(GeckoDriverManager().install())
    #en caso q este trabajando con 2 pantallas le seteo manualmente la posicion al browser
    #firefox_browser.set_window_position(2000,0)
    #firefox_browser.maximize_window()
    
    #inicial el navegador
    #firefox_browser.start_client()
    
    #hago consulta a la ur
    firefox_browser.get('https://mercadolibre.com.pe')
    
    print(f"{firefox_browser.title}")
    time.sleep(3)
    
    #con estas siguientes lineas obtengo el input de busqueda, escribo teclados para filtar por teclados en la tienda
    
    search_input = firefox_browser.find_element(by=By.ID,value='cb1-edit')
    search_input.send_keys("teclados")
    #search_button = firefox_browser.find_element(by=By.CLASS_NAME,value='nav-search-btn')
    search_button = firefox_browser.find_element(by=By.XPATH,value='/html/body/header/div/form/button')   
    search_button.click()
    print("enviado")
   
    #obtengo si hay teclados q tengan descuentos del 30% y si hubieran, agarro la url
    descuento_treinta_percent = firefox_browser.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/aside/section/div[9]/ul/li[4]/a')
    if descuento_treinta_percent != None:
        url_descuento = descuento_treinta_percent.get_attribute('href')
        #print(f"{url_descuento}")
        time.sleep(3)
        print("redirigiendo a la url del 30 porciento de descuento")
        firefox_browser.get(url=url_descuento)
        time.sleep(3)
        teclados_descuento = firefox_browser.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/section/ol')
        teclados = teclados_descuento.find_elements(by=By.TAG_NAME, value='li')
        #print(f"{teclados}")
               
        for item in teclados:
            titulo = item.find_element(by=By.TAG_NAME,value='h2').text
            precio = item.find_element(by=By.CLASS_NAME,value='price-tag-fraction').text
            url = item.find_element(by=By.TAG_NAME,value='a').get_attribute('href')
            print("*"*10)          
            print(f"articulo: {titulo}")
            print(f"precio: {precio}")  
            print(f"url: {url}")  
            
    
    
    
    
    
    #hago esperar al navegador hasta q exista un elemento clickeable seleccionandolo por su class name para el caso del buscador de la pagina
    #WebDriverWait(firefox_browser, 5).until(EC.element_to_be_clickable(By.CLASS_NAME['input.nav-search-input']))

    

    #firefox_browser.quit()



    






if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()    
