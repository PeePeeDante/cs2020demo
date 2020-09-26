import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSalad(): # cannot have same method name 
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");

    minCost = 101
    for street in data["salad_prices_street_map"]:
        temp_minCost = minCostStreet(data["number_of_salads"], street)
        if (temp_minCost < minCost):
            minCost = temp_minCost

    if (minCost == 101):
        minCost = 0

    logging.info("My result: {}".format(minCost))
    return jsonify(result=minCost)

def minCostStreet(n, street):
    
    street_size = len(street)
    
    i=0
    j=i
    cost = 101
    while (j < street_size):

        if (street[j]!="X" and j!=street_size-1):
            j+=1
        else:
            if (street[j] != "X" and j==street_size-1):
                j+=1

            if (i==j):
                i+=1
                j+=1
                continue
            
            temp_cost = minSubarray(i,j-1,n,street)
            if (temp_cost < cost):
                cost = temp_cost
            j+=1
            i=j

    return cost

def minSubarray(start,end,n,street):
    
    if (n > end-start+1):
        return 101

    res = 0
    for i in range(n):
        res += int(street[start+i])

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    curr_sum = res
    for i in range(start+n, end+1):
        curr_sum += int(street[i]) - int(street[i-n])
        res = min(res, curr_sum)

    return res





