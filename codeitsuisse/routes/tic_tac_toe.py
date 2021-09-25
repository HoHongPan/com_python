import logging
import json
import urllib.request
import urllib.parse

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
    r = urllib.request.urlopen(url, timeout= 0.0001)
    print(r.read().decode('utf-8'))
    return json.dumps(url)
