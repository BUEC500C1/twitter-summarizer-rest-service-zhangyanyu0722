from requests import put, get, post, delete

result_1 = post('http://127.0.0.1:5000/twitter/BU_Tweets').json()
print(result_1)
result_2 = delete('http://127.0.0.1:5000/twitter/BU_Tweets').json()
print(result_2)
# result_3 = put('http://127.0.0.1:5000/twitter/BU_Tweets', data={'twitter_name': 'BU_Tweets'}).json()
# print(result_3)
# result_4 = post('http://127.0.0.1:5000/twitter/BU_ece').json()
# print(result_4)
get('http://127.0.0.1:5000/twitter/BU_ece').json()
