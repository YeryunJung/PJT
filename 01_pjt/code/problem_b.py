import json
from pprint import pprint

# 장르 번호가 아닌 장르 이름 리스트로 바꿔 반환하는 함수

def movie_info(movie, genres):
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

    

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
