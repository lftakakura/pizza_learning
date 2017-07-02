from selenium import webdriver

url = 'http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/?page='
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

MAX_PAGES = 1400
j = 0
for i in range(519, MAX_PAGES):
    with open('movies_links', 'a') as f:

        driver.get(url + str(i))
        movie_pages = driver.find_elements_by_xpath("//h2[contains(@class,'tt_18 d_inline')]/a")

        movies = list()

        for movie in movie_pages:
            movie = movie.get_attribute("href")

            movies.append(movie)
            j += 1

            print("Got %i movie links" % j)

        print("Saving movies links")
        for item in movies:
            f.write("%s\n" % item)

    # with open('movies_links', 'w') as f:
    #     print("Saving movies links")
    #     for item in movies:
    #         f.write("%s\n" % item)

driver.quit()
