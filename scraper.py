from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys
  
def get_title(container):
    title = container.div.div.h2.a.get_text()
    return title

def get_studio(container):
    studio = container.div.span.get_text()
    return studio

def get_episodes(container):
    episodes = container.find('div',{'class': 'eps'}).get_text().strip()
    try:
        episode =int(episodes.replace(' eps', ''))
    except:
        try:
            episode =int(episodes.replace(' ep', ''))
        except:
            episode = "Unavailable"
    
    return episode

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

def get_score(container):
    score = container.find('span', {'title': 'Score'}).get_text().strip()
    return score

def get_data(genre):
    page = 1
    end_of_pages = False
    num_anime = 0
    genres_key = {"action":"1",
              "adventure": "2",
              "cars": "3",
              "comedy":"4",
              "dementia":"5",
              "demons":"6",
              "drama": "8",
              "ecchi": "9",
              "fantasy": "10",
              "game":"11",
              "harem":"35",
              "historical":"13",
              "horror":"14",
              "josei": "43",
              "kids": "15",
              "magic": "16",
              "martial arts": "17",
              "mecha": "18",
              "military": "38",
              "music":"19",
              "mystery":"7",
              "parody":"20",
              "police":"39",
              "psychological": "40",
              "romance": "22",
              "samurai":"21",
              "school":"23",
              "sci-fi":"24",
              "seinen": "42",
              "shoujo":"25",
              "shoujo-ai":"26",
              "shounen": "27",
              "shounen-ai":"28",
              "slice of life":"36",
              "space": "29",
              "sports": "30",
              "super power": "31",
              "supernatural":"37",
              "thriller":"41",
              "vampire":"32"}

    genres = {"action":"action",
              "adventure": "adventure",
              "cars": "cars",
              "comedy":"comedy",
              "dementia":"dementia",
              "demons":"demons",
              "drama": "drama",
              "ecchi": "ecchi",
              "fantasy": "fantasy",
              "game":"game",
              "harem":"harem",
              "historical":"historical",
              "horror":"horror",
              "josei": "josei",
              "kids": "kids",
              "magic": "magic",
              "martial arts": "martial_arts",
              "mecha": "mecha",
              "military": "military",
              "music":"music",
              "mystery":"mystery",
              "parody":"parody",
              "police":"police",
              "psychological": "psychological",
              "romance": "romance",
              "samurai":"samurai",
              "school":"school",
              "sci-fi":"sci_fi",
              "seinen": "seinen",
              "shoujo":"shoujo",
              "shoujo-ai":"shoujo_ai",
              "shounen": "shounen",
              "shounen-ai":"shounen_ai",
              "slice of life":"slice_of_life",
              "space": "space",
              "sports": "sports",
              "super power": "super_power",
              "supernatural":"supernatural",
              "thriller":"thriller",
              "vampire":"vampire"}
    while not end_of_pages:
        page_string= str(page)
        try:
            my_url = f'https://myanimelist.net/anime/genre/{genres_key[genre]}/{genres[genre]}?page={page_string}'
            uClient = uReq(my_url)
            page_html = uClient.read()
            #uClient.close()
            page_soup = soup(page_html , 'html.parser')  #HTML parser 
            containers = page_soup.findAll('div', {'class': 'seasonal-anime js-seasonal-anime'})
            page += 1

        except:
            end_of_pages = True

        #container = containers[0]   
        for container in containers:
            print(get_title(container))
            print(get_studio(container))
            print(get_episodes(container))
            print(get_genre(container))
            print(get_score(container))
        if not end_of_pages:    
            num_anime += len(containers) #number of anime in a page
        print(my_url)
        print(num_anime)
        print(f"{genres[genre]}")


    





if __name__ == "__main__":
    genre = input("Enter genre: ")
    get_data(genre)