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
    messages = SSEClient(url)

    for msg in messages:
        outputMsg = msg.data
        if type(outputMsg) is not str:
            outputJS = json.loads(outputMsg)
            FilterName = "data"
            print(outputJS[FilterName])
    return json.dumps(url)
