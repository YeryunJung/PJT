import json

# 모든 영화중 12월에 개봉한 영화들의 제목 리스트를 출력
def dec_movies(movies):
    # movies.json 파일에서 각 영화의 id 리스트를 추출
    id_list = []
    for i in range(len(movies)):
        id_list.append(movies[i]['id'])

    dec_list = []
    # 추출한 id 리스트를 적용한 파일이름을 반복해서 열기
    for id in id_list:
        movies_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movies_list = json.load(movies_json)

        # 12월에 개봉하는 영화를 dec_list에 추가
        month = movies_list['release_date'][5:7]
        if month == '12':
            dec_list.append(movies_list['title'])
    
    return dec_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
