''' installs
py -m venv env
env/Scripts/activate
python.exe -m pip install --upgrade pip
pip install requests
pip install bs4
pip install lxml
pip install selenium

'''
'''
pip install asyncio
pip install aiogram
pip install aiofiles
pip install aiocsv

deactivate
pip install webdriver-manager

'''

import json
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By



def save_selenium(url):
    link = url
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')

    try:
        driver = webdriver.Firefox(
            executable_path='C:\\projects\\selenium\\geckodriver.exe',
            options=options,
        )
        driver.get(url=link)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

    except Exception as ex:
        print(ex)
        #with open('./blank/otl_oge.html', 'w', encoding='utf-8') as f:
        #    f.write(driver.page_source)
    finally:
        body = driver.find_element(by=By.CLASS_NAME, value="body")

        print(body.text)


        time.sleep(3)
        driver.close()
        driver.quit()

def parse_url():
    # open index.html
    with open('index.html', 'r', encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml') # create soup object
    titles = soup.find_all('div', {"class":'similar-item__title'})
    phones = soup.find_all('div',{"class":'phone'})
    phones2 = []
    for phone in phones:
        phone_text = phone.text.replace('\n','')
        phones2.append(phone_text)


    items = []

    for i in range (len(titles)):
        #print('www.',i.get('href'),' : ',i.get_text(),sep='')
        #print(f"www.{title.get('href')} : {title.get_text()}")


        #save json file

        title_a=titles[i].contents[1]
       # print(title2)
        title_text=title_a.get_text()
        href = f"{title_a.get('href')}"
        phone = phones2[i]
        #print(title_text)
        items.append(
                {
                    title_text : href ,
                    'phone': phone.strip()

                }
        )

    print(items)
    with open("./data/data.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)



def main():
    #save_selenium(r'https://www.orgpage.ru/moskva/%D0%BC%D1%8F%D1%81%D0%BE%D0%BA%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%82%D1%8B/')

    parse_url()

if __name__ == '__main__':
    main()
