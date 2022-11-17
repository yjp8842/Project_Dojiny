import requests
import json

def get_director(movie_id):
    BASE_URL = 'https://api.themoviedb.org/3'
    movie_id = movie_id
    PATH1 = f'/movie/{movie_id}/credits'
    my_params = {
        'api_key' : 'c23cd6fb816b2263bfdfecf34a8a6805',
    }
    response = requests.get(BASE_URL + PATH1, params = my_params).json()
    result = response.get("crew")
    # person id 가져오기
    director = 0
    for p in result:
        if p.get("job") == "Director":
            director = p.get("id")
    # 한글로 이름 가져오기
    PATH2 = f'/person/{director}'
    my_params = {
        'api_key' : 'c23cd6fb816b2263bfdfecf34a8a6805',
        'language' : 'ko-KR'
    }
    response = requests.get(BASE_URL + PATH2, params = my_params).json()
    result = response.get('also_known_as')
    name = []
    if result :
        for r in result:
            if r.isalpha():
                name.append(r)
                return name
            else:
                name = []
                name.append(response.get("name"))
                return name
        return name
    else :
        name.append(response.get("name"))
        return name


def get_movies_detail(movie_id):
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = f'/movie/{movie_id}'
    my_params = {
        'api_key' : 'c23cd6fb816b2263bfdfecf34a8a6805',
        'language' : 'ko',
    }
    response = requests.get(BASE_URL + PATH, params = my_params).json()
    return response


def get_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/now_playing'
    my_params = {
        'api_key' : 'c23cd6fb816b2263bfdfecf34a8a6805',
        'language' : 'ko',
        'region' : 'KR',
    }
    response = requests.get(BASE_URL + PATH, params = my_params).json()
    result = response.get('results')
    movies = []
    for r in result:
        genres = []
        name = 0
        for n in get_director(r.get('id')):
            name = n
        detail = get_movies_detail(r.get('id'))
        for i, d in enumerate(detail.get("genres")):
            genres.append(d.get("name"))

        objects = {
            "model": "movies.movie",
            "fields": {
                'movie_id' : r.get('id'),
                'original_title': r.get('original_title'),
                'title': r.get('title'),
                'overview': r.get('overview'),
                'genres': genres,
                'release_date': r.get('release_date'),
                'vote_average': r.get('vote_average'),
                'backdrop_path': r.get('backdrop_path'),
                'runtime': detail.get('runtime'),
                'director': name,
                'poster_path': r.get('poster_path'),
            }
        }
        
        movies.append(objects)

    with open('movies.json', 'w', encoding='utf-8') as f :
        json.dump(movies, f, ensure_ascii=False, indent=4)
        
get_movies()