# Golden Rapsberry Awards API

This project is meant to be an level 2 Richardson RESTful API
responsible for parsing it from an csv file, registering it on
a memory database (sqlite3 was chosen).

Main libraries used:
* numpy and pandas for numeric analysis.
* flask for managing backend connections and hosting API.
* re and json for data-structuring.
* sqlite3 in memory for database management.
* requests for connecting to the API.
Project structure:
```
.
├── README.md
├── api_texo.py
├── movieslist.csv
├── movies.json
├── texo_parser.py
├── db_connector.py
├── requirements.txt
├── api_test.py
```

* api_texo.py - flask application initialization.
* db_connector.py - all database operation functions.
* texo_parser.py - script for mapping the csv entries for the database structure.
* 
## Running 

1. Clone repository.
2. pip install requirements.txt
3. Start server by running python api_texo.py
4. You can use api_test.py to see examples of usage.

## Usage
GET http://127.0.0.1:5000/api/v1/movielist

returns a top 2 producers with more years between receiving a prize
and minor years between 2 prizes.

REQUEST
```python
    url_get = "http://127.0.0.1:5000/api/v1/movielist"
    get_results = requests.get(url_get)
    movies_json = json.loads(get_results.content)
    return movies_json
```
RESPONSE
```json
{
  'max': 
[
  {
    'followingWin': 2015, 
    'interval': 13, 
    'previousWin': 2002, 
    'producer': 'Matthew Vaughn'}, 
  {
    'followingWin': 1994, 
    'interval': 9, 
    'previousWin': 1985, 
    'producer': 'Buzz Feitshans'
  }], 
  'min':
  [
    {
      'followingWin': 1991, 
      'interval': 1, 
      'previousWin': 1990, 
      'producer': 'Joel Silver'}, 
    {
      'followingWin': 1990, 
      'interval': 6, 
      'previousWin': 1984, 
      'producer': 'Bo Derek'
    }]
}
```
POST http://127.0.0.1:5000/api/v1/add_producer

REQUEST
```python
    url_post = "http://127.0.0.1:5000/api/v1/add_producer"
    dict_post_example = {'followingWin': 2015, 'interval': 26, 'previousWin': 3015, 'producer': 'Egg Plant Monster of Eternal Void'}
    post_result = requests.post(url_post, json=dict_post_example)
    return post_result
```

```json
{
  'followingWin': 2015, 
  'interval': 26, 
  'previousWin': 3015, 
  'producer': 'Egg Plant Monster of Eternal Void'
}
```
RESPONSE
```text
    "<Response [200]>
```
DELETE http://127.0.0.1:5000/api/v1/delete_producer



REQUEST LAYOUT
```python
del_producer = requests.delete("http://127.0.0.1:5000/api/v1/delete_producer", data=producer)

```

RESPONSE
```text
if success:
    b'Producer data removed.'
if producer doesn't exists on database:
    b'Producer not found.'
```



PUT http://127.0.0.1:5000/api/v1/producer_update

REQUEST LAYOUT

```json
{
  'followingWin': 2018, 
  'interval': 125, 
  'previousWin': 3015, 
  'producer': 'Egg Plant Monster of Eternal Void'
}
```

RESPONSE

```text
<Response [200]>
```

PATCH http://127.0.0.1:5000/api/v1/<producer_change>/patch_producer
* <producer_change> will be used to select which one to change

REQUEST LAYOUT

```python
patch_request = requests.patch("http://127.0.0.1:5000/api/v1/eggmancer/patch_producer", json=json_patch)
```

```json
{
  'followingWin': 2015, 
  'interval': 26, 
  'previousWin': 3015,
  'producer': 'Egg Plant Monster of Eternal Void'
}

``` 


RESPONSE


```
if producer_change is different than producer name contained 
in json, the return will be:
<Response [200]>
producer informed on json is different from producer informed to change.

if both producer_change and producer name in json are the same:
<Response [200]>




``` 




