# W konsolę wpisać:
# python -m venv .venv
# .\.venv\Scripts\activate.ps1
# pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# konfiguracja Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--start-maximized")

# otworzenie przeglądarki Chrome
driver = webdriver.Chrome(options=chrome_options)

# nawigacja do strony www
driver.get("https://equibeam.mechadevs.com/Identity/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DBeamAnalyzerWeb%26redirect_uri%3Dhttps%253A%252F%252Fequibeam.mechadevs.com%252Fauthentication%252Flogin-callback%26response_type%3Dcode%26scope%3DBeamAnalyzerWebAPI%2520openid%2520profile%26state%3Dba11e386a0414498b3d31393d9ba7a09%26code_challenge%3DGeqD88ovg3dpaPxz2mH7dnfGtl6jPer_KHzifrMMjxU%26code_challenge_method%3DS256%26response_mode%3Dquery")

# manipulacja obiektem inputbox na Wikipedia
elem = driver.find_element("xpath",'//*[@id="Input_Email"]')
elem.clear()
elem.send_keys("sylwia.grudowska5@gmail.com") # wpisanie słowa w przeglądarkę
elem.send_keys(Keys.RETURN)
elem = driver.find_element("xpath",'//*[@id="Input_Password"]')
elem.clear()
elem.send_keys("Dupa1!")
elem.send_keys(Keys.RETURN)
'''# manipulacja kursorem na najechanie obrazka
link = driver.find_element('xpath','//*[@id="main-page-didyouknow"]/p[2]/i[1]/b/a')
webdriver.ActionChains(driver).move_to_element(link).perform()'''



