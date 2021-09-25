import logging
import json
from sseclient import SSEClient
import pprint

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def with_urllib3(url):
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False)

def with_requests(url):
    import requests
    return requests.get(url, stream=True)



@app.route('/tic-tac-toe', methods=['POST'])
def tic_tac_toe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    id = data.get("battleId")
    url = 'https://cis2021-arena.herokuapp.com/tic-tac-toe/start/' + id
    print(url)
    response = with_urllib3(url)
    client = sseclint.SSEClient(respone)
    for event in client.event():
        pprint.pprint(json.loads(event.data))
    return 0
