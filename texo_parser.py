import numpy
import pandas
import json
import re

import db_connector
from db_connector import insert_db

class Producer:
    def __init__(self, name):
        self.title = []
        self.time = None
        self.name = name

    def first_title(self, year):
        self.first_year_title = year

    def last_title(self, year):
        self.last_year_title = year

    def titles(self,year):
        self.title.append(year)

    def time_prizes(self, time):
        self.time = time

csv_file = 'movielist.csv'
json_dest = 'movies.json'

def parse_csv_json(csv_file, json_dest):
    df = pandas.read_csv(csv_file, on_bad_lines='skip', sep=';')
    df.to_json(json_dest)

producers_winners = []
producers_winners_obj = [] #Database of objects containing

def return_awards():

    parse_csv_json(csv_file, json_dest)

    with open('movies.json','r') as json_movies:
        movielist = json.loads(json_movies.read())

        for i in range(len(movielist['winner'])):
            x = str(i)
            producers_name = str(movielist['producers'][x])
            if movielist['winner'][x]:
                year = int(movielist['year'][x])
                movie = movielist['title'][x]
                for producer_name in re.split(' and |,', producers_name):
                    if producer_name: #check if string is empty
                        producer_name = producer_name.lstrip()
                        if producer_name not in producers_winners:
                            producers_winners.append(producer_name)
                            producer = Producer(name=producer_name)
                            producer.titles(year)
                            producer.last_title(year)
                            producer.first_title(year)
                            producers_winners_obj.append(producer)
                        else:
                            for prod_obj in producers_winners_obj:
                                if producer_name == prod_obj.name:
                                    prod_obj.titles(year)
                                    if prod_obj.last_year_title < year:
                                        prod_obj.last_title(year)
                                    elif prod_obj.first_year_title > year:
                                        prod_obj.first_title(year)
                                    break



def time_between_title():
    list_time = []
    for _ in producers_winners_obj:
            titles_difference = numpy.diff(_.title)
            _.time_prizes(titles_difference)
            if titles_difference.size > 0:
                print(f"Inserindo dados de {_.name}")
                insert_db(_.name, int(_.time[0]), _.first_year_title, _.last_year_title)
                list_time.append(_.time[0])
    return list_time


def return_min_title(list_time):
    list_time.sort()
    list_min_winners =[]
    list_min_obj = []
    list_min_winners.append(list_time[0])
    list_min_winners.append(list_time[1])
    for _ in producers_winners_obj:
        for prod_year in list_min_winners:
            if prod_year.size > 0 and prod_year in _.time:
                list_min_obj.append(_)
    return list_min_obj

def return_max_title(list_time):
    list_time.sort(reverse=True)
    list_max_winners =[]
    list_max_obj = []
    list_max_winners.append(list_time[0])
    list_max_winners.append(list_time[1])
    for _ in producers_winners_obj:
        for prod_year in list_max_winners:
            if prod_year.size > 0:
                if prod_year in _.time:
                    list_max_obj.append(_)
    return list_max_obj



if __name__ == '__main__':

    db_connector.cria_db()

    return_awards()

    list_time = time_between_title()

    max_winners = db_connector.select_max_winners()

    for max in max_winners:
        print(max)

    min_winners = db_connector.select_min_winners()

    print(min_winners)

    for min in min_winners:
        print(min)

    list_min_winners = []

    print(list_time)

    db_connector.cursor.close()

    return_min_title(list_time)

    return_max_title(list_time)
