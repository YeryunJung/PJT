import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key': '8189d7f86439a7dd168ff05d6e420fb5',
        'language': 'ko-KR',
        'page': '1',
    }
    response = requests.get(URL, params=params).json()
    count = len(response['results'])
    return count

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
