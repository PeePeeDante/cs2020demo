import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluateSearch(): # cannot have same method name 
    #data = request.get_json()
    d = request.get_data()
    data = json.loads(d)
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");

    answer = []

    for i in range(len(data)):
        search_wd = data[i]["searchItemName"]
        key_list = data[i]["items"]
        oper_list = []
        cost_list = []
        answer.append({"searchItemName": search_wd, "searchResult": []})

        for key in key_list:
            oper, cost = getOperations(key, search_wd)
            oper_list += oper
            cost_list += cost

    # [{"searchItemName":"Samsung Aircon","searchResult":["-Samsung+h Aircon","Samsung+a Air-con","S-ams-ung Au-r-con"]}]

        while(cost_list!=[]):
            m_index = cost_list.index(min(cost_list))
            answer[i]["searchResult"].append(oper_list[m_index])
            cost_list.pop(m_index)
            oper_list.pop(m_index)

    logging.info("My result: {}".format(answer))
    return json.dumps(answer)

def getOperations(key, search_wd):

    keyLen = len(key)  # input
    wdLen = len(search_wd)  # item

    dp = [None]*(wdLen+1)
    op = [None]*(wdLen+1)
    for i in range(wdLen+1):
        dp[i] = [1000000]*(keyLen+1)
        op[i] = [None]*(keyLen+1)

    dp[0][0] = 0
    op[0][0] = '0'

    for i in range(1, wdLen+1):
        dp[i][0] = i
        op[i][0] = '-'

    for i in range(1, keyLen+1):
        dp[0][i] = i
        op[0][i] = '+'

    for i in range(1, wdLen+1):
        for j in range(1, keyLen+1):
            cost = dp[i-1][j-1]
            op[i][j] = '0'
            if (key[j-1].lower() != search_wd[i-1].lower()):
                cost += 1
                op[i][j] = 's'

            inscost = dp[i][j-1]+1
            if (inscost <= cost):
                cost = inscost
                op[i][j] = '+'

            delcost = dp[i-1][j]+1
            if (delcost <= cost):
                cost = delcost
                op[i][j] = '-'

            dp[i][j] = cost

    result = ""
    i = wdLen
    j = keyLen
    while (i > 0 or j > 0):
        if (op[i][j] == '0'):
            result = search_wd[i-1] + result
            i -= 1
            j -= 1

        elif (op[i][j] == '+'):
            result = '+' + key[j-1] + result
            j -= 1

        elif (op[i][j] == '-'):
            result = '-' + search_wd[i-1] + result
            i -= 1

        elif (op[i][j] == 's'):
            result = key[j-1] + result
            i -= 1
            j -= 1

    return [result], [dp[wdLen][keyLen]]
            

        

    



