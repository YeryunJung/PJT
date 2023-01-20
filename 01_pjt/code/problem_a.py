import json
from pprint import pprint


def movie_info(movie):
    # pprint(movie)
    # id, title, poster_path, vote_average, overview, genre_ids
   result = {
    'id': movie['id'],
    'title': movie['title'],
    'poster_path': movie.get('poster_path'),
    'vote_average': movie['vote_average'],
    'overview': movie['overview'],
    'genre_ids': movie.get('genre_ids'),
   }
   return result

# movie.get # 해당 key가 있으면 해당 value를 반환, 없으면 None을 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
