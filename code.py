from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")



def tiedonHaku():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 5)
    driver.get('https://tietopalvelu.ytj.fi/?companyName=S%C3%A4hk%C3%B6-Sinssi+Oy&isCompanyValid=true&isCompanyTerminated=false')

    #lista asiakkaista
    a = ["100-ILMASTOINTI OY",
        "2M-IT OY",
        "3 D LINJA OY",
        "3 STEP IT OY",
        "A&S TRADING KB",
        "A. KALKE OY",
        "A. KUNINGAS KY",
        "A. S. MAASTOHITSAUS OY",
        "AALLON AUTO OY",
        "AALTO REAL ESTATE OY",
        "AALTODJ RY",
        ]
    
    b = {}

    
    print(len(a))
    m = len(a)
    for k in a:
        #Kirjoita hakukenttään ja hae
        haku = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/section/div[2]/div[1]/input')))
                                                                        
        print("onnistui")
        haku.clear()
        m = m -1
        print(m)
        haku.send_keys(k)

        etsi = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/section/button[1]'))).click()

        #Etsi elementti
        try:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[5]/table/tbody/tr/td[2]/div/div/div[2]')))
            element2 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[5]/table/tbody/tr/td[5]/div/div/div[2]')))
        except:
            continue

        #lisää tiedot sanakirjaan
        text = element.text
        text2 = element2.text
        b[text] = text2
        
        

    #Tiedoston muokkaus
    file_path = "C:\\Users\\käyttäjä\\Desktop\\data.txt"

    #Avaa tiedoston kirjoitustilassa
    with open(file_path, "w") as file:
        #Käy läpi sanakirjan
        for key, value in b.items():
            #Kirjoittaa tiedostoon
            file.write(f"{key}: {value}\n")

tiedonHaku()
