# coding=UTF-8
import urllib.request as url
import sys
from unidecode import unidecode
from bs4 import BeautifulSoup
from datetime import date, timedelta

def get_movies_shedule(cinema, city='france'):
    data = []
    movie_date = date.today()
    cinema = unidecode(cinema)
    cinema = cinema.replace(' ', '+')
    for day in range(0, 7):
        try:
            html = url.urlopen('https://www.google.fr/movies?near=' + city + '&q=' + cinema + '&date=' + str(day)).read()
        except:
            print ("Query Error. Exiting...")
            sys.exit(1)
        soup = BeautifulSoup(html, "html.parser")
        for info in soup.find_all('div', class_="movie"):
            data.append(movie_tuple(info, movie_date))
        movie_date += timedelta(1)
    return sorted(data)

def movie_tuple(info, date):
    shedule = []
    time_format = 5
    movies = info.get_text('|').split('|')
    movie = (movies[0] if movies[0].find('3D') == -1 else movies[0][:-4], date.isoformat(), shedule,
             '2D' if movies[0].find('3D') == -1 else '3D', "VF (VO)" if len(movies[2]) == time_format else movies[2])
    for time in movies:
        if len(time) == time_format:
            shedule.append(time)
    return movie

def write_movies_shedule(cinema, city='france'):
    data = get_movies_shedule(cinema, city)
    with open("movies_shedule.txt", "w") as file:
        if not data:
            file.write ("No result Found.")
        for movie in data:
            for show in movie[2]:
                file.write ('{0:50}{1}\t{2}\t{3}\t{4}\n'.format(movie[0], movie[1], show, movie[3], movie[4]))

write_movies_shedule('mk2 bibliothèque')
print ("SUCCESS")
