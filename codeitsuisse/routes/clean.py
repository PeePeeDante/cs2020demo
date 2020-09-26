import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluateClean(): # cannot have same method name 
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");

    result = {"answers":{}}

    for test_case in data["tests"]:
        s = stepsRequired(data["tests"][test_case]["floor"])
        result["answers"][test_case] = s 

    logging.info("My result: {}".format(result))
    return jsonify(result)

def stepsRequired(floor):
    total_steps = 0
    for i in range(len(floor)-1):
        if i == len(floor)-2:
            if (floor[i] == 1) and (floor[i+1] == 1):
                return total_steps + 2
            elif (floor[i] == 1) and (floor[i+1] == 0):
                return total_steps + 3
            elif (floor[i] == 0) and (floor[i+1] == 0):
                return total_steps
        total_steps += 2*floor[i]+1
        if (floor[i+1]-floor[i]-1>=0):
            floor[i+1] = floor[i+1]-floor[i]-1
        else:
            if ((floor[i+1]-floor[i]-1)%2):
                floor[i+1]=1
            else:
                floor[i+1]=0
        
    remain = floor[len(floor)-1]
    if (remain%2):
        total_steps += 2*remain+1
    else:
        total_steps += 2*remain
    return total_steps
