import logging
import json
import request
import sseclient

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
    #r = requests.get(url, stream=True, headers=headers)
    #print(r.txt)
    return json.dumps(url)
