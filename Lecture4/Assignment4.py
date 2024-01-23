# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #4 - Data Scraping, Storage and Visualization
# Frederick Burke
import requests
import html5lib
from bs4 import BeautifulSoup
import OutputUtil as ou


def print_page_content(url):
    r = requests.get(url)
    print(r.content)


def parse_page_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())


def next_text(itr):
    return next(itr).text


def next_int(itr):
    return int(next_text(itr).replace(',', ''))


def scrape_covid_data(dict_countries_pop):
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []
    itr = iter(soup.find_all('td'))
    while True:
        try:
            country = next_text(itr)
            cases = next_int(itr)
            deaths = next_int(itr)
            continent = next_text(itr)
            if country.startswith('Japan'):
                country = 'Japan'
            if country in ['Channel Islands', 'MS Zaandam']:
                continue
            population = dict_countries_pop[country]
            percent_cases = round((cases / population) * 100, 2)
            percent_deaths = round((deaths / cases) * 100, 2)
            data.append([country, continent, population, cases, percent_cases, deaths, percent_deaths])

        # StopIteration error is raised when there are no more elements left for iteration
        except StopIteration:
            break
    return data


def scrape_population_data():
    url = 'https://www.worldometers.info/world-population/population-by-country/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []
    itr = iter(soup.find_all('td'))
    dict_countries = {}
    while True:
        try:
            no = next_text(itr)
            country = next_text(itr)
            population = next_int(itr)
            for i in range(9):
                junk = next_text(itr)
            dict_countries[country] = population
            print(country, population)
        except StopIteration:
            break
    return dict_countries


def make_output(data, assn):
    title = "Covid data by Country"
    align = ["l", "l", "r", "r", "r", "r", "r"]
    types = ["S", "S", "N", "N", "N", "N", "N"]
    heads = ["Country", "Continent", "Population", "Cases", "Pct Cases", "Deaths", "Pct Deaths"]
    ou.write_tt_file(assn + ".txt", title, heads, data, align)
    ou.write_csv_file(assn + ".csv", heads, data)
    ou.write_xml_file(assn + ".xml", title, heads, data, True)
    do_graph(assn, data, title)
    for i in range(len(data)):
        add_wiki_link(data, i,0)
        add_wiki_link(data, i,1)
    ou.add_stats(data, [2,3,4,5,6], 0,1,True)
    ou.write_html_file(assn + ".html", title, heads, types, align, data, True)


def do_graph(assn, data, title):
    x_label = 'Population'
    y_label = 'Cases'
    x_data = [data[i][2] for i in range(len(data))]
    y_data = [data[i][3] for i in range(len(data))]
    x_ticks = [i * 1000000 for i in range(50)]
    y_ticks = [i * 1000000 for i in range(50)]
    ou.write_bar_graph(assn + ".png", title, x_label, x_data, x_ticks, y_label, y_data, y_ticks)


def add_wiki_link(data, i, j):
    name = data[i][j]
    wiki_name = name
    if wiki_name == 'Australia/Oceania':
        wiki_name = 'Australia'
    href = "https://www.wikipedia.org/wiki/" + wiki_name.replace(' ', '_')
    a_attributes = 'href="' + href + '" target="_blank"'
    data[i][j] = ou.create_element(ou.TAG_A, name, a_attributes)


def main():
    dict_countries_pop = scrape_population_data()
    data = scrape_covid_data(dict_countries_pop)
    make_output(data, "Assignment4")


if __name__ == '__main__':
    main()
