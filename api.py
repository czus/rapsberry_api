import flask
import parser
import db_connector
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/', methods=['GET'])
def home():
    return '''<h1>Rapsberry Golden Awards!</h1>
<p>.........................................................</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/movielist', methods=['GET'])
def list_winners():

    list_min_winners = db_connector.select_min_winners()
    list_max_winners = db_connector.select_max_winners()

    awards = {
        "min": [
            {
                "producer": list_min_winners[0][0],
                "interval": list_min_winners[0][1],
                "previousWin": list_min_winners[0][2],
                "followingWin": list_min_winners[0][3]
            },
        ],
        "max": [
            {
                "producer": list_max_winners[0][0],
                "interval": list_max_winners[0][1],
                "previousWin": list_max_winners[0][2],
                "followingWin": list_max_winners[0][3]
            },
        ]
    }

    return jsonify(awards)

@app.route('/api/v1/db_select', methods=['GET'])
def list_db():
    if request.data:
        producer = str(request.data.decode('utf-8'))
        result = db_connector.search_producer(producer)
        return jsonify(result)
    else:
        return "Nothing found"

@app.route('/api/v1/delete_producer', methods=['DELETE'])
def delete_producer():
    producer = str(request.data.decode('utf-8'))
    return db_connector.delete(producer)

@app.route('/api/v1/list_producers', methods=['GET'])
def list_producers():
    return jsonify(db_connector.search_all_producers())


@app.route('/api/v1/producer_update', methods=['PUT'])
def update_producer():
    producer = request.json
    print(producer)
    return(db_connector.update_producer(producer))


@app.route("/api/v1/add_producer",methods=['POST'])
def add_producer():
    content = request.json
    producer = content['producer']
    interval = content['interval']
    followingWin = content['followingWin']
    previousWin = content['previousWin']
    db_connector.insert_db(producer, interval, previousWin, followingWin)
    return(content)

@app.route('/api/v1/<producer_change>/patch_producer', methods=['PATCH'])
def patch_producer(producer_change):
    content = request.json
    return db_connector.patch_db(content, producer_change)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':

    db_connector.cria_db()

    parser.return_awards()
    list_winners = parser.time_between_title()

    list_min_winners = db_connector.select_min_winners()

    list_max_winners = db_connector.select_max_winners()

    awards = {
        "min": [
            {
                "producer": list_min_winners[0][0],
                "interval": list_min_winners[0][1],
                "previousWin": list_min_winners[0][2],
                "followingWin": list_min_winners[0][3]
            },
        ],
        "max": [
            {
                "producer": list_max_winners[0][0],
                "interval": list_max_winners[0][1],
                "previousWin": list_max_winners[0][2],
                "followingWin": list_max_winners[0][3]
            },
        ]
    }

    app.run()
