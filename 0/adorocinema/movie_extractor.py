import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

categories_dict = {
    'Ação': '1',
    'Animação': '2',
    'Aventura': '3',
    'Biografia': '4',
    'Comédia': '5',
    'Comédia dramática': '6',
    'Drama': '7',
    'Documentário': '8',
    'Família': '9',
    'Fantasia': '10',
    'Ficção científica': '11',
    'Guerra': '12',
    'Policial': '13',
    'Romance': '14',
    'Terror': '15'
}

with open('movies_links') as f:
    i = 0
    rows = list()
    for movie in f:
        html = urllib.request.urlopen(movie)
        html = html.read().decode('utf-8')

        parsed_html = BeautifulSoup(html, "lxml")
        description = parsed_html.body.find('div', attrs={'class': 'synopsis-txt'})

        if description:
            description = parsed_html.body.find('div', attrs={'class': 'synopsis-txt'}).text.strip()
            description = description.replace("\"", "\'")
            description = '\"' + description + '\"'

            categories = parsed_html.body.find_all('span', attrs={'itemprop': 'genre'})

            categories_list = list()

            for categ in categories:
                categ_id = categories_dict.get(categ.text.strip())

                if categ_id is not None:
                    categories_list.append(categ_id)

            # normalize number of categories to 3
            if len(categories_list) < 3:
                while len(categories_list) < 3:
                    categories_list.append('0')
            elif len(categories_list) > 3:
                categories_list = categories_list[0:3]

            categories_list[0] = '\"' + categories_list[0] + '\"'
            categories_list[1] = '\"' + categories_list[1] + '\"'
            categories_list[2] = '\"' + categories_list[2] + '\"'

            # driver.get(movie)
            # description = driver.find_elements_by_class_name("synopsis-txt")[0].text
            # description = description.replace("\"", "\'")
            # description = '\"' + description + '\"'
            # categories = driver.find_elements_by_xpath("//div[@class='meta-body-item']/a[@class='xXx blue-link']")
            #
            # categories_list = list()
            #
            # for categ in categories:
            #     categ_id = categories_dict.get(categ.text)
            #
            #     if categ_id is not None:
            #         categories_list.append(categ_id)
            #
            # # normalize number of categories to 3
            # if len(categories_list) < 3:
            #     while len(categories_list) < 3:
            #         categories_list.append('0')
            # elif len(categories_list) > 3:
            #     categories_list = categories_list[0:3]
            #
            # categories_list[0] = '\"' + categories_list[0] + '\"'
            # categories_list[1] = '\"' + categories_list[1] + '\"'
            # categories_list[2] = '\"' + categories_list[2] + '\"'

            # build a csv row
            row = str(','.join(categories_list)) + ',' + description.strip()

            # print(row)
            #
            # rows.append(row)

            i += 1
            with open('movies.csv', 'a') as file:
                file.write("%s\n" % row)

            file.close()

            print("Saved %i movie(s)" % i)


    # with open('movies.csv', 'w') as file:
    #     print("Saving movies")
    #     for item in rows:
    #         file.write("%s\n" % item)

driver.quit()
