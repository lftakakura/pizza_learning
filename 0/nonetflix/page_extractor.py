from enum import Enum
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time


reload(sys)
sys.setdefaultencoding('utf-8')


class Category(Enum):
    Acao = 1
    Documentario = 2
    Romance = 3
    Drama = 4
    Terror = 5
    Comedia = 6
    Suspense = 7

urls = ['http://www.nonetflix.com.br/categoria/acao-e-aventura',
        'http://www.nonetflix.com.br/categoria/documentarios',
        'http://www.nonetflix.com.br/categoria/filmes-romanticos',
        'http://www.nonetflix.com.br/categoria/dramas',
        'http://www.nonetflix.com.br/categoria/filmes-de-terror',
        'http://www.nonetflix.com.br/categoria/comedias',
        'http://www.nonetflix.com.br/categoria/suspenses']
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

category = 0

for url in urls:
    category += 1
    prev_page = 0

    desc_list = list()
    labels = list()

    driver.get(url)
    main_window = driver.current_window_handle

    while True:
        driver.switch_to_window(main_window)

        # time.sleep(2)
        # print('Waited 2 seconds')

        page = driver.find_elements_by_class_name("pgctr")[0].text.split(' - ')
        current_page = int(str(page[0]).strip())
        end_page = int(str(page[1]).strip())

        print("Current page: %s\nFinal page: %s" % (current_page, end_page))

        button = driver.find_elements_by_class_name("glyphicon-chevron-right")[0]
        button = button.find_element_by_xpath('..')

        if current_page > prev_page:
            description = driver.find_elements_by_class_name("msyn")
            for desc in description:

                text = re.sub(r'^[0-9]+\,[0-9]+', '', desc.text)
                text = text.strip()

                desc_list.append(str(text))
                # print(text)
                # print('----------')
                labels.append(category)

            df = pd.DataFrame(desc_list, labels)
            with open('nonetflix.csv', 'a') as f:
                print("Saving page %s" % current_page)
                df.to_csv(f, header=False)

            prev_page = current_page

        if current_page == end_page:
            break

        button.click()

driver.quit()
