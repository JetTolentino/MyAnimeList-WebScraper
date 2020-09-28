from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

my_url = 'https://myanimelist.net/anime/genre/6/Demons?page=1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html , 'html.parser')  #HTML parser 
containers = page_soup.findAll('div', {'class': 'seasonal-anime js-seasonal-anime'})     #anime list

container = containers[0]  
def get_title(container):
    title = container.div.div.h2.a.get_text()
    return title

def get_studio(container):
    studio = container.div.span.get_text()
    return studio

def get_episodes(container):
    episodes = container.find('div',{'class': 'eps'}).get_text().strip()   
    return episodes

genre_container = container.find('div', {'class': 'genres-inner js-genre-inner'}) #finds the genre container
genres = genre_container.findAll('a') #this is a list of genres 

def get_genre(container):
    genre_container = container.find('div', {'class': 'genres-inner js-genre-inner'}) #finds the genre container
    genres = genre_container.findAll('a') #this is a list of genres 
    ptr = 0
    genre = []
    while ptr < len(genres):                   
        g = genres[ptr].get_text()
        genre.append(g)                        #gets a list of genres
        ptr+=1
    return genre

def get_data():
    my_url = 'https://myanimelist.net/anime/genre/6/Demons?page=1'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html , 'html.parser')  #HTML parser 
    containers = page_soup.findAll('div', {'class': 'seasonal-anime js-seasonal-anime'})     #anime list

    #container = containers[0]   
    for container in containers:
        print(get_title(container))
        print(get_studio(container))
        print(get_episodes(container))
        print(get_genre(container))
    
    print(len(containers))

get_data()