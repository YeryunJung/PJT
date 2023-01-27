import requests
from pprint import pprint

# movie_name = ['기생충', '그래비티', '검색할 수 없는 영화']

def recommendation(title):
    recommendation_list = []

    # 영화 제목을 URL의 쿼리로 넣어서 API 데이터를 가져오기
    search_URL = f'https://api.themoviedb.org/3/search/movie?api_key=8189d7f86439a7dd168ff05d6e420fb5&language=ko-KR&page=1&query={title}'
    search_response = requests.get(search_URL).json()
    if len(search_response['results']) == 0:
        return None

    # 검색한 정보에서 id 추출해서 추천 영화 정보를 가져오기
    first_id = search_response['results'][0]['id']
    recommendation_URL = f'https://api.themoviedb.org/3/movie/{first_id}/recommendations?api_key=8189d7f86439a7dd168ff05d6e420fb5&language=ko-KR&page=1'
    recommendation_response = requests.get(recommendation_URL).json()['results']
    if len(recommendation_response) == 0:
        return []
    
    # 추천 영화를 목록으로 가공하기
    for el in recommendation_response:
        recommendation_list.append(el['title'])
        
    return recommendation_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
