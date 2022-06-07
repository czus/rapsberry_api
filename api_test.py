import json
import requests

def put_producers():
    url_update = "http://127.0.0.1:5000/api/v1/producer_update"
    dict_update_example = {'followingWin': 2018, 'interval': 125, 'previousWin': 3015, 'producer': 'Egg Plant Monster of Eternal Void'}
    update_req = requests.put(url_update, json=dict_update_example)
    return update_req

def post_producers():
    url_post = "http://127.0.0.1:5000/api/v1/add_producer"
    dict_post_example = {'followingWin': 2015, 'interval': 26, 'previousWin': 3015, 'producer': 'Egg Plant Monster of Eternal Void'}
    post_result = requests.post(url_post, json=dict_post_example)
    return post_result

def get_producers():
    url_get = "http://127.0.0.1:5000/api/v1/movielist"
    get_results = requests.get(url_get)
    movies_json = json.loads(get_results.content)
    return movies_json


def get_producer(producer):
    get_producer = requests.get("http://127.0.0.1:5000/api/v1/db_select", data=producer)
    print(get_producer.content)
#teste_get = requests.get(url_get)
#print(teste_get.content)



def delete_producer(producer):
    del_producer = requests.delete("http://127.0.0.1:5000/api/v1/delete_producer", data=producer)
    print(del_producer.content)


def patch_producer():
    json_patch = {'followingWin': 2015, 'interval': 26, 'previousWin': 3015,'producer': 'eggmancer'}

    patch_request = requests.patch("http://127.0.0.1:5000/api/v1/eggmancer/patch_producer", json=json_patch)
    return patch_request

if __name__ == '__main__':

   # print(get_producers())
    #post_content = post_producers()
    #print(post_producers())

    #print(get_producer("Egg Plant Monster of Eternal Void"))

    #print(delete_producer("Bo Derek"))
    print(patch_producer())