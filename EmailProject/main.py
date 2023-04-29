from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import smtplib


options = Options()
options.add_argument("--headless")
PATH = 'C:\Program Files (x86)\chromedriver.exe'
URL = 'https://www.gsuplementos.com.br/whey-protein-concentrado-1kg-growth-supplements-p985936'

driver = webdriver.Chrome(PATH,options=options)
driver.get(URL)
html = driver.execute_script("return document.documentElement.innerHTML")
driver.quit()
soup = BeautifulSoup(html, "html.parser")
soup.prettify
lists = soup.find_all("li", {"class": "option"})

def send_email(body, subject):
    server = smtplib.SMTP('smtp.gmail.com', 587)    
    server.ehlo()    
    server.starttls()    
    server.ehlo()    
    server.login('lucas.hrqc@gmail.com', 'cdixjrajwacpvpgg')   
    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail('lucas.hrqc@gmail.com', 'lucas.hrqc@gmail.com', msg)     
    print('Email sent !')     
    server.quit()

for li in lists:
    if (li.string == 'Chocolate Branco'):
        print(li)
        subject = 'Eu sei o que você fez verão passado!'
        body = 'Cagou na moita'
        send_email(body,subject)
