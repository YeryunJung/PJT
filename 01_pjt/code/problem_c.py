import json
from pprint import pprint


def movie_info(movies, genres):
    def get_genres_name(movie, genres):
        ids = movie.get('genre_ids')
        genre_list = []

        # 장르 id가 맞는 요소를 찾아서 장르 name을 genre_list에 추가
        for i in ids:
            for j in range(len(genres)):
                if genres[j]['id'] == i:
                    genre_list.append(genres[j]['name'])
        
        result = {
        'id': movie['id'],
        'title': movie['title'],
        'poster_path': movie.get('poster_path'),
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_name': genre_list,
    }
        return result

    result = []
    for movie in movies:
        result.append(get_genres_name(movie, genres))
    return result

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
