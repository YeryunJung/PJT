import requests
from pprint import pprint

movie_name = ['기생충', '검색할 수 없는 영화']

def credits(title):
    result = {'cast': [], 'directing': []}

    # 영화 제목을 URL의 쿼리로 넣어서 API 데이터를 가져오기
    search_URL = f'https://api.themoviedb.org/3/search/movie?api_key=8189d7f86439a7dd168ff05d6e420fb5&language=ko-KR&query={title}'
    search_response = requests.get(search_URL).json()
    if len(search_response['results']) == 0:
        return None
    
    # 검색한 정보에서 id 추출해서 출연진과 연출진 정보를 가져오기
    first_id = search_response['results'][0]['id']
    credits_URL = f'https://api.themoviedb.org/3//movie/{first_id}/credits?api_key=8189d7f86439a7dd168ff05d6e420fb5&language=ko-KR'
    credits_response = requests.get(credits_URL).json()

    # 리스트 합친 후 추출
    # staff_list = credits_response['cast'] + credits_response['crew']
    # 
    # for staff in staff_list:
    #     if cast_id in staff and staff['cast_id'] < 10:
    #         result['cast'].append(staff['name'])
        # if department in staff and staff['department'] == 'Directing':
        #     result['directing'].append(staff['name'])

    # 조건에 맞는 출연진과 연출진 정보 반환하기
    casting_list = credits_response['cast']
    crew_list = credits_response['crew']
    
    for el in casting_list:
        if el['cast_id'] < 10:
            result['cast'].append(el['name'])
    for el in crew_list:
        if el['department'] == 'Directing':
            if not el['original_name'] in result['directing']:
                result['directing'].append(el['name'])
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
