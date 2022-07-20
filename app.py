import os
import psycopg2
from flask import Flask, request, Response, jsonify
import json
import requests
import re
from flask_cors import CORS, cross_origin

from connection import DBConnet
from chapterManager import ChapterManaer

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

user = 'postgres'
passw = '123456'
host = '127.0.0.1'  
database = 'flask_pg'

obj = DBConnet(database , user , passw, host)

chapter_manager = ChapterManaer()
@app.route('/')
def index():
    #PostgreSQL(usuario, senha, host, porta, banco)
    return "Hello World"


@app.route('/request_manga', methods = ['POST'])
def manga():
    
    request_data = request.get_json()
    print("ye2")
    print(request_data["search"])

    command = "SELECT * FROM public.mangas WHERE title ILIKE '%{}%'".format(request_data["search"]) 
    print(command)
    result = obj.search(command)
    
    return jsonify(result)
    #return "OI"

@app.route('/request_list_chapter', methods = ['POST'])
def manga_chapter(debug=True):
    request_data = request.get_json()

    
    url = "https://mangatube.site/manga/" + request_data["search_site"]
    #print(url)
    
    r = requests.get(url)
    frase = list(filter(lambda x: ('"item": "https://mangatube.site/manga/' in x), r.text.split('\n')))[0]
    id = frase.split('/')[5].replace('"' , "")
    print(id)


    chapter_url = 'https://mangatube.site/jsons/series/chapters_list.json?page=1&order=desc&id_s={}'.format(id)
    print(id)
    result_c = requests.get(chapter_url)
    data_json = json.loads(result_c.text)
    #print(result_c.json())
    return result_c.json()

@app.route('/request_images' , methods = ['POST'])
def request_images():
    request_data = request.get_json()
    print(request_data["code"])
    url = 'https://mangatube.site/jsons/series/images_list.json?id_serie={}'.format(request_data["code"])

    result = requests.get(url)


    return result.json()

    