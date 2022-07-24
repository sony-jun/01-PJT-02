#- 인기 영화 목록의 개수를 출력합니다.
#- requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
#- 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.

import requests


def popular_count():
    base_url ='https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key' : '70e057d1ff42d2f6a5d09f508a9b1d70', 
    'language' : 'ko-KR'
}
    response = requests.get(base_url+path, params).json()  #여기서 왜?
    return(response)

    popular_count = 0
    for i in response:
        if 'original_title' in response:
            popular_count += 1
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
