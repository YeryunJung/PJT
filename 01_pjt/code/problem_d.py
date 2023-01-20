import json

# 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성

def max_revenue(movies):
    # movies.json 파일에서 각 영화의 id 리스트를 추출
    id_list = []
    for i in range(len(movies)):
        id_list.append(movies[i]['id'])
    
    max = 0
    max_title = ''
    # 추출한 id 리스트를 적용한 파일이름을 반복해서 열기
    for id in id_list:
        movies_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movies_list = json.load(movies_json)

        # 수익이 가장 높은 영화 제목 추출
        if movies_list['revenue'] > max:
            max = movies_list['revenue']
            max_title = movies_list['title']
    
    return max_title
    
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
