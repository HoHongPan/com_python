import logging
import json
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/tic-tac-toe', methods=['POST'])
def tic_tac_toe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    id = data.get("battleId")
    url = 'https://cis2021-arena.herokuapp.com/tic-tac-toe/start/' + id
    table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(url)
    my_data = { "action": "putSymbol", "position": "SE"}
    s = requests.post(url, data = my_data)
    r = requests.get(url)
    print(r.read())
    return json.dumps(url)
